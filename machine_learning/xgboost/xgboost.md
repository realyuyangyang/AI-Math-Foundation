# XGBoost (Extreme Gradient Boosting)

## 1. Model Definition

XGBoost is an ensemble learning algorithm based on gradient boosted decision trees.

The prediction is the sum of multiple decision trees:

$$
\hat{y}^{(t)}
=
\sum_{k=1}^{t} f_k(x)
$$

where:

- $f_k(x)$ is the $k$-th decision tree
- $t$ is the number of trees


Adding a new tree:

$$
\hat{y}^{(t)}
=
\hat{y}^{(t-1)}
+
f_t(x)
$$


The new tree learns the error of the previous model.

---

# 2. Objective Function

XGBoost minimizes:

$$
Obj
=
\sum_i l(y_i,\hat{y_i})
+
\sum_k \Omega(f_k)
$$


The objective contains:

1. Training loss

$$
l(y_i,\hat{y_i})
$$


2. Tree complexity regularization

$$
\Omega(f)
=
\gamma T
+
\frac12\lambda ||w||^2
$$


where:

- $T$ : number of leaf nodes
- $\gamma$ : penalty for adding leaves
- $\lambda$ : L2 regularization

---

# 3. Gradient Boosting

For each iteration, XGBoost calculates gradients.

First-order gradient:

$$
g_i
=
\frac{\partial l(y_i,\hat{y_i})}
{\partial \hat{y_i}}
$$


Second-order gradient:

$$
h_i
=
\frac{\partial^2 l(y_i,\hat{y_i})}
{\partial \hat{y_i}^2}
$$


Compared with traditional GBDT:

| Algorithm | Gradient |
|---|---|
| GBDT | First order |
| XGBoost | First + Second order |


---

# 4. Taylor Expansion

XGBoost uses second-order Taylor expansion:

$$
Obj^{(t)}
\approx
\sum_i
[
g_i f_t(x_i)
+
\frac12 h_i f_t^2(x_i)
]
+
\Omega(f_t)
$$


This improves:

- convergence speed
- optimization accuracy

---

# 5. Decision Tree Split

For each possible split, XGBoost calculates gain:


$$
Gain
=
\frac12
\left(
\frac{G_L^2}{H_L+\lambda}
+
\frac{G_R^2}{H_R+\lambda}
-
\frac{G^2}{H+\lambda}
\right)
-\gamma
$$


where:


$$
G=\sum_i g_i
$$


$$
H=\sum_i h_i
$$


A larger gain means a better split.

---

# 6. Prediction Update

After training a new tree:


$$
\hat{y}_t
=
\hat{y}_{t-1}
+
\eta f_t(x)
$$


where:

- $\eta$ : learning rate


Small learning rate:

- more stable
- requires more trees

---

# 7. Training Process

