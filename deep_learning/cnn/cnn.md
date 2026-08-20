# Convolutional Neural Network (CNN)

## 1. Convolution Operation

Input image:

$$
X \in R^{H \times W \times C}
$$


Convolution:

$$
Y_{i,j}
=
\sum_m
\sum_n
X_{i+m,j+n}K_{m,n}
$$


where:

- X: input image
- K: convolution kernel
- Y: feature map


---

## 2. Multiple Channels


For RGB image:

$$
X \in R^{H \times W \times 3}
$$


Output feature map:

$$
Y
=
\sum_{c=1}^{C}
X_c*K_c+b
$$


---

## 3. Activation Function


CNN usually uses ReLU:


$$
ReLU(x)=max(0,x)
$$


---

## 4. Pooling


Max Pooling:

$$
Y_{i,j}
=
max(X_{i:i+k,j:j+k})
$$


Purpose:

- reduce dimension
- keep important features


---

## 5. Fully Connected Layer


After convolution:

$$
z=Wx+b
$$


Prediction:

$$
\hat y=softmax(z)
$$


---

## 6. Cross Entropy Loss


For classification:


$$
L
=
-\sum_i y_i log(\hat y_i)
$$


---

## 7. Backpropagation


Gradient:


$$
\frac{\partial L}{\partial W}
$$


Update:


$$
W
=
W-\eta
\frac{\partial L}{\partial W}
$$


where:

- η: learning rate


---

## CNN Architecture


Input Image

↓

Convolution

↓

ReLU

↓

Pooling

↓

Convolution

↓

ReLU

↓

Pooling

↓

Flatten

↓

Fully Connected

↓

Prediction