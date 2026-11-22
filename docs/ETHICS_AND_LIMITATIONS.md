# Ethics, privacy and limitations

This project concerns sensitive mental-health outcomes and historical social-media accounts. Content formerly visible to the public may remain identifiable or sensitive and may be governed by platform terms and research-ethics requirements.

## Boundaries

- **No individual assessment:** Do not use the thesis to assess suicide risk or infer health information about any identifiable person.
- **No clinical deployment:** The work is not a clinically evaluated screening tool, diagnosis system or crisis-response application.
- **No causal inference:** Feature selection does not prove a language category causes an outcome.
- **No raw account datasets on GitHub:** Do not commit account-labeled social-media exports or personal posts from the uploaded ZIP.
- **No secrets:** The separate archive contains files named as API tokens/passwords. Revoke or rotate anything that may still be active.
- **Third-party literature:** Link to papers rather than republishing PDFs without authorization.

## Research-quality concerns

1. Historical data appears to be a **small nonrandom sample**, potentially affected by selection, survivorship and reporting biases.
2. Draft collection notes mention **68 + 67 = 135** CSV files but the analysis matrix contains **132 observations**; exclusions or deduplication are undocumented.
3. Labels drawn from public stories or sources are **not equivalent to validated current clinical assessments**.
4. Translation and LIWC vocabulary categories may vary by language, culture and historical context.
5. A small dataset combined with exploratory feature selection increases overfitting and leakage risks without carefully designed external evaluation.
6. The supplied documents do not establish independent holdout results, subgroup assessment, probability calibration or clinically validated thresholds.
7. Associations involving a category such as `leisure` should not be used for personal surveillance or risk classification.

## Before any further research or publication

Seek appropriate ethical and institutional review, establish permissions for data access/use, validate data labels and sampling procedures, document reproducible processing decisions, and involve domain experts. This repository is intended to explain historical research rather than enable targeting or prediction for individuals.
