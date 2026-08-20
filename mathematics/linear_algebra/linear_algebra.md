# Linear Algebra

## 1. Overview

Linear algebra studies vectors, matrices, linear transformations, and systems of linear equations.

It is widely used in machine learning and deep learning for:

- Data representation
- Model parameters
- Neural network computation
- Dimensionality reduction
- Optimization

---

## 2. Scalars, Vectors, and Matrices

A scalar is a single number:

$$
a \in \mathbb{R}
$$

A vector is an ordered list of numbers:

$$
\mathbf{x}
=
\begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix}
\in \mathbb{R}^{n}
$$

A matrix is a rectangular array of numbers:

$$
A
=
\begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
\in \mathbb{R}^{m \times n}
$$

---

## 3. Vector Operations

Vector addition:

$$
\mathbf{x}+\mathbf{y}
=
\begin{bmatrix}
x_1+y_1 \\
x_2+y_2 \\
\vdots \\
x_n+y_n
\end{bmatrix}
$$

Scalar multiplication:

$$
c\mathbf{x}
=
\begin{bmatrix}
cx_1 \\
cx_2 \\
\vdots \\
cx_n
\end{bmatrix}
$$

Dot product:

$$
\mathbf{x}^{T}\mathbf{y}
=
\sum_{i=1}^{n}x_i y_i
$$

---

## 4. Matrix Operations

Matrix addition:

$$
(A+B)_{ij}
=
a_{ij}+b_{ij}
$$

Matrix multiplication:

$$
C=AB
$$

where:

$$
c_{ij}
=
\sum_{k=1}^{n}a_{ik}b_{kj}
$$

Matrix multiplication is generally not commutative:

$$
AB \neq BA
$$

Element-wise multiplication:

$$
C=A\odot B
$$

$$
c_{ij}=a_{ij}b_{ij}
$$

---

## 5. Transpose

The transpose exchanges the rows and columns of a matrix.

$$
(A^{T})_{ij}
=
A_{ji}
$$

Important properties:

$$
(A^{T})^{T}=A
$$

$$
(A+B)^{T}=A^{T}+B^{T}
$$

$$
(AB)^{T}=B^{T}A^{T}
$$

---

## 6. Identity and Inverse Matrices

The identity matrix satisfies:

$$
AI=IA=A
$$

For example:

$$
I
=
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix}
$$

The inverse matrix satisfies:

$$
AA^{-1}
=
A^{-1}A
=
I
$$

For:

$$
A
=
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

the inverse is:

$$
A^{-1}
=
\frac{1}{ad-bc}
\begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
$$

---

## 7. Systems of Linear Equations

A system of linear equations can be written as:

$$
A\mathbf{x}
=
\mathbf{b}
$$

If the inverse of \(A\) exists:

$$
\mathbf{x}
=
A^{-1}\mathbf{b}
$$

---

## 8. Linear Independence and Basis

Vectors are linearly independent if:

$$
c_1\mathbf{v}_1
+
c_2\mathbf{v}_2
+
\cdots
+
c_k\mathbf{v}_k
=
\mathbf{0}
$$

has only the solution:

$$
c_1=c_2=\cdots=c_k=0
$$

A basis is a set of linearly independent vectors that spans a vector space.

---

## 9. Rank and Determinant

The rank of a matrix is the number of linearly independent rows or columns:

$$
\operatorname{rank}(A)
$$

For:

$$
A\in\mathbb{R}^{m\times n}
$$

$$
\operatorname{rank}(A)
\leq
\min(m,n)
$$

For a two-dimensional matrix:

$$
A
=
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

the determinant is:

$$
\det(A)
=
ad-bc
$$

A square matrix is invertible when:

$$
\det(A)\neq 0
$$

---

## 10. Vector Norms

The L1 norm is:

$$
\|\mathbf{x}\|_1
=
\sum_{i=1}^{n}|x_i|
$$

The L2 norm is:

$$
\|\mathbf{x}\|_2
=
\sqrt{
\sum_{i=1}^{n}x_i^2
}
$$

The general Lp norm is:

$$
\|\mathbf{x}\|_p
=
\left(
\sum_{i=1}^{n}|x_i|^p
\right)^{1/p}
$$

---

## 11. Distance and Cosine Similarity

Euclidean distance:

$$
d(\mathbf{x},\mathbf{y})
=
\|\mathbf{x}-\mathbf{y}\|_2
$$

Cosine similarity:

$$
\operatorname{cosine}(\mathbf{x},\mathbf{y})
=
\frac{
\mathbf{x}^{T}\mathbf{y}
}{
\|\mathbf{x}\|_2
\|\mathbf{y}\|_2
}
$$

---

## 12. Orthogonality and Projection

Two vectors are orthogonal if:

$$
\mathbf{x}^{T}\mathbf{y}
=
0
$$

The projection of \(\mathbf{x}\) onto \(\mathbf{u}\) is:

$$
\operatorname{proj}_{\mathbf{u}}(\mathbf{x})
=
\frac{
\mathbf{x}^{T}\mathbf{u}
}{
\mathbf{u}^{T}\mathbf{u}
}
\mathbf{u}
$$

---

## 13. Eigenvalues and Eigenvectors

For a square matrix \(A\), an eigenvector \(\mathbf{v}\) and an eigenvalue \(\lambda\) satisfy:

$$
A\mathbf{v}
=
\lambda\mathbf{v}
$$

The eigenvalues are obtained from:

$$
\det(A-\lambda I)
=
0
$$

Eigendecomposition:

$$
A
=
V\Lambda V^{-1}
$$

---

## 14. Singular Value Decomposition

Any matrix can be decomposed as:

$$
A
=
U\Sigma V^{T}
$$

where:

- \(U\) contains the left singular vectors
- \(V\) contains the right singular vectors
- \(\Sigma\) contains the singular values

A rank-\(k\) approximation is:

$$
A_k
=
U_k\Sigma_kV_k^{T}
$$

---

## 15. Linear Transformations

A linear transformation is:

$$
\mathbf{y}
=
A\mathbf{x}
$$

It satisfies:

$$
A(\mathbf{x}+\mathbf{y})
=
A\mathbf{x}
+
A\mathbf{y}
$$

$$
A(c\mathbf{x})
=
cA\mathbf{x}
$$

A neural network linear layer is:

$$
\mathbf{z}
=
W\mathbf{x}
+
\mathbf{b}
$$

---

## 16. Principal Component Analysis

For a centered data matrix:

$$
X\in\mathbb{R}^{n\times d}
$$

the covariance matrix is:

$$
C
=
\frac{1}{n-1}X^{T}X
$$

The principal directions satisfy:

$$
C\mathbf{v}_i
=
\lambda_i\mathbf{v}_i
$$

The transformed data is:

$$
Z
=
XV_k
$$

---

## 17. Linear Algebra in Artificial Intelligence

Linear regression:

$$
\hat{\mathbf{y}}
=
X\mathbf{w}
+
\mathbf{b}
$$

Neural network layer:

$$
\mathbf{z}
=
W\mathbf{x}
+
\mathbf{b}
$$

Self-attention:

$$
Q=XW_Q
$$

$$
K=XW_K
$$

$$
V=XW_V
$$

$$
\operatorname{Attention}(Q,K,V)
=
\operatorname{softmax}
\left(
\frac{QK^{T}}{\sqrt{d_k}}
\right)V
$$

---

## 18. Core Idea

The main purpose of linear algebra is to represent and transform multidimensional data.

The core concepts are:

$$
\text{Vectors and matrices}
$$

$$
\text{Matrix multiplication}
$$

$$
\text{Linear transformations}
$$

$$
\text{Eigenvalues and eigenvectors}
$$

$$
\text{Singular value decomposition}
$$
