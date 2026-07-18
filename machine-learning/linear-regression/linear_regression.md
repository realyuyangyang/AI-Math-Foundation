# Linear Regression

## 1. Introduction

Linear Regression is a fundamental machine learning algorithm used to model the relationship between input variables and continuous output values.

The goal is to learn a linear function that minimizes the difference between predicted values and true values.

---

## 2. Mathematical Formulation

### Model

For a single feature:

\[
\hat{y}=wx+b
\]

For multiple features:

\[
\hat{y}=Xw+b
\]

where:

- \(X\): input feature matrix
- \(w\): weight parameters
- \(b\): bias term
- \(\hat{y}\): predicted output

---

## 3. Loss Function

Mean Squared Error (MSE) is commonly used:

\[
L(w,b)=\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2
\]

The objective is to minimize:

\[
\min_{w,b} L(w,b)
\]

---

## 4. Gradient Descent

The parameters are updated using gradients:

\[
w=w-\eta\frac{\partial L}{\partial w}
\]

\[
b=b-\eta\frac{\partial L}{\partial b}
\]

where:

- \(\eta\) is the learning rate
- \(\frac{\partial L}{\partial w}\) is the gradient of weights
- \(\frac{\partial L}{\partial b}\) is the gradient of bias

---

## 5. Implementation

This project implements Linear Regression from scratch using PyTorch autograd.

### Code

See:

