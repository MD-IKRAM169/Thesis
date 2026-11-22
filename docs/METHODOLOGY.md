# Methodology — historical thesis narrative

This page summarizes the previously supplied working documents, including `F Thesis paper.docx` and chapter drafts. Drafts may not exactly match the final PDF. These are historical descriptions, not independently reproduced experiments.

## Stages described

1. **Data collection:** Historical Twitter profiles manually identified, posts collected using Twitter API tools and group labels assigned. The draft mentions **68** CSV files in one group and **67** in another; later R output reports **132 observations**. The difference has not been reconciled.
2. **Preprocessing:** Translation to English and cleaning/normalization. Exact translation version and data lineage were not preserved as a reproducible public pipeline.
3. **Features:** Linguistic Inquiry and Word Count (**LIWC**) word categories, including language and psychological-process categories.
4. **Feature table:** A data frame reported as **132 observations, 71 variables** including its target/group column.
5. **Exploratory subset selection:** The R `leaps::regsubsets()` function was used with different subset sizes (`nvmax`).
6. **Interpretation:** The word category `leisure` was mentioned repeatedly in selected subsets.

## What the available evidence cannot establish

- A defensible account-level sampling frame, permission to redistribute posts, or verified label validity.
- Stable Twitter API, translation or LIWC dictionary versions.
- Complete source code and a reproducible preprocessing pipeline.
- Independent held-out or prospective evaluation, calibrated risk scores, or clinically relevant metrics.
- Agreement between every working chapter and the final public PDF.

## Statistical interpretation

Subset selection is **exploratory**. Selecting a language feature cannot establish causation or reliable individual prediction. Group comparisons are sensitive to how samples were formed and to potential leakage. The [synthetic R example](../examples/subset_selection_demo.R) illustrates function syntax only and is **not** an attempt to replicate mental-health findings.
