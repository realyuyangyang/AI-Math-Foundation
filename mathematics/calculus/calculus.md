# Calculus

## 1. Functions

A function maps an input to an output:

$$
y=f(x)
$$

Common functions:

### 1.1 Linear Function

$$
f(x)=ax+b
$$

### 1.2 Polynomial Function

$$
f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0
$$

### 1.3 Exponential Function

$$
f(x)=a^x
$$

Special case:

$$
f(x)=e^x
$$

### 1.4 Logarithmic Function

$$
f(x)=\log_a x
$$

Natural logarithm:

$$
f(x)=\ln x
$$

### 1.5 Trigonometric Functions

$$
\sin x,\quad \cos x,\quad \tan x
$$

---

## 2. Limits

The limit describes the value that a function approaches:

$$
\lim_{x\to a}f(x)=L
$$

### 2.1 Basic Limit Rules

$$
\lim_{x\to a}[f(x)+g(x)]
=
\lim_{x\to a}f(x)+\lim_{x\to a}g(x)
$$

$$
\lim_{x\to a}[f(x)g(x)]
=
\left(\lim_{x\to a}f(x)\right)
\left(\lim_{x\to a}g(x)\right)
$$

$$
\lim_{x\to a}\frac{f(x)}{g(x)}
=
\frac{\lim_{x\to a}f(x)}{\lim_{x\to a}g(x)}
$$

### 2.2 Important Limits

$$
\lim_{x\to 0}\frac{\sin x}{x}=1
$$

$$
\lim_{x\to 0}\frac{e^x-1}{x}=1
$$

$$
\lim_{x\to 0}\frac{\ln(1+x)}{x}=1
$$

$$
\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n=e
$$

---

## 3. Continuity

A function is continuous at $x=a$ if:

$$
\lim_{x\to a}f(x)=f(a)
$$

The three conditions are:

$$
f(a)\text{ exists}
$$

$$
\lim_{x\to a}f(x)\text{ exists}
$$

$$
\lim_{x\to a}f(x)=f(a)
$$

---

## 4. Derivatives

The derivative measures the instantaneous rate of change of a function.

### 4.1 Definition

$$
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
$$

Other notations:

$$
f'(x),\quad \frac{dy}{dx},\quad \frac{df}{dx}
$$

### 4.2 Basic Derivative Rules

Constant rule:

$$
\frac{d}{dx}c=0
$$

Power rule:

$$
\frac{d}{dx}x^n=nx^{n-1}
$$

Constant multiple rule:

$$
\frac{d}{dx}[cf(x)]=cf'(x)
$$

Sum rule:

$$
\frac{d}{dx}[f(x)+g(x)]=f'(x)+g'(x)
$$

Product rule:

$$
\frac{d}{dx}[f(x)g(x)]
=
f'(x)g(x)+f(x)g'(x)
$$

Quotient rule:

$$
\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right]
=
\frac{f'(x)g(x)-f(x)g'(x)}{[g(x)]^2}
$$

Chain rule:

$$
\frac{d}{dx}f(g(x))
=
f'(g(x))g'(x)
$$

### 4.3 Common Derivatives

$$
\frac{d}{dx}e^x=e^x
$$

$$
\frac{d}{dx}a^x=a^x\ln a
$$

$$
\frac{d}{dx}\ln x=\frac{1}{x}
$$

$$
\frac{d}{dx}\log_a x=\frac{1}{x\ln a}
$$

$$
\frac{d}{dx}\sin x=\cos x
$$

$$
\frac{d}{dx}\cos x=-\sin x
$$

$$
\frac{d}{dx}\tan x=\sec^2 x
$$

$$
\frac{d}{dx}\arcsin x=\frac{1}{\sqrt{1-x^2}}
$$

$$
\frac{d}{dx}\arctan x=\frac{1}{1+x^2}
$$

---

## 5. Higher-Order Derivatives

Second derivative:

$$
f''(x)=\frac{d^2y}{dx^2}
$$

The second derivative describes the rate of change of the first derivative.

Higher-order derivative:

$$
f^{(n)}(x)=\frac{d^ny}{dx^n}
$$

---

## 6. Applications of Derivatives

### 6.1 Critical Points

Critical points satisfy:

$$
f'(x)=0
$$

or the derivative does not exist.

### 6.2 Increasing and Decreasing Functions

If:

$$
f'(x)>0
$$

then $f(x)$ is increasing.

If:

$$
f'(x)<0
$$

then $f(x)$ is decreasing.

### 6.3 Local Maximum and Minimum

First derivative test:

$$
f'(x): +\to-
$$

indicates a local maximum.

$$
f'(x): -\to+
$$

indicates a local minimum.

Second derivative test:

If:

$$
f'(x_0)=0
$$

and:

$$
f''(x_0)>0
$$

then $x_0$ is a local minimum.

If:

$$
f''(x_0)<0
$$

then $x_0$ is a local maximum.

### 6.4 Convexity and Concavity

If:

$$
f''(x)>0
$$

then the function is convex.

If:

$$
f''(x)<0
$$

then the function is concave.

### 6.5 Linear Approximation

Near $x=a$:

$$
f(x)\approx f(a)+f'(a)(x-a)
$$

---

## 7. Integrals

Integration is the reverse process of differentiation.

### 7.1 Indefinite Integral

$$
\int f(x)\,dx=F(x)+C
$$

where:

$$
F'(x)=f(x)
$$

### 7.2 Definite Integral

$$
\int_a^b f(x)\,dx
$$

represents the signed area under the curve from $a$ to $b$.

### 7.3 Fundamental Theorem of Calculus

$$
\int_a^b f(x)\,dx=F(b)-F(a)
$$

where:

$$
F'(x)=f(x)
$$

Also:

$$
\frac{d}{dx}\int_a^x f(t)\,dt=f(x)
$$

---

## 8. Basic Integration Formulas

$$
\int x^n\,dx=\frac{x^{n+1}}{n+1}+C,
\quad n\neq -1
$$

$$
\int \frac{1}{x}\,dx=\ln|x|+C
$$

$$
\int e^x\,dx=e^x+C
$$

$$
\int a^x\,dx=\frac{a^x}{\ln a}+C
$$

$$
\int \sin x\,dx=-\cos x+C
$$

$$
\int \cos x\,dx=\sin x+C
$$

$$
\int \sec^2 x\,dx=\tan x+C
$$

$$
\int \frac{1}{1+x^2}\,dx=\arctan x+C
$$

$$
\int \frac{1}{\sqrt{1-x^2}}\,dx=\arcsin x+C
$$

---

## 9. Integration Techniques

### 9.1 Substitution

Let:

$$
u=g(x)
$$

Then:

$$
du=g'(x)\,dx
$$

Therefore:

$$
\int f(g(x))g'(x)\,dx
=
\int f(u)\,du
$$

### 9.2 Integration by Parts

$$
\int u\,dv=uv-\int v\,du
$$

### 9.3 Partial Fractions

For a rational function:

$$
\frac{P(x)}{Q(x)}
$$

factor $Q(x)$ and decompose the fraction into simpler terms before integration.

---

## 10. Improper Integrals

Infinite interval:

$$
\int_a^{\infty}f(x)\,dx
=
\lim_{b\to\infty}\int_a^b f(x)\,dx
$$

Unbounded function:

$$
\int_a^b f(x)\,dx
=
\lim_{c\to a^+}\int_c^b f(x)\,dx
$$

---

## 11. Sequences

A sequence is written as:

$$
\{a_n\}_{n=1}^{\infty}
$$

A sequence converges to $L$ if:

$$
\lim_{n\to\infty}a_n=L
$$

Geometric sequence:

$$
a_n=ar^{n-1}
$$

---

## 12. Series

An infinite series is:

$$
\sum_{n=1}^{\infty}a_n
$$

### 12.1 Geometric Series

$$
\sum_{n=0}^{\infty}ar^n
=
\frac{a}{1-r},
\quad |r|<1
$$

### 12.2 Harmonic Series

$$
\sum_{n=1}^{\infty}\frac{1}{n}
$$

The harmonic series diverges.

### 12.3 P-Series

$$
\sum_{n=1}^{\infty}\frac{1}{n^p}
$$

It converges when:

$$
p>1
$$

It diverges when:

$$
p\leq 1
$$

---

## 13. Taylor Series

The Taylor series of $f(x)$ around $x=a$ is:

$$
f(x)
=
\sum_{n=0}^{\infty}
\frac{f^{(n)}(a)}{n!}(x-a)^n
$$

Maclaurin series is the special case $a=0$:

$$
f(x)
=
\sum_{n=0}^{\infty}
\frac{f^{(n)}(0)}{n!}x^n
$$

Common expansions:

$$
e^x
=
1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots
$$

$$
\sin x
=
x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots
$$

$$
\cos x
=
1-\frac{x^2}{2!}+\frac{x^4}{4!}-\cdots
$$

$$
\ln(1+x)
=
x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots
$$

---

## 14. Multivariable Functions

A multivariable function has more than one input:

$$
z=f(x,y)
$$

or:

$$
f(x_1,x_2,\ldots,x_n)
$$

---

## 15. Partial Derivatives

The partial derivative with respect to $x$ is:

$$
\frac{\partial f}{\partial x}
$$

The partial derivative with respect to $y$ is:

$$
\frac{\partial f}{\partial y}
$$

Example:

$$
f(x,y)=x^2y+3y^2
$$

Then:

$$
\frac{\partial f}{\partial x}=2xy
$$

$$
\frac{\partial f}{\partial y}=x^2+6y
$$

---

## 16. Gradient

The gradient is the vector of all first-order partial derivatives:

$$
\nabla f(x)
=
\begin{bmatrix}
\frac{\partial f}{\partial x_1}\\
\frac{\partial f}{\partial x_2}\\
\vdots\\
\frac{\partial f}{\partial x_n}
\end{bmatrix}
$$

For two variables:

$$
\nabla f(x,y)
=
\begin{bmatrix}
\frac{\partial f}{\partial x}\\
\frac{\partial f}{\partial y}
\end{bmatrix}
$$

The gradient points in the direction of the fastest increase of the function.

---

## 17. Directional Derivative

For a unit vector $u$:

$$
D_uf(x)=\nabla f(x)^Tu
$$

---

## 18. Multivariable Chain Rule

If:

$$
z=f(x,y)
$$

where:

$$
x=x(t),\quad y=y(t)
$$

then:

$$
\frac{dz}{dt}
=
\frac{\partial f}{\partial x}\frac{dx}{dt}
+
\frac{\partial f}{\partial y}\frac{dy}{dt}
$$

For vector functions:

$$
\frac{\partial L}{\partial x}
=
\frac{\partial L}{\partial y}
\frac{\partial y}{\partial x}
$$

This formula is the mathematical foundation of backpropagation.

---

## 19. Jacobian Matrix

For a vector-valued function:

$$
f:\mathbb{R}^n\to\mathbb{R}^m
$$

The Jacobian matrix is:

$$
J_f(x)
=
\begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n}\\
\vdots & \ddots & \vdots\\
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}
$$

---

## 20. Hessian Matrix

The Hessian matrix contains all second-order partial derivatives:

$$
H_f(x)
=
\begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2}
&
\frac{\partial^2 f}{\partial x_1\partial x_2}
&
\cdots
\\
\frac{\partial^2 f}{\partial x_2\partial x_1}
&
\frac{\partial^2 f}{\partial x_2^2}
&
\cdots
\\
\vdots & \vdots & \ddots
\end{bmatrix}
$$

For optimization:

- Positive definite Hessian: local minimum.
- Negative definite Hessian: local maximum.
- Indefinite Hessian: saddle point.

---

## 21. Multivariable Optimization

A stationary point satisfies:

$$
\nabla f(x)=0
$$

Gradient descent updates parameters using:

$$
x_{t+1}=x_t-\eta\nabla f(x_t)
$$

where:

$$
\eta>0
$$

is the learning rate.

---

## 22. Double and Multiple Integrals

Double integral:

$$
\iint_D f(x,y)\,dA
$$

Iterated form:

$$
\int_a^b\int_c^d f(x,y)\,dy\,dx
$$

Triple integral:

$$
\iiint_V f(x,y,z)\,dV
$$

---

## 23. Differential Equations

A differential equation contains an unknown function and its derivatives.

### 23.1 First-Order Differential Equation

$$
\frac{dy}{dx}=f(x,y)
$$

### 23.2 Separable Equation

$$
\frac{dy}{dx}=g(x)h(y)
$$

Rearrange:

$$
\frac{1}{h(y)}\,dy=g(x)\,dx
$$

Then integrate both sides.

### 23.3 Exponential Growth and Decay

$$
\frac{dy}{dt}=ky
$$

Solution:

$$
y(t)=y_0e^{kt}
$$

---

## 24. Core Calculus Structure

The basic learning order is:

1. Functions
2. Limits
3. Continuity
4. Derivatives
5. Applications of derivatives
6. Integrals
7. Applications of integrals
8. Sequences and series
9. Taylor series
10. Multivariable calculus
11. Gradient, Jacobian, and Hessian
12. Optimization and differential equations

The most important formulas for artificial intelligence are:

$$
f'(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}
$$

$$
\frac{d}{dx}f(g(x))=f'(g(x))g'(x)
$$

$$
\nabla f(x)
=
\begin{bmatrix}
\frac{\partial f}{\partial x_1}\\
\vdots\\
\frac{\partial f}{\partial x_n}
\end{bmatrix}
$$

$$
H_f(x)
=
\left[
\frac{\partial^2 f}{\partial x_i\partial x_j}
\right]
$$

$$
x_{t+1}=x_t-\eta\nabla f(x_t)
$$

$$
f(x)\approx f(a)+f'(a)(x-a)
$$

$$
f(x)
=
\sum_{n=0}^{\infty}
\frac{f^{(n)}(a)}{n!}(x-a)^n
$$
