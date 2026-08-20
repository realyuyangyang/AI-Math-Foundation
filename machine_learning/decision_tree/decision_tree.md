# Decision Tree Mathematics


## 1. Basic Idea

Decision Tree learns a sequence of decision rules:

$$
if\ condition(x):
    left
else:
    right
$$


The goal is to divide data into purer subsets.


---

# 2. Entropy


Entropy measures uncertainty:


$$
H(Y)
=
-\sum_{i=1}^{K}p_i\log_2 p_i
$$


where:

- $p_i$ is the probability of class $i$


For binary classification:


$$
H(Y)
=
-p_1\log_2p_1
-p_2\log_2p_2
$$


Maximum uncertainty:


$$
p_1=p_2=0.5
$$


$$
H(Y)=1
$$


Pure node:


$$
p_1=1
$$


$$
H(Y)=0
$$



---

# 3. Information Gain


Information Gain measures entropy reduction:


$$
IG(Y,X)
=
H(Y)-H(Y|X)
$$


Conditional entropy:


$$
H(Y|X)
=
\sum_v
\frac{|D_v|}{|D|}
H(Y_v)
$$


Decision Tree selects:


$$
\boxed{
\max IG(Y,X)
}
$$



---

# 4. Gini Impurity


CART Decision Tree uses Gini index:


$$
Gini(D)
=
1-\sum_{i=1}^{K}p_i^2
$$


Binary case:


$$
Gini(D)
=
1-p_1^2-p_2^2
$$


Pure node:


$$
Gini=0
$$


Maximum impurity:


$$
p_1=p_2=0.5
$$


$$
Gini=0.5
$$



---

# 5. Split Criterion


For a split:


$$
D \rightarrow D_1,D_2
$$


Weighted impurity:


$$
Gini_{split}
=
\frac{|D_1|}{|D|}
Gini(D_1)
+
\frac{|D_2|}{|D|}
Gini(D_2)
$$


Choose:


$$
\boxed{
\min Gini_{split}
}
$$



---

# 6. Regression Tree


Regression Tree predicts continuous values.


Leaf prediction:


$$
\hat y
=
\frac1N
\sum_{i=1}^{N}y_i
$$



Optimization:


$$
MSE
=
\frac1N
\sum_i
(y_i-\hat y)^2
$$



The split minimizes:


$$
\boxed{
\min MSE
}
$$



---

# 7. Tree Growing Algorithm


Input:

$$
D=\{(x_i,y_i)\}_{i=1}^{N}
$$


Algorithm:


1. Select feature $X_j$

2. Find split point $s$


$$
X_j < s
$$


3. Calculate impurity

4. Choose best split

5. Repeat recursively


---

# 8. Overfitting Control


Maximum depth:


$$
depth(T)\leq d
$$


Minimum samples:


$$
N_{leaf}\geq m
$$


Pruning removes unnecessary branches.


---

# 9. Prediction


Classification:


$$
\hat y
=
\arg\max_k P(y=k|x)
$$


Regression:


$$
\hat y
=
mean(y_{leaf})
$$