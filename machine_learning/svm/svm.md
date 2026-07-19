# Support Vector Machine (SVM)

## 1. Linear Decision Function

Given training data:

$$
(x_i,y_i),\quad y_i\in\{-1,+1\}
$$

The decision boundary is:

$$
w^Tx+b=0
$$


Prediction:

$$
\hat{y}=sign(w^Tx+b)
$$


---

## 2. Maximum Margin

The distance from a point to the hyperplane:

$$
d=\frac{|w^Tx+b|}{||w||}
$$


For support vectors:

$$
y_i(w^Tx_i+b)=1
$$


The two margin boundaries:

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


Maximize margin:

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


Objective:

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

The hinge loss function:

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

## 6. Kernel Function

Mapping input into high dimensional space:

$$
\phi(x)
$$


Kernel trick:

$$
K(x_i,x_j)
=
\phi(x_i)^T\phi(x_j)
$$


### Linear Kernel

$$
K(x_i,x_j)=x_i^Tx_j
$$


### Polynomial Kernel

$$
K(x_i,x_j)
=
(x_i^Tx_j+c)^d
$$


### Gaussian RBF Kernel

$$
K(x_i,x_j)
=
exp(-\gamma||x_i-x_j||^2)
$$


---

## 7. Dual Optimization

Lagrangian multipliers:

$$
\alpha_i
$$


Dual form:

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
\alpha_i y_i K(x_i,x)+b
$$


Prediction:

$$
\hat y=sign(f(x))
$$


---

## 9. Support Vector Condition

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

## 10. Parameters

### C

Large C:

$$
C\uparrow
$$

- smaller training error
- smaller margin
- higher overfitting risk


Small C:

$$
C\downarrow
$$

- larger margin
- more tolerance to errors


### Gamma (RBF Kernel)

Large gamma:

$$
\gamma\uparrow
$$

- complex decision boundary


Small gamma:

$$
\gamma\downarrow
$$

- smoother decision boundary