# Fictional-data demonstration only; NOT the thesis analysis or a clinical model.
# Install with: install.packages("leaps")
# Run: Rscript examples/subset_selection_demo.R

if (!requireNamespace("leaps", quietly = TRUE)) {
  stop('The optional "leaps" R package is required; run install.packages("leaps")')
}
set.seed(42)
n <- 80L
sample_data <- data.frame(
  writing_length = rnorm(n, mean = 100, sd = 10),
  token_diversity = runif(n, min = 0.2, max = 0.9),
  punctuation_rate = runif(n, min = 0, max = 0.1),
  synthetic_score = rnorm(n)
)
selection <- leaps::regsubsets(
  synthetic_score ~ writing_length + token_diversity + punctuation_rate,
  data = sample_data, nvmax = 3
)
print(summary(selection)$which)
cat("Illustrative fictional data only; no clinical or thesis results.\n")
