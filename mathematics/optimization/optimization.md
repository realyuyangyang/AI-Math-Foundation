# Optimization

## 1. Objective Function

Optimization finds model parameters that minimize or maximize an objective function.

For machine learning, the usual goal is:

$$
\theta^* = \arg\min_{\theta} J(\theta)
$$

where:

- $\theta$ represents model parameters
- $J(\theta)$ is the loss or objective function
- $\theta^*$ is the optimal parameter value

---

## 2. Loss Function

For a dataset with $n$ samples, the empirical loss is:

$$
J(\theta) = \frac{1}{n}\sum_{i=1}^{n} L\left(f(x_i;\theta), y_i\right)
$$

where:

- $x_i$ is the input
- $y_i$ is the true output
- $f(x_i;\theta)$ is the model prediction
- $L$ is the loss function

---

## 3. Gradient

The gradient contains the partial derivatives of the objective function:

$$
\nabla_{\theta} J(\theta)
=
\begin{bmatrix}
\frac{\partial J}{\partial \theta_1} \\
\frac{\partial J}{\partial \theta_2} \\
\vdots \\
\frac{\partial J}{\partial \theta_d}
\end{bmatrix}
$$

The gradient points in the direction of the fastest increase.

Therefore, the negative gradient points in the direction of the fastest decrease.

---

## 4. Gradient Descent

Gradient descent updates parameters using:

$$
\theta_{t+1}
=
\theta_t
-
\eta \nabla_{\theta}J(\theta_t)
$$

where:

- $t$ is the iteration number
- $\eta$ is the learning rate
- $\nabla_{\theta}J(\theta_t)$ is the gradient

---

## 5. Learning Rate

The learning rate controls the update size:

$$
\Delta \theta
=
-\eta \nabla_{\theta}J(\theta)
$$

A small learning rate may cause slow convergence.

A large learning rate may cause oscillation or divergence.

---

## 6. Batch Gradient Descent

Batch gradient descent uses the entire training dataset:

$$
\nabla_{\theta}J(\theta)
=
\frac{1}{n}
\sum_{i=1}^{n}
\nabla_{\theta}
L\left(f(x_i;\theta),y_i\right)
$$

Parameter update:

$$
\theta_{t+1}
=
\theta_t
-
\eta
\frac{1}{n}
\sum_{i=1}^{n}
\nabla_{\theta}
L_i(\theta_t)
$$

---

## 7. Stochastic Gradient Descent

Stochastic Gradient Descent uses one training sample at each update:

$$
\theta_{t+1}
=
\theta_t
-
\eta
\nabla_{\theta}L_i(\theta_t)
$$

SGD is computationally efficient but produces noisy updates.

---

## 8. Mini-Batch Gradient Descent

Mini-batch gradient descent uses a subset of samples:

$$
J_B(\theta)
=
\frac{1}{|B|}
\sum_{i \in B}
L_i(\theta)
$$

The update rule is:

$$
\theta_{t+1}
=
\theta_t
-
\eta
\nabla_{\theta}J_B(\theta_t)
$$

Mini-batch gradient descent is commonly used in deep learning.

---

## 9. Momentum

Momentum accumulates previous gradients:

$$
v_t
=
\beta v_{t-1}
+
\nabla_{\theta}J(\theta_t)
$$

$$
\theta_{t+1}
=
\theta_t
-
\eta v_t
$$

where $\beta$ controls the contribution of previous gradients.

Momentum can accelerate convergence and reduce oscillation.

---

## 10. Nesterov Accelerated Gradient

Nesterov momentum calculates the gradient after looking ahead:

$$
v_t
=
\beta v_{t-1}
+
\nabla_{\theta}
J\left(\theta_t-\eta\beta v_{t-1}\right)
$$

$$
\theta_{t+1}
=
\theta_t
-
\eta v_t
$$

---

## 11. AdaGrad

AdaGrad adjusts the learning rate for each parameter:

$$
G_t
=
G_{t-1}
+
g_t^2
$$

$$
\theta_{t+1}
=
\theta_t
-
\frac{\eta}{\sqrt{G_t}+\epsilon}
g_t
$$

where:

$$
g_t = \nabla_{\theta}J(\theta_t)
$$

AdaGrad gives smaller updates to frequently updated parameters.

---

## 12. RMSProp

RMSProp uses an exponentially weighted average of squared gradients:

$$
s_t
=
\beta s_{t-1}
+
(1-\beta)g_t^2
$$

$$
\theta_{t+1}
=
\theta_t
-
\frac{\eta}{\sqrt{s_t}+\epsilon}
g_t
$$

RMSProp avoids the continuously decreasing learning rate of AdaGrad.

---

## 13. Adam

Adam combines momentum and adaptive learning rates.

First moment estimate:

$$
m_t
=
\beta_1 m_{t-1}
+
(1-\beta_1)g_t
$$

Second moment estimate:

$$
v_t
=
\beta_2 v_{t-1}
+
(1-\beta_2)g_t^2
$$

Bias correction:

$$
\hat{m}_t
=
\frac{m_t}{1-\beta_1^t}
$$

$$
\hat{v}_t
=
\frac{v_t}{1-\beta_2^t}
$$

Parameter update:

$$
\theta_{t+1}
=
\theta_t
-
\eta
\frac{\hat{m}_t}
{\sqrt{\hat{v}_t}+\epsilon}
$$

---

## 14. Weight Decay

Weight decay directly reduces parameter values:

$$
\theta_{t+1}
=
(1-\eta\lambda)\theta_t
-
\eta \nabla_{\theta}J(\theta_t)
$$

where $\lambda$ is the weight decay coefficient.

---

## 15. Regularized Objective

L2 regularization:

$$
J_{\text{reg}}(\theta)
=
J(\theta)
+
\lambda ||\theta||_2^2
$$

L1 regularization:

$$
J_{\text{reg}}(\theta)
=
J(\theta)
+
\lambda ||\theta||_1
$$

L2 regularization encourages smaller parameters.

L1 regularization encourages sparse parameters.

---

## 16. First-Order Optimality Condition

For a differentiable unconstrained objective, a stationary point satisfies:

$$
\nabla_{\theta}J(\theta^*) = 0
$$

This condition may correspond to:

- a local minimum
- a local maximum
- a saddle point

---

## 17. Hessian Matrix

The Hessian matrix contains second-order partial derivatives:

$$
H(\theta)
=
\nabla_{\theta}^2J(\theta)
$$

For two variables:

$$
H
=
\begin{bmatrix}
\frac{\partial^2J}{\partial\theta_1^2}
&
\frac{\partial^2J}{\partial\theta_1\partial\theta_2}
\\
\frac{\partial^2J}{\partial\theta_2\partial\theta_1}
&
\frac{\partial^2J}{\partial\theta_2^2}
\end{bmatrix}
$$

At a stationary point:

- positive definite Hessian: local minimum
- negative definite Hessian: local maximum
- indefinite Hessian: saddle point

---

## 18. Newton's Method

Newton's method uses first-order and second-order information:

$$
\theta_{t+1}
=
\theta_t
-
H(\theta_t)^{-1}
\nabla_{\theta}J(\theta_t)
$$

Newton's method can converge quickly but computing and inverting the Hessian is expensive.

---

## 19. Convex Function

A function is convex if:

$$
J(\lambda x + (1-\lambda)y)
\leq
\lambda J(x)
+
(1-\lambda)J(y)
$$

for:

$$
0 \leq \lambda \leq 1
$$

For a convex function, every local minimum is also a global minimum.

---

## 20. Strong Convexity

A differentiable function is strongly convex if:

$$
J(y)
\geq
J(x)
+
\nabla J(x)^T(y-x)
+
\frac{\mu}{2}||y-x||_2^2
$$

where $\mu > 0$ is the strong convexity constant.

Strong convexity usually provides faster convergence guarantees.

---

## 21. Constrained Optimization

A constrained optimization problem has the form:

$$
\min_{\theta} J(\theta)
$$

subject to:

$$
g_i(\theta) \leq 0
$$

and:

$$
h_j(\theta) = 0
$$

where $g_i$ represents inequality constraints and $h_j$ represents equality constraints.

---

## 22. Lagrange Multiplier

For an equality constraint:

$$
h(\theta)=0
$$

the Lagrangian is:

$$
\mathcal{L}(\theta,\lambda)
=
J(\theta)
+
\lambda h(\theta)
$$

The stationary conditions are:

$$
\nabla_{\theta}\mathcal{L}(\theta,\lambda)=0
$$

$$
h(\theta)=0
$$

---

## 23. Karush-Kuhn-Tucker Conditions

For inequality constraints:

$$
g_i(\theta)\leq 0
$$

the Lagrangian is:

$$
\mathcal{L}(\theta,\lambda)
=
J(\theta)
+
\sum_i \lambda_i g_i(\theta)
$$

The KKT conditions include:

$$
\nabla_{\theta}\mathcal{L}(\theta,\lambda)=0
$$

$$
g_i(\theta)\leq 0
$$

$$
\lambda_i \geq 0
$$

$$
\lambda_i g_i(\theta)=0
$$

---

## 24. Learning Rate Decay

Step decay:

$$
\eta_t
=
\eta_0 \gamma^{\lfloor t/s \rfloor}
$$

Exponential decay:

$$
\eta_t
=
\eta_0 e^{-kt}
$$

Inverse-time decay:

$$
\eta_t
=
\frac{\eta_0}{1+kt}
$$

Cosine decay:

$$
\eta_t
=
\eta_{\min}
+
\frac{1}{2}
(\eta_{\max}-\eta_{\min})
\left(
1+\cos\left(\frac{\pi t}{T}\right)
\right)
$$

---

## 25. Gradient Clipping

Gradient clipping prevents excessively large gradients.

Clipping by norm:

$$
g
\leftarrow
g
\cdot
\min\left(
1,
\frac{\tau}{||g||_2}
\right)
$$

where $\tau$ is the maximum gradient norm.

---

## 26. Common Optimization Problems

### Vanishing Gradient

$$
||\nabla_{\theta}J(\theta)|| \rightarrow 0
$$

The parameter updates become extremely small.

### Exploding Gradient

$$
||\nabla_{\theta}J(\theta)|| \rightarrow \infty
$$

The parameter updates become unstable.

### Local Minimum

The objective is smaller than nearby points but may not be globally optimal.

### Saddle Point

The gradient is zero, but the point is neither a local minimum nor a local maximum.

---

## 27. Common Optimizers

| Optimizer | Main Idea | Typical Characteristic |
|---|---|---|
| Gradient Descent | Full-dataset gradient | Stable but expensive |
| SGD | One-sample gradient | Fast but noisy |
| Mini-Batch SGD | Small-batch gradient | Standard deep learning method |
| Momentum | Accumulated direction | Reduces oscillation |
| AdaGrad | Parameter-wise learning rate | Useful for sparse gradients |
| RMSProp | Moving average of squared gradients | Stable adaptive updates |
| Adam | Momentum and adaptive learning rate | Widely used default optimizer |

---

## 28. Core Optimization Process

The standard optimization process is:

$$
\text{Initialize parameters}
\rightarrow
\text{Forward propagation}
\rightarrow
\text{Compute loss}
\rightarrow
\text{Backpropagation}
\rightarrow
\text{Update parameters}
\rightarrow
\text{Repeat}
$$

The final goal is:

$$
\theta_t \rightarrow \theta^*
$$
