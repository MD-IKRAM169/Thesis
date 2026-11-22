#!/usr/bin/env python3
"""Read-only structural checks for the original thesis PDF and PowerPoint.

These tests do not verify scholarly/clinical claims, privacy, or file safety.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import zipfile


def inspect_pdf(path: Path) -> dict[str, object]:
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    size = path.stat().st_size
    if size < 20:
        raise ValueError("PDF is unexpectedly small")
    with path.open("rb") as stream:
        header = stream.read(5)
        stream.seek(max(0, size - 32768))
        trailer = stream.read()
    if header != b"%PDF-":
        raise ValueError("Missing PDF header")
    if b"%%EOF" not in trailer:
        raise ValueError("Missing PDF end-of-file marker")
    return {"file": path.name, "kind": "PDF", "bytes": size, "basic_structure": "ok"}


def inspect_pptx(path: Path) -> dict[str, object]:
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    if not zipfile.is_zipfile(path):
        raise ValueError("PPTX is not a valid ZIP package")
    with zipfile.ZipFile(path) as presentation:
        names = set(presentation.namelist())
        required = {"[Content_Types].xml", "ppt/presentation.xml"}
        if not required.issubset(names):
            raise ValueError("Missing required PPTX package components")
        corrupted = presentation.testzip()
        if corrupted is not None:
            raise ValueError(f"PPTX ZIP CRC failed: {corrupted}")
        slides = sorted(p for p in names
                        if p.startswith("ppt/slides/slide") and p.endswith(".xml"))
        if not slides:
            raise ValueError("No PowerPoint slide XML files found")
    return {"file": path.name, "kind": "PPTX",
            "bytes": path.stat().st_size, "slide_xml_count": len(slides),
            "basic_structure": "ok"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, default=Path("."),
                        help="Repository root")
    args = parser.parse_args(argv)
    try:
        report = inspect_pdf(args.directory / "Suicidal_Prediction-Final.pdf")
        slides = inspect_pptx(args.directory / "Prediction of suicidal behavior.pptx")
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"Artifact check failed: {exc}")
        return 1
    for result in (report, slides):
        print(f"OK: {result['kind']} {result['file']} ({result['bytes']:,} bytes)")
    print("Basic file structure checked; scholarly and clinical validity NOT assessed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
