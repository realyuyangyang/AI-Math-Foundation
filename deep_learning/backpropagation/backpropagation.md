# Backpropagation

## 1. Overview

Backpropagation is the algorithm used to calculate gradients in neural networks.

The training process is:

$$
\text{Forward Pass}
\rightarrow
\text{Loss}
\rightarrow
\text{Backward Pass}
\rightarrow
\text{Parameter Update}
$$

---

## 2. Forward Propagation

For a two-layer neural network:

$$
z_1 = XW_1 + b_1
$$

$$
a_1 = f(z_1)
$$

$$
z_2 = a_1W_2 + b_2
$$

$$
\hat{y} = \sigma(z_2)
$$

where:

* $X$ is the input
* $W_1$ and $W_2$ are weight matrices
* $b_1$ and $b_2$ are bias vectors
* $f$ is the hidden-layer activation function
* $\sigma$ is the sigmoid function
* $\hat{y}$ is the prediction

---

## 3. Loss Function

For binary classification, the binary cross-entropy loss is:

$$
L =
-\frac{1}{m}
\sum_{i=1}^{m}
\left[
y_i\log(\hat{y}_i)
+
(1-y_i)\log(1-\hat{y}_i)
\right]
$$

The objective is to minimize:

$$
\min_{\theta} L
$$

where $\theta$ represents all model parameters.

---

## 4. Chain Rule

Backpropagation is based on the chain rule.

If:

$$
L = L(a)
$$

$$
a = f(z)
$$

$$
z = wx+b
$$

then:

$$
\frac{\partial L}{\partial w}
=============================

\frac{\partial L}{\partial a}
\frac{\partial a}{\partial z}
\frac{\partial z}{\partial w}
$$

The gradient is propagated from the output layer toward the input layer.

---

## 5. Output Layer Gradients

For sigmoid output and binary cross-entropy loss:

$$
\delta_2
========

# \frac{\partial L}{\partial z_2}

\hat{y}-y
$$

The output-layer weight gradient is:

$$
\frac{\partial L}{\partial W_2}
===============================

\frac{1}{m}a_1^T\delta_2
$$

The output-layer bias gradient is:

$$
\frac{\partial L}{\partial b_2}
===============================

\frac{1}{m}
\sum_{i=1}^{m}\delta_2^{(i)}
$$

---

## 6. Hidden Layer Gradients

The error propagated to the hidden layer is:

$$
\delta_1
========

(\delta_2W_2^T)
\odot
f'(z_1)
$$

where $\odot$ represents element-wise multiplication.

The hidden-layer weight gradient is:

$$
\frac{\partial L}{\partial W_1}
===============================

\frac{1}{m}X^T\delta_1
$$

The hidden-layer bias gradient is:

$$
\frac{\partial L}{\partial b_1}
===============================

\frac{1}{m}
\sum_{i=1}^{m}\delta_1^{(i)}
$$

---

## 7. Sigmoid Derivative

The sigmoid function is:

$$
\sigma(z)
=========

\frac{1}{1+e^{-z}}
$$

Its derivative is:

$$
\sigma'(z)
==========

\sigma(z)(1-\sigma(z))
$$

---

## 8. Parameter Update

Gradient descent updates the parameters as follows:

$$
W_1
\leftarrow
W_1
---

\eta
\frac{\partial L}{\partial W_1}
$$

$$
b_1
\leftarrow
b_1
---

\eta
\frac{\partial L}{\partial b_1}
$$

$$
W_2
\leftarrow
W_2
---

\eta
\frac{\partial L}{\partial W_2}
$$

$$
b_2
\leftarrow
b_2
---

\eta
\frac{\partial L}{\partial b_2}
$$

where $\eta$ is the learning rate.

---

## 9. Algorithm

1. Initialize weights and biases.
2. Perform forward propagation.
3. Compute the loss.
4. Calculate output-layer gradients.
5. Propagate the error to the hidden layer.
6. Calculate hidden-layer gradients.
7. Update all parameters.
8. Repeat until the loss converges.

---

## 10. Gradient Checking

A numerical gradient can be approximated by:

$$
\frac{\partial L}{\partial \theta}
\approx
\frac{
L(\theta+\epsilon)
------------------

L(\theta-\epsilon)
}{
2\epsilon
}
$$

The numerical gradient should be close to the backpropagation gradient.

---

## 11. Summary

Backpropagation combines the chain rule with gradient descent:

$$
\text{Backpropagation}
======================

\text{Chain Rule}
+
\text{Gradient Calculation}
$$

The complete learning process is:

$$
\text{Forward}
\rightarrow
\text{Loss}
\rightarrow
\text{Backward}
\rightarrow
\text{Update}
$$

Backpropagation is the foundation of training neural networks, including CNNs, RNNs, Transformers, and diffusion models.


