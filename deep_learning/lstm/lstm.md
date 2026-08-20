# Long Short-Term Memory

## 1. Overview

Long Short-Term Memory, or LSTM, is a recurrent neural network architecture designed to learn long-term dependencies in sequential data.

An LSTM uses a cell state and three gates:

- Forget gate
- Input gate
- Output gate

---

## 2. Input

At time step \(t\):

$$
x_t = \text{current input}
$$

$$
h_{t-1} = \text{previous hidden state}
$$

$$
c_{t-1} = \text{previous cell state}
$$

---

## 3. Forget Gate

The forget gate determines which information should be removed from the previous cell state.

$$
f_t = \sigma(W_f x_t + U_f h_{t-1} + b_f)
$$

---

## 4. Input Gate

The input gate determines which new information should be stored.

$$
i_t = \sigma(W_i x_t + U_i h_{t-1} + b_i)
$$

The candidate cell state is:

$$
\tilde{c}_t = \tanh(W_c x_t + U_c h_{t-1} + b_c)
$$

---

## 5. Cell State Update

The new cell state combines retained old information and new candidate information.

$$
c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t
$$

---

## 6. Output Gate

The output gate determines which part of the cell state becomes the hidden state.

$$
o_t = \sigma(W_o x_t + U_o h_{t-1} + b_o)
$$

$$
h_t = o_t \odot \tanh(c_t)
$$

---

## 7. Activation Functions

Sigmoid function:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

Hyperbolic tangent:

$$
\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
$$

---

## 8. Classification Output

For binary classification:

$$
z = W_y h_T + b_y
$$

$$
\hat{y} = \sigma(z)
$$

---

## 9. Binary Cross-Entropy Loss

$$
L = -\frac{1}{N}
\sum_{i=1}^{N}
\left[
y_i \log(\hat{y}_i)
+
(1-y_i)\log(1-\hat{y}_i)
\right]
$$

---

## 10. Core Idea

The cell state provides a path for information to flow through many time steps.

The gates control:

$$
\text{Forget old information}
$$

$$
\text{Store new information}
$$

$$
\text{Produce the hidden state}
$$
