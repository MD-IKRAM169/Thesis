# Reproducibility and artifact status

## Original public files

The original GitHub repository contained:
- `Suicidal_Prediction-Final.pdf` — historical written thesis.
- `Prediction of suicidal behavior.pptx` — historical presentation.

The separately supplied `Thesis.zip` contains working thesis chapters, original data, literature and files named as access credentials. That ZIP and its sensitive contents **are not redistributed here**.

## What can be rerun

- Basic PDF and PowerPoint file-structure checks, via Python's standard library.
- An optional demonstration of `leaps::regsubsets()` using **fictional data**, if R and the `leaps` package are available.

Neither activity validates a clinical conclusion or reproduces the thesis findings.

```bash
python tools/verify_artifacts.py
python -m unittest discover -s tests -v

# Optional: R with the leaps package installed
Rscript examples/subset_selection_demo.R
```

## What is needed for genuine research reproduction

- A privacy-reviewed shareable data derivative and consent/data-use documentation.
- Documented sampling and independently reviewed target/group labels.
- Exact feature definitions, proprietary LIWC dictionary version and preprocessing/translation choices.
- Scripts and package versions that regenerate the 132-row analysis table.
- Documentation reconciling source file counts with analysis rows.
- Reproducible held-out model evaluation with appropriate independent validation.

The current checks address **document integrity only**, not scientific reproducibility.
