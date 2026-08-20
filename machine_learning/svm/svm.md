# Support Vector Machine (SVM)

## 1. Linear Decision Function

Given training data:

$$
(x_i,y_i),\quad y_i\in\{-1,+1\}
$$

The decision boundary:

$$
w^Tx+b=0
$$

Prediction:

$$
\hat{y}=sign(w^Tx+b)
$$


---

## 2. Maximum Margin

Distance from a point to the hyperplane:

$$
d=\frac{|w^Tx+b|}{||w||}
$$


For support vectors:

$$
y_i(w^Tx_i+b)=1
$$


The margin boundaries:

$$
w^Tx+b=1
$$

and

$$
w^Tx+b=-1
$$


Margin size:

$$
Margin=\frac{2}{||w||}
$$


Maximum margin:

$$
\max \frac{2}{||w||}
$$


Equivalent optimization:

$$
\min \frac12||w||^2
$$


---

## 3. Hard Margin SVM

Optimization problem:

$$
\min_{w,b}
\frac12||w||^2
$$


Subject to:

$$
y_i(w^Tx_i+b)\geq1
$$


---

## 4. Soft Margin SVM

Introduce slack variables:

$$
\xi_i\geq0
$$


Objective function:

$$
\min
\frac12||w||^2
+
C\sum_i\xi_i
$$


Constraint:

$$
y_i(w^Tx_i+b)\geq1-\xi_i
$$


---

## 5. Hinge Loss

Hinge loss:

$$
L_i=
max(0,1-y_i(w^Tx_i+b))
$$


Total loss:

$$
L=
\sum_i max(0,1-y_i(w^Tx_i+b))
$$


---

## 6. Kernel Trick

Mapping input into high-dimensional space:

$$
\phi(x)
$$


Kernel function:

$$
K(x_i,x_j)
=
\phi(x_i)^T\phi(x_j)
$$


Linear kernel:

$$
K(x_i,x_j)=x_i^Tx_j
$$


Polynomial kernel:

$$
K(x_i,x_j)
=
(x_i^Tx_j+c)^d
$$


Gaussian RBF kernel:

$$
K(x_i,x_j)
=
exp(-\gamma||x_i-x_j||^2)
$$


---

## 7. Dual Formulation

Lagrange multipliers:

$$
\alpha_i
$$


Dual optimization:

$$
\max_\alpha
\sum_i\alpha_i
-
\frac12
\sum_i\sum_j
\alpha_i\alpha_jy_iy_jK(x_i,x_j)
$$


Constraints:

$$
\alpha_i\geq0
$$


$$
\sum_i\alpha_iy_i=0
$$


---

## 8. Decision Function

Final classifier:

$$
f(x)
=
\sum_i
\alpha_i y_iK(x_i,x)+b
$$


Prediction:

$$
\hat y=sign(f(x))
$$


---

## 9. Support Vectors

Support vectors satisfy:

$$
\alpha_i>0
$$


or:

$$
y_i(w^Tx_i+b)=1
$$


Only support vectors determine the decision boundary.


---

## 10. Parameter Effects

### C Parameter

Large C:

$$
C\uparrow
$$

- Smaller training error
- Narrower margin
- Higher overfitting risk


Small C:

$$
C\downarrow
$$

- Larger margin
- More tolerance to errors


---

### Gamma Parameter

Large gamma:

$$
\gamma\uparrow
$$

- More complex decision boundary


Small gamma:

$$
\gamma\downarrow
$$

- Smoother decision boundary