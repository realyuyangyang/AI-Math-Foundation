# Logistic Regression Mathematics


## 1. Linear Model


The linear model:


$$
z=W^Tx+b
$$


The dot product:


$$
W^Tx=\sum_{i=1}^{d}w_ix_i
$$


For batch data:


$$
Z=XW+b
$$



## 2. Sigmoid Function


$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$



## 3. Prediction


Probability prediction:


$$
\hat{y}=\sigma(W^Tx+b)
$$


Expanded form:


$$
\hat{y}
=
\frac{1}{1+e^{-(W^Tx+b)}}
$$



Classification:


$$
\hat{y}=1,\quad \hat{y}\geq0.5
$$


$$
\hat{y}=0,\quad \hat{y}<0.5
$$