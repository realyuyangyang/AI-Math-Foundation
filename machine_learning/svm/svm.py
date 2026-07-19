import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


# =========================
# Generate dataset
# =========================

X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    random_state=42
)


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# Train SVM
# =========================

model = SVC(
    kernel="linear",
    C=1.0
)

model.fit(
    X_train,
    y_train
)


print("Accuracy:",
      model.score(X_test, y_test))


# =========================
# Plot decision boundary
# =========================

plt.figure(figsize=(8, 6), dpi= 300)


# data points
plt.scatter(
    X_train[:, 0],
    X_train[:, 1],
    c=y_train,
    s=40
)


# support vectors

plt.scatter(
    model.support_vectors_[:, 0],
    model.support_vectors_[:, 1],
    s=120,
    facecolors="none"
)


# create grid

ax = plt.gca()

xlim = ax.get_xlim()
ylim = ax.get_ylim()


xx = np.linspace(
    xlim[0],
    xlim[1],
    300
)

yy = np.linspace(
    ylim[0],
    ylim[1],
    300
)


YY, XX = np.meshgrid(
    yy,
    xx
)


xy = np.vstack(
    [
        XX.ravel(),
        YY.ravel()
    ]
).T


Z = model.decision_function(xy).reshape(
    XX.shape
)


# decision boundary and margins

ax.contour(
    XX,
    YY,
    Z,
    colors="k",
    levels=[-1, 0, 1],
    linestyles=["--", "-", "--"]
)


plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.title(
    "Linear SVM Decision Boundary"
)


plt.savefig(
    "./svm_boundary.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()