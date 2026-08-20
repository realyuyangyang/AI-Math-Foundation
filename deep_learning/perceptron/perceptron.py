import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


class Perceptron:

    def __init__(self, lr=0.1, epochs=20):
        self.lr = lr
        self.epochs = epochs


    def fit(self, X, y):

        self.w = np.zeros(X.shape[1])
        self.b = 0

        self.errors = []

        for epoch in range(self.epochs):

            error = 0

            for xi, yi in zip(X, y):

                if yi * (np.dot(self.w, xi) + self.b) <= 0:

                    self.w += self.lr * yi * xi
                    self.b += self.lr * yi

                    error += 1

            self.errors.append(error)

            print(
                f"Epoch {epoch+1}: errors = {error}"
            )

            if error == 0:
                break


    def predict(self, X):

        return np.sign(
            np.dot(X, self.w) + self.b
        )



# ============================
# Generate Dataset
# ============================

X, y = make_blobs(
    n_samples=100,
    centers=2,
    n_features=2,
    cluster_std=1.2,
    random_state=42
)


# Convert labels:
# 0 -> -1
# 1 -> +1

y = np.where(y == 0, -1, 1)



# ============================
# Train
# ============================

model = Perceptron(
    lr=0.1,
    epochs=20
)

model.fit(X, y)


# ============================
# Plot Result
# ============================

plt.figure(figsize=(8,6))


# Data points

plt.scatter(
    X[:,0],
    X[:,1],
    c=y,
    s=50
)


# Decision boundary

x_min, x_max = X[:,0].min()-1, X[:,0].max()+1

x_values = np.linspace(
    x_min,
    x_max,
    200
)


# w1*x1+w2*x2+b=0

if model.w[1] != 0:

    y_values = (
        -model.w[0] * x_values
        - model.b
    ) / model.w[1]


    plt.plot(
        x_values,
        y_values
    )


plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.title(
    "Perceptron Decision Boundary"
)


plt.grid(True)


# Save figure

plt.savefig(
    "./perceptron_result.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()