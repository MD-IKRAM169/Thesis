"""Offline unit tests that do not access any original thesis participant data."""
from pathlib import Path
import tempfile
import unittest
import zipfile
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.verify_artifacts import inspect_pdf, inspect_pptx  # noqa: E402


class DocumentTests(unittest.TestCase):
    def test_valid_minimal_pdf_header_trailer(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "example.pdf"
            path.write_bytes(b"%PDF-1.7\n1 0 obj\n<<>>\nendobj\n%%EOF\n")
            self.assertEqual(inspect_pdf(path)["kind"], "PDF")

    def test_rejects_bad_pdf(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.pdf"
            path.write_bytes(b"this is not a pdf\n" * 6)
            with self.assertRaisesRegex(ValueError, "header"):
                inspect_pdf(path)

    def test_valid_pptx(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "sample.pptx"
            with zipfile.ZipFile(path, "w") as z:
                z.writestr("[Content_Types].xml", "<Types/>")
                z.writestr("ppt/presentation.xml", "<p:presentation/>")
                z.writestr("ppt/slides/slide1.xml", "<p:sld/>")
            self.assertEqual(inspect_pptx(path)["slide_xml_count"], 1)

    def test_rejects_invalid_pptx(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.pptx"
            with zipfile.ZipFile(path, "w") as z:
                z.writestr("random.txt", "not a slide")
            with self.assertRaisesRegex(ValueError, "required PPTX"):
                inspect_pptx(path)

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(FileNotFoundError):
                inspect_pdf(Path(folder) / "missing.pdf")


if __name__ == "__main__":
    unittest.main()
