# Recurrent Neural Network (RNN)

## 1. Basic Idea

RNN is a neural network designed for sequential data.

Examples:

- Text
- Time series
- Speech
- Biological sequences


The key idea:

The current hidden state contains information from previous steps.


---

# 2. RNN Structure


For input sequence:

$$
x_1,x_2,...,x_T
$$


Hidden state:

$$
h_1,h_2,...,h_T
$$


At time step $t$:


$$
h_t=f(W_xx_t+W_hh_{t-1}+b)
$$


where:


- $x_t$ : current input
- $h_{t-1}$ : previous hidden state
- $h_t$ : current hidden state


---

# 3. Activation Function


Usually:


$$
h_t=tanh(W_xx_t+W_hh_{t-1}+b)
$$


The hidden state is updated recursively.


---

# 4. Output Layer


Prediction:


$$
y_t=W_yh_t+b_y
$$


where:

- $W_y$ is output weight
- $b_y$ is bias


---

# 5. Unrolling RNN


A sequence is expanded:


$$
x_1 \rightarrow h_1
$$


$$
x_2+h_1 \rightarrow h_2
$$


$$
x_3+h_2 \rightarrow h_3
$$


The same parameters are shared across all time steps.


---

# 6. Loss Function


For regression:


$$
L=
\frac{1}{N}
\sum_{i=1}^{N}
(y_i-\hat y_i)^2
$$


Mean Squared Error (MSE):

$$
MSE=
\frac{1}{N}
\sum(y-\hat y)^2
$$


---

# 7. Backpropagation Through Time (BPTT)


RNN uses:

$$
\frac{\partial L}{\partial W}
$$


through all time steps.


The gradient is accumulated:


$$
\frac{\partial L}{\partial W}
=
\sum_{t=1}^{T}
\frac{\partial L_t}{\partial W}
$$


---

# 8. Gradient Problems


Because of repeated multiplication:


$$
\frac{\partial h_t}{\partial h_{t-1}}
$$


gradients may become:


## Vanishing Gradient


$$
|\frac{\partial L}{\partial W}| \rightarrow 0
$$


## Exploding Gradient


$$
|\frac{\partial L}{\partial W}| \rightarrow \infty
$$


Solutions:

- LSTM
- GRU
- Gradient clipping


---

# 9. RNN vs Transformer


| RNN | Transformer |
|-|-|
| Sequential processing | Parallel processing |
| Hidden state memory | Attention memory |
| Slow for long sequences | Efficient for long sequences |
| Vanishing gradient problem | Better long-range dependency |


---

# 10. Core Formula Summary


Hidden state:

$$
h_t=tanh(W_xx_t+W_hh_{t-1}+b)
$$


Output:

$$
y_t=W_yh_t+b_y
$$


Loss:

$$
L=
\frac{1}{N}
\sum(y-\hat y)^2
$$


Gradient:

$$
\frac{\partial L}{\partial W}
$$