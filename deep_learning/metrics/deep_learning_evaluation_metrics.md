# Deep Learning Evaluation Metrics

## 1. Classification Metrics

Deep learning classification models (CNN, RNN, Transformer) usually use the following evaluation metrics.

Assume:

- True label: \(y_i\)
- Predicted label: \(\hat{y}_i\)
- Number of samples: \(N\)


## Confusion Matrix

| | Predicted Positive | Predicted Negative |
|---|---|---|
| Actual Positive | TP | FN |
| Actual Negative | FP | TN |


---

## Accuracy

The ratio of correctly classified samples.

$$
Accuracy=
\frac{TP+TN}
{TP+TN+FP+FN}
$$


---

## Precision

The proportion of true positive samples among all predicted positive samples.

$$
Precision=
\frac{TP}
{TP+FP}
$$


---

## Recall

The proportion of actual positive samples correctly detected.

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


Equivalent:

$$
F1=
\frac{2TP}
{2TP+FP+FN}
$$


---

## AUC (Area Under ROC Curve)

True Positive Rate:

$$
TPR=
\frac{TP}{TP+FN}
$$


False Positive Rate:

$$
FPR=
\frac{FP}{FP+TN}
$$


AUC:

$$
AUC=
\int_0^1 TPR(FPR)d(FPR)
$$


---

# 2. Loss Functions

Deep learning models are trained by minimizing loss functions.

---

## Binary Cross Entropy Loss

Used for binary classification.

$$
L=
-\frac1N
\sum_{i=1}^{N}
[
y_i\log(\hat{y}_i)
+
(1-y_i)\log(1-\hat{y}_i)
]
$$


---

## Categorical Cross Entropy Loss

Used for multi-class classification.

$$
L=
-\frac1N
\sum_{i=1}^{N}
\sum_{c=1}^{C}
y_{ic}
\log(\hat{y}_{ic})
$$


where:

- \(C\): number of classes
- \(y_{ic}\): true label
- \(\hat{y}_{ic}\): predicted probability


---

## Perplexity (PPL)

Used in language models (RNN, Transformer, LLM).

$$
PPL=e^L
$$


where:

$$
L=
-\frac1N
\sum_{i=1}^{N}
\log P(x_i)
$$


Lower PPL indicates better language modeling ability.

---

# 3. Regression Metrics

Used for deep learning regression models.

---

## Mean Absolute Error (MAE)

$$
MAE=
\frac1N
\sum_{i=1}^{N}
|y_i-\hat{y}_i|
$$


---

## Mean Squared Error (MSE)

$$
MSE=
\frac1N
\sum_{i=1}^{N}
(y_i-\hat{y}_i)^2
$$


---

## Root Mean Squared Error (RMSE)

$$
RMSE=
\sqrt{
\frac1N
\sum_{i=1}^{N}
(y_i-\hat{y}_i)^2
}
$$


---

## R² Score

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
\frac1N
\sum_{i=1}^{N}y_i
$$


---

# 4. Computer Vision Metrics

## Intersection over Union (IoU)

Used for image segmentation and object detection.

$$
IoU=
\frac{|A\cap B|}
{|A\cup B|}
$$


where:

- \(A\): predicted region
- \(B\): ground truth region


---

## Dice Coefficient

Used for medical image segmentation.

$$
Dice=
\frac{2|A\cap B|}
{|A|+|B|}
$$


Relationship:

$$
Dice=
\frac{2IoU}{1+IoU}
$$


---

## Mean Average Precision (mAP)

Used for object detection.

$$
mAP=
\frac1C
\sum_{c=1}^{C}AP_c
$$


Average Precision:

$$
AP=
\int_0^1 Precision(Recall)dRecall
$$


---

# 5. Generative Model Metrics

## Fréchet Inception Distance (FID)

Used for GAN and image generation evaluation.

$$
FID=
||\mu_r-\mu_g||^2
+
Tr(
\Sigma_r+\Sigma_g
-2(\Sigma_r\Sigma_g)^{1/2}
)
$$


where:

- \(\mu_r,\Sigma_r\): real data distribution
- \(\mu_g,\Sigma_g\): generated data distribution


Lower FID indicates better generated image quality.

---

## Inception Score (IS)

Measures image quality and diversity.

$$
IS=
exp
(
E_x
D_{KL}
(p(y|x)||p(y))
)
$$


---

# 6. Large Language Model (LLM) Metrics

## Exact Match (EM)

Prediction exactly matches the reference answer.

$$
EM=
\frac{
Number\ of\ Correct\ Answers
}
{
Total\ Answers
}
$$


---

## BLEU Score

Used for machine translation.

$$
BLEU=
BP
\cdot
exp
(
\sum_{n=1}^{N}
w_n\log p_n
)
$$


where:

- \(p_n\): n-gram precision
- \(BP\): brevity penalty


---

## ROUGE Score

Used for text summarization.

$$
ROUGE=
\frac{
Overlapping\ Tokens
}
{
Reference\ Tokens
}
$$


---

## Pass@k

Used for code generation evaluation.

$$
Pass@k=
1-
\frac{
\binom{n-c}{k}
}
{
\binom nk
}
$$


where:

- \(n\): total generated samples
- \(c\): correct samples


---

# Summary Table

| Task | Metric | Formula |
|---|---|---|
| Classification | Accuracy | \(\frac{TP+TN}{TP+TN+FP+FN}\) |
| Classification | Precision | \(\frac{TP}{TP+FP}\) |
| Classification | Recall | \(\frac{TP}{TP+FN}\) |
| Classification | F1 | \(\frac{2TP}{2TP+FP+FN}\) |
| Classification | Cross Entropy | \(-\sum y\log\hat y\) |
| Language Model | Perplexity | \(e^L\) |
| Regression | MAE | \(\frac1N\sum|y-\hat y|\) |
| Regression | MSE | \(\frac1N\sum(y-\hat y)^2\) |
| Segmentation | IoU | \(\frac{|A\cap B|}{|A\cup B|}\) |
| Segmentation | Dice | \(\frac{2|A\cap B|}{|A|+|B|}\) |
| Detection | mAP | \(\frac1C\sum AP_c\) |
| Generation | FID | Distribution distance |
| LLM | BLEU / ROUGE | Text similarity |
| LLM | Pass@k | Code correctness probability |