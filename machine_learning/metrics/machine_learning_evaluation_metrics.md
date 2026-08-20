# Machine Learning Evaluation Metrics

## 1. Classification Metrics

Assume:

- True label: \(y_i\)
- Predicted label: \(\hat{y}_i\)
- Number of samples: \(N\)

Confusion Matrix:

| | Predicted Positive | Predicted Negative |
|---|---|---|
| Actual Positive | TP | FN |
| Actual Negative | FP | TN |


---

## Accuracy

The proportion of correctly classified samples.

$$
Accuracy=
\frac{TP+TN}
{TP+TN+FP+FN}
$$


---

## Precision

The proportion of true positive predictions among all positive predictions.

$$
Precision=
\frac{TP}
{TP+FP}
$$


---

## Recall (Sensitivity)

The proportion of actual positives correctly identified.

$$
Recall=
\frac{TP}
{TP+FN}
$$


---

## F1-score

The harmonic mean of Precision and Recall.

$$
F1=
2
\frac{Precision \times Recall}
{Precision+Recall}
$$


Equivalent form:

$$
F1=
\frac{2TP}
{2TP+FP+FN}
$$


---

## Specificity

The proportion of actual negatives correctly identified.

$$
Specificity=
\frac{TN}
{TN+FP}
$$


---

## False Positive Rate (FPR)

The proportion of negative samples incorrectly classified as positive.

$$
FPR=
\frac{FP}
{FP+TN}
$$


---

## False Negative Rate (FNR)

The proportion of positive samples incorrectly classified as negative.

$$
FNR=
\frac{FN}
{FN+TP}
$$


---

## ROC Curve

ROC curve uses:

True Positive Rate:

$$
TPR=
\frac{TP}
{TP+FN}
$$


False Positive Rate:

$$
FPR=
\frac{FP}
{FP+TN}
$$


---

## AUC (Area Under Curve)

The area under the ROC curve.

$$
AUC=
\int_0^1 TPR(FPR)d(FPR)
$$


Probability interpretation:

$$
AUC=
P(score(x^+)>score(x^-))
$$


---

# 2. Regression Metrics

Assume:

True value:

$$
y_i
$$


Predicted value:

$$
\hat{y}_i
$$


Number of samples:

$$
N
$$


---

## Mean Absolute Error (MAE)

Average absolute prediction error.

$$
MAE=
\frac{1}{N}
\sum_{i=1}^{N}
|y_i-\hat{y}_i|
$$


---

## Mean Squared Error (MSE)

Average squared prediction error.

$$
MSE=
\frac{1}{N}
\sum_{i=1}^{N}
(y_i-\hat{y}_i)^2
$$


---

## Root Mean Squared Error (RMSE)

Square root of MSE.

$$
RMSE=
\sqrt{
\frac{1}{N}
\sum_{i=1}^{N}
(y_i-\hat{y}_i)^2
}
$$


---

## R² Score (Coefficient of Determination)

Measures how much variance is explained by the model.

$$
R^2=
1-
\frac{
\sum_{i=1}^{N}(y_i-\hat{y}_i)^2
}
{
\sum_{i=1}^{N}(y_i-\bar{y})^2
}
$$


where:

$$
\bar{y}
=
\frac{1}{N}
\sum_{i=1}^{N}y_i
$$


Interpretation:

- \(R^2=1\): Perfect prediction
- \(R^2=0\): Same as predicting the mean
- \(R^2<0\): Worse than mean prediction


---

## Mean Absolute Percentage Error (MAPE)

Percentage-based prediction error.

$$
MAPE=
\frac{100\%}{N}
\sum_{i=1}^{N}
\left|
\frac{y_i-\hat{y}_i}{y_i}
\right|
$$


---

# Summary Table

| Task | Metric | Formula |
|---|---|---|
| Classification | Accuracy | \(\frac{TP+TN}{TP+TN+FP+FN}\) |
| Classification | Precision | \(\frac{TP}{TP+FP}\) |
| Classification | Recall | \(\frac{TP}{TP+FN}\) |
| Classification | F1-score | \(\frac{2TP}{2TP+FP+FN}\) |
| Classification | AUC | \(\int TPR\,d(FPR)\) |
| Regression | MAE | \(\frac1N\sum|y-\hat y|\) |
| Regression | MSE | \(\frac1N\sum(y-\hat y)^2\) |
| Regression | RMSE | \(\sqrt{MSE}\) |
| Regression | R² | \(1-\frac{SS_{res}}{SS_{tot}}\) |