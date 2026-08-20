# Multilayer Perceptron (MLP)

## 1. Definition

A Multilayer Perceptron is a feedforward neural network composed of:

1. Input layer
2. One or more hidden layers
3. Output layer

Each neuron performs a linear transformation followed by a nonlinear activation function.

---

## 2. Linear Transformation

For layer \(l\), the linear transformation is:

$$
z^{(l)} = W^{(l)}a^{(l-1)} + b^{(l)}
$$

where:

- \(W^{(l)}\) is the weight matrix
- \(b^{(l)}\) is the bias vector
- \(a^{(l-1)}\) is the output of the previous layer
- \(z^{(l)}\) is the linear output

---

## 3. Activation Function

The hidden-layer output is:

$$
a^{(l)} = f\left(z^{(l)}\right)
$$

A common activation function is ReLU:

$$
f(z) = \max(0,z)
$$

ReLU introduces nonlinearity, allowing the MLP to learn complex relationships.

---

## 4. Forward Propagation

For an MLP with two hidden layers:

$$
z^{(1)} = W^{(1)}x + b^{(1)}
$$

$$
a^{(1)} = \operatorname{ReLU}\left(z^{(1)}\right)
$$

$$
z^{(2)} = W^{(2)}a^{(1)} + b^{(2)}
$$

$$
a^{(2)} = \operatorname{ReLU}\left(z^{(2)}\right)
$$

$$
z^{(3)} = W^{(3)}a^{(2)} + b^{(3)}
$$

The final output logits are:

$$
\hat{z} = z^{(3)}
$$

---

## 5. Softmax Function

For multi-class classification, Softmax converts logits into probabilities:

$$
P(y=k \mid x)
=
\frac{\exp(\hat{z}_k)}
{\sum_{j=1}^{K}\exp(\hat{z}_j)}
$$

The predicted class is:

$$
\hat{y}
=
\arg\max_k P(y=k \mid x)
$$

---

## 6. Cross-Entropy Loss

For one sample, the cross-entropy loss is:

$$
L
=
-\sum_{k=1}^{K} y_k \log(\hat{y}_k)
$$

For \(N\) samples:

$$
J
=
-\frac{1}{N}
\sum_{i=1}^{N}
\sum_{k=1}^{K}
y_{ik}\log(\hat{y}_{ik})
$$

---

## 7. Backpropagation

The gradient of the loss with respect to each parameter is computed using the chain rule:

$$
\frac{\partial L}{\partial W^{(l)}}
=
\frac{\partial L}{\partial z^{(l)}}
\frac{\partial z^{(l)}}{\partial W^{(l)}}
$$

The parameters are updated by gradient descent:

$$
W^{(l)}
\leftarrow
W^{(l)}
-
\eta
\frac{\partial L}{\partial W^{(l)}}
$$

$$
b^{(l)}
\leftarrow
b^{(l)}
-
\eta
\frac{\partial L}{\partial b^{(l)}}
$$

where \(\eta\) is the learning rate.

---

## 8. Model Structure

The example model uses:

$$
2
\rightarrow
16
\rightarrow
8
\rightarrow
2
$$

The network contains:

- 2 input features
- 16 neurons in the first hidden layer
- 8 neurons in the second hidden layer
- 2 output classes

---

## 9. Core Principle

An MLP repeatedly applies:

$$
\text{Linear Transformation}
+
\text{Nonlinear Activation}
$$

The complete mapping is:

$$
\hat{y}
=
f_{\theta}(x)
$$

where \(\theta\) represents all trainable weights and biases.
