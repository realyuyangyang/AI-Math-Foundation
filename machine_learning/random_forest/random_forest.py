# random_forest.py

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# =========================
# 1. Generate Dataset
# =========================

X, y = make_classification(
    n_samples=500,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    random_state=42
)


# =========================
# 2. Train/Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# 3. Random Forest Model
# =========================

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)


model.fit(
    X_train,
    y_train
)


# =========================
# 4. Evaluation
# =========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Accuracy:", accuracy)


# =========================
# 5. Decision Boundary
# =========================

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1


xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 300),
    np.linspace(y_min, y_max, 300)
)


grid = np.c_[
    xx.ravel(),
    yy.ravel()
]


Z = model.predict(grid)

Z = Z.reshape(xx.shape)


plt.figure(figsize=(8, 6))

plt.contourf(
    xx,
    yy,
    Z,
    alpha=0.3
)


plt.scatter(
    X_train[:, 0],
    X_train[:, 1],
    c=y_train,
    marker="o",
    label="Train"
)


plt.scatter(
    X_test[:, 0],
    X_test[:, 1],
    c=y_test,
    marker="x",
    label="Test"
)


plt.title(
    "Random Forest Decision Boundary"
)

plt.xlabel(
    "Feature 1"
)

plt.ylabel(
    "Feature 2"
)

plt.legend()

plt.savefig(
    "./random_forest_boundary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# =========================
# 6. Feature Importance
# =========================

importance = model.feature_importances_


plt.figure(figsize=(6, 4))

plt.bar(
    ["Feature 1", "Feature 2"],
    importance
)


plt.title(
    "Random Forest Feature Importance"
)


plt.ylabel(
    "Importance"
)


plt.savefig(
    "./random_forest_feature_importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()