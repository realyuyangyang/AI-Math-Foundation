# Perceptron（感知机）

## 1. Model

Perceptron is a binary linear classifier.

Given training data:

$$
(x_i,y_i),\quad y_i\in\{-1,+1\}
$$


The linear function:

$$
z=w^Tx+b
$$


where:

- $w$ is the weight vector
- $b$ is the bias


Prediction:

$$
\hat{y}=sign(w^Tx+b)
$$


The sign function:

$$
sign(z)=
\begin{cases}
+1, & z\geq0\\
-1, & z<0
\end{cases}
$$


---

# 2. Decision Boundary

The decision boundary is:

$$
w^Tx+b=0
$$


For two-dimensional data:

$$
w_1x_1+w_2x_2+b=0
$$


The boundary separates two classes.


---

# 3. Classification Condition

A correctly classified sample satisfies:

$$
y_i(w^Tx_i+b)>0
$$


A misclassified sample satisfies:

$$
y_i(w^Tx_i+b)\leq0
$$


---

# 4. Perceptron Loss Function

The loss is defined on misclassified samples:

$$
L(w,b)
=
-\sum_{x_i\in M}
y_i(w^Tx_i+b)
$$


where:

- $M$ is the set of misclassified samples.


---

# 5. Gradient Update

For a misclassified sample:

$$
y_i(w^Tx_i+b)\leq0
$$


Update weights:

$$
w=w+\eta y_ix_i
$$


Update bias:

$$
b=b+\eta y_i
$$


where:

- $\eta$ is the learning rate.


---

# 6. Training Algorithm

Initialize:

$$
w=0,\quad b=0
$$


For each training sample:

1. Compute prediction:

$$
\hat{y}=sign(w^Tx_i+b)
$$


2. Check classification:

$$
y_i(w^Tx_i+b)\leq0
$$


3. Update parameters:

$$
w=w+\eta y_ix_i
$$


$$
b=b+\eta y_i
$$


Repeat until convergence.


---

# 7. Geometric Interpretation

The model learns a hyperplane:

$$
w^Tx+b=0
$$


The vector $w$ is perpendicular to the decision boundary.


The distance from a point to the hyperplane:

$$
d=
\frac{|w^Tx+b|}
{||w||}
$$


---

# 8. Relationship with Neural Network

A perceptron can be viewed as a single neuron:

$$
y=f(w^Tx+b)
$$


where:

- Perceptron uses:

$$
f(x)=sign(x)
$$


- Neural networks use differentiable activation functions:

$$
f(x)=ReLU(x)
$$

or

$$
f(x)=\sigma(x)
$$


---

# 9. Limitation

Perceptron can only solve linearly separable problems.


A dataset is linearly separable if there exists:

$$
w,b
$$

such that:

$$
y_i(w^Tx_i+b)>0
$$

for all samples.


It cannot solve XOR:

$$
XOR(0,0)=0
$$

$$
XOR(0,1)=1
$$

$$
XOR(1,0)=1
$$

$$
XOR(1,1)=0
$$


because no single hyperplane can separate the two classes.


---

# 10. Historical Importance

Perceptron is the foundation of:

$$
\text{Perceptron}
\rightarrow
\text{MLP}
\rightarrow
\text{Backpropagation}
\rightarrow
\text{Deep Learning}
$$