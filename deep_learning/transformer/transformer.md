# Transformer

## 1. Overview

Transformer processes a sequence through the following main steps:

1. Token Embedding
2. Positional Encoding
3. Query, Key, and Value projection
4. Scaled Dot-Product Attention
5. Multi-Head Attention
6. Residual Connection and Layer Normalization
7. Feed-Forward Network
8. Encoder and Decoder stacking
9. Linear projection and Softmax
10. Autoregressive prediction

---

## 2. Input Sequence

Given a sequence of tokens:

$$
x_1, x_2, \ldots, x_n
$$

Each token is converted into an integer token ID:

$$
t_i \in {1,2,\ldots,V}
$$

where:

* $n$ is the sequence length
* $V$ is the vocabulary size

---

## 3. Token Embedding

Each token ID is mapped to a dense vector through an embedding matrix:

$$
E \in \mathbb{R}^{V \times d_{\text{model}}}
$$

The embedding of token $t_i$ is:

$$
e_i = E[t_i]
$$

For the complete sequence:

$$
X =
\begin{bmatrix}
e_1 \
e_2 \
\vdots \
e_n
\end{bmatrix}
\in \mathbb{R}^{n \times d_{\text{model}}}
$$

where $d_{\text{model}}$ is the hidden dimension of the Transformer.

---

## 4. Positional Encoding

Self-attention does not directly contain token-order information.

Therefore, positional information is added to the token embeddings:

$$
H^{(0)} = X + P
$$

where $P$ is the positional encoding matrix.

For sinusoidal positional encoding:

$$
PE(pos, 2i)
===========

\sin
\left(
\frac{pos}{10000^{2i/d_{\text{model}}}}
\right)
$$

$$
PE(pos, 2i+1)
=============

\cos
\left(
\frac{pos}{10000^{2i/d_{\text{model}}}}
\right)
$$

where:

* $pos$ is the token position
* $i$ is the dimension index

---

## 5. Query, Key, and Value

The input representation is projected into three matrices:

$$
Q = HW_Q
$$

$$
K = HW_K
$$

$$
V = HW_V
$$

where:

$$
W_Q \in \mathbb{R}^{d_{\text{model}} \times d_k}
$$

$$
W_K \in \mathbb{R}^{d_{\text{model}} \times d_k}
$$

$$
W_V \in \mathbb{R}^{d_{\text{model}} \times d_v}
$$

The meanings are:

* Query: what the current token is looking for
* Key: what information each token contains
* Value: the actual information passed to the output

---

## 6. Attention Score

The similarity between each query and every key is computed using a dot product:

$$
S = QK^T
$$

For token $i$ attending to token $j$:

$$
s_{ij} = q_i k_j^T
$$

A larger score means token $i$ should pay more attention to token $j$.

---

## 7. Scaled Dot-Product Attention

The attention scores are divided by $\sqrt{d_k}$:

$$
S_{\text{scaled}}
=================

\frac{QK^T}{\sqrt{d_k}}
$$

The scaling prevents the dot products from becoming too large when $d_k$ is large.

The attention weights are then calculated using Softmax:

$$
A
=

\operatorname{softmax}
\left(
\frac{QK^T}{\sqrt{d_k}}
\right)
$$

The final attention output is:

$$
Z = AV
$$

Therefore:

$$
\operatorname{Attention}(Q,K,V)
===============================

\operatorname{softmax}
\left(
\frac{QK^T}{\sqrt{d_k}}
\right)V
$$

---

## 8. Softmax

For a vector of scores:

$$
z_1,z_2,\ldots,z_n
$$

Softmax is defined as:

$$
\operatorname{softmax}(z_i)
===========================

\frac{e^{z_i}}
{\sum_{j=1}^{n}e^{z_j}}
$$

The resulting attention weights satisfy:

$$
\sum_{j=1}^{n}A_{ij}=1
$$

---

## 9. Causal Mask

In autoregressive language models, a token must not see future tokens.

The masked attention score is:

$$
S_{\text{masked}}
=================

\frac{QK^T}{\sqrt{d_k}} + M
$$

The mask matrix is:

$$
M_{ij}
======

\begin{cases}
0, & j \le i \
-\infty, & j > i
\end{cases}
$$

The masked attention is:

$$
\operatorname{MaskedAttention}(Q,K,V)
=====================================

\operatorname{softmax}
\left(
\frac{QK^T}{\sqrt{d_k}} + M
\right)V
$$

The mask matrix has the following form:

$$
M =
\begin{bmatrix}
0 & -\infty & -\infty & -\infty \
0 & 0 & -\infty & -\infty \
0 & 0 & 0 & -\infty \
0 & 0 & 0 & 0
\end{bmatrix}
$$

---

## 10. Multi-Head Attention

Instead of using one attention operation, Transformer uses multiple attention heads.

For head $i$:

$$
Q_i = HW_i^Q
$$

$$
K_i = HW_i^K
$$

$$
V_i = HW_i^V
$$

Each attention head is:

$$
\operatorname{head}_i
=====================

\operatorname{Attention}(Q_i,K_i,V_i)
$$

The outputs of all heads are concatenated:

$$
H_{\text{concat}}
=================

\operatorname{Concat}
\left(
\operatorname{head}_1,
\operatorname{head}_2,
\ldots,
\operatorname{head}_h
\right)
$$

The concatenated result is projected back to the model dimension:

$$
\operatorname{MultiHead}(H)
===========================

H_{\text{concat}}W_O
$$

The complete formula is:

$$
\operatorname{MultiHead}(Q,K,V)
===============================

\operatorname{Concat}
\left(
\operatorname{head}_1,
\ldots,
\operatorname{head}_h
\right)W_O
$$

where:

$$
\operatorname{head}_i
=====================

\operatorname{Attention}
\left(
QW_i^Q,
KW_i^K,
VW_i^V
\right)
$$

---

## 11. Residual Connection

The input of a sublayer is added to its output:

$$
Y = X + \operatorname{Sublayer}(X)
$$

For the attention sublayer:

$$
Y = X + \operatorname{MultiHeadAttention}(X)
$$

Residual connections help preserve the original information and improve gradient flow.

---

## 12. Layer Normalization

For a hidden vector:

$$
x =
\begin{bmatrix}
x_1,x_2,\ldots,x_d
\end{bmatrix}
$$

The mean is:

$$
\mu
===

\frac{1}{d}
\sum_{i=1}^{d}x_i
$$

The variance is:

$$
\sigma^2
========

\frac{1}{d}
\sum_{i=1}^{d}
(x_i-\mu)^2
$$

Layer normalization is:

$$
\operatorname{LayerNorm}(x)
===========================

\gamma
\frac{x-\mu}
{\sqrt{\sigma^2+\epsilon}}
+
\beta
$$

where $\gamma$ and $\beta$ are learnable parameters.

A Transformer sublayer can be written as:

$$
Y
=

\operatorname{LayerNorm}
\left(
X+\operatorname{Sublayer}(X)
\right)
$$

---

## 13. Feed-Forward Network

Each token independently passes through a two-layer neural network:

$$
\operatorname{FFN}(x)
=====================

\operatorname{ReLU}(xW_1+b_1)W_2+b_2
$$

The dimensions are usually:

$$
W_1
\in
\mathbb{R}^{d_{\text{model}} \times d_{\text{ff}}}
$$

$$
W_2
\in
\mathbb{R}^{d_{\text{ff}} \times d_{\text{model}}}
$$

Normally:

$$
d_{\text{ff}} > d_{\text{model}}
$$

Modern Transformers may use GELU instead of ReLU:

$$
\operatorname{FFN}(x)
=====================

\operatorname{GELU}(xW_1+b_1)W_2+b_2
$$

---

## 14. Encoder Layer

One encoder layer contains:

1. Multi-Head Self-Attention
2. Residual Connection
3. Layer Normalization
4. Feed-Forward Network
5. Residual Connection
6. Layer Normalization

The attention output is:

$$
H'
==

\operatorname{LayerNorm}
\left(
H+
\operatorname{MultiHeadAttention}(H,H,H)
\right)
$$

The feed-forward output is:

$$
H_{\text{out}}
==============

\operatorname{LayerNorm}
\left(
H'
+
\operatorname{FFN}(H')
\right)
$$

Multiple encoder layers are stacked:

$$
H^{(l)}
=======

\operatorname{EncoderLayer}
\left(
H^{(l-1)}
\right)
$$

where:

$$
l=1,2,\ldots,L
$$

---

## 15. Decoder Layer

A decoder layer contains:

1. Masked Multi-Head Self-Attention
2. Encoder-Decoder Cross-Attention
3. Feed-Forward Network

### 15.1 Masked Self-Attention

$$
D'
==

\operatorname{LayerNorm}
\left(
D+
\operatorname{MaskedMultiHeadAttention}(D,D,D)
\right)
$$

### 15.2 Cross-Attention

In cross-attention:

* Query comes from the decoder
* Key comes from the encoder
* Value comes from the encoder

Therefore:

$$
Q = D'W_Q
$$

$$
K = H_{\text{encoder}}W_K
$$

$$
V = H_{\text{encoder}}W_V
$$

The cross-attention output is:

$$
D''
===

\operatorname{LayerNorm}
\left(
D'
+
\operatorname{MultiHeadAttention}
\left(
D',
H_{\text{encoder}},
H_{\text{encoder}}
\right)
\right)
$$

### 15.3 Feed-Forward Network

$$
D_{\text{out}}
==============

\operatorname{LayerNorm}
\left(
D''
+
\operatorname{FFN}(D'')
\right)
$$

---

## 16. Output Projection

The final hidden representation is projected to vocabulary logits:

$$
Z = HW_{\text{vocab}} + b_{\text{vocab}}
$$

where:

$$
W_{\text{vocab}}
\in
\mathbb{R}^{d_{\text{model}} \times V}
$$

For token position $t$:

$$
z_t
\in
\mathbb{R}^{V}
$$

Each value in $z_t$ is the score of one vocabulary token.

---

## 17. Output Probability

Softmax converts logits into token probabilities:

$$
P(y_t=j)
========

\frac{\exp(z_{t,j})}
{\sum_{k=1}^{V}\exp(z_{t,k})}
$$

The predicted token is:

$$
\hat{y}_t
=========

\arg\max_j P(y_t=j)
$$

---

## 18. Autoregressive Factorization

A language model predicts a sequence one token at a time:

$$
P(x_1,x_2,\ldots,x_T)
=====================

\prod_{t=1}^{T}
P(x_t \mid x_1,x_2,\ldots,x_{t-1})
$$

At step $t$, the model predicts:

$$
P(x_t \mid x_{<t})
$$

where:

$$
x_{<t}
======

x_1,x_2,\ldots,x_{t-1}
$$

---

## 19. Training Target Shift

The input sequence may be:

$$
x_1,x_2,x_3,\ldots,x_{T-1}
$$

The target sequence is shifted by one token:

$$
x_2,x_3,x_4,\ldots,x_T
$$

For example:

```text
Input:  I like deep
Target: like deep learning
```

The model learns to predict the next token at every position.

---

## 20. Cross-Entropy Loss

For one token, the cross-entropy loss is:

$$
L_t
===

-\log P(x_t \mid x_{<t})
$$

For the complete sequence:

$$
L
=

-\sum_{t=1}^{T}
\log P(x_t \mid x_{<t})
$$

The average loss is:

$$
L
=

-\frac{1}{T}
\sum_{t=1}^{T}
\log P(x_t \mid x_{<t})
$$

The model parameters are updated to minimize this loss:

$$
\theta
\leftarrow
\theta
------

\eta
\nabla_{\theta}L
$$

where:

* $\theta$ represents all model parameters
* $\eta$ is the learning rate

---

## 21. Complete Transformer Process

The complete process can be summarized as:

### Step 1: Token Embedding

$$
X = \operatorname{Embedding}(\text{tokens})
$$

### Step 2: Add Positional Encoding

$$
H^{(0)} = X + P
$$

### Step 3: Calculate Query, Key, and Value

$$
Q = HW_Q
$$

$$
K = HW_K
$$

$$
V = HW_V
$$

### Step 4: Calculate Attention Scores

$$
S = \frac{QK^T}{\sqrt{d_k}}
$$

### Step 5: Apply Mask

$$
S_{\text{masked}} = S + M
$$

### Step 6: Calculate Attention Weights

$$
A = \operatorname{softmax}(S_{\text{masked}})
$$

### Step 7: Weighted Sum of Values

$$
Z = AV
$$

### Step 8: Multi-Head Attention

$$
H_{\text{attention}}
====================

\operatorname{Concat}
\left(
\operatorname{head}_1,
\ldots,
\operatorname{head}_h
\right)W_O
$$

### Step 9: Residual Connection and Layer Normalization

$$
H'
==

\operatorname{LayerNorm}
\left(
H+H_{\text{attention}}
\right)
$$

### Step 10: Feed-Forward Network

$$
F
=

\operatorname{FFN}(H')
$$

### Step 11: Second Residual Connection

$$
H_{\text{out}}
==============

\operatorname{LayerNorm}
\left(
H'+F
\right)
$$

### Step 12: Output Logits

$$
Z = H_{\text{out}}W_{\text{vocab}}+b
$$

### Step 13: Output Probabilities

$$
P
=

\operatorname{softmax}(Z)
$$

### Step 14: Predict the Next Token

$$
\hat{x}_{t+1}
=============

\arg\max_j P(x_{t+1}=j \mid x_{\le t})
$$

---

## 22. Core Transformer Formula

The central formula of Transformer is:

$$
\boxed{
\operatorname{Attention}(Q,K,V)
===============================

\operatorname{softmax}
\left(
\frac{QK^T}{\sqrt{d_k}}
\right)V
}
$$

For autoregressive models with a causal mask:

$$
\boxed{
\operatorname{MaskedAttention}(Q,K,V)
=====================================

\operatorname{softmax}
\left(
\frac{QK^T}{\sqrt{d_k}}+M
\right)V
}
$$

The complete Transformer block is:

$$
H'
==

\operatorname{LayerNorm}
\left(
H+
\operatorname{MultiHeadAttention}(H)
\right)
$$

$$
H_{\text{out}}
==============

\operatorname{LayerNorm}
\left(
H'
+
\operatorname{FFN}(H')
\right)
$$
