# Logistic Regression Mathematics


## 1. Linear Model


\[
z=w^Tx+b
\]


where:


\[
w^Tx
=
\sum_{i=1}^{n}w_ix_i
\]


For a batch of samples:


\[
Z=XW+b
\]


---

## 2. Sigmoid Function


\[
\sigma(z)=\frac{1}{1+e^{-z}}
\]


Prediction:


\[
\hat{y}=\sigma(w^Tx+b)
\]


or:


\[
\hat{y}
=
\frac{1}{1+e^{-(w^Tx+b)}}
\]


---

## 3. Probability Model


\[
P(y=1|x)=\hat{y}
\]


\[
P(y=0|x)=1-\hat{y}
\]


---

## 4. Decision Boundary


\[
\hat{y}=0.5
\]


Equivalent condition:


\[
w^Tx+b=0
\]


---

## 5. Binary Cross Entropy Loss


\[
L
=
-\frac{1}{N}
\sum_{i=1}^{N}
[
y_i\log(\hat{y_i})
+
(1-y_i)\log(1-\hat{y_i})
]
\]


---

## 6. Gradient


Weight gradient:


\[
\frac{\partial L}{\partial w}
=
\frac{1}{N}X^T(\hat{y}-y)
\]


Bias gradient:


\[
\frac{\partial L}{\partial b}
=
\frac{1}{N}
\sum_{i=1}^{N}
(\hat{y_i}-y_i)
\]


---

## 7. Gradient Descent Update


Weight update:


\[
w=w-\eta\frac{\partial L}{\partial w}
\]


Bias update:


\[
b=b-\eta\frac{\partial L}{\partial b}
\]


---

## 8. Complete Optimization Objective


\[
\min_{w,b}
-
\frac{1}{N}
\sum_{i=1}^{N}
[
y_i\log(\hat{y_i})
+
(1-y_i)\log(1-\hat{y_i})
]
\]


where:


\[
\hat{y_i}
=
\frac{1}{1+e^{-(w^Tx_i+b)}}
\]