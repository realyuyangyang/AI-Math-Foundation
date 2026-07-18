import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification


# Generate dataset
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_classes=2,
    random_state=42
)


# Initialize parameters
w = np.zeros(X.shape[1])
b = 0

learning_rate = 0.1
epochs = 1000


# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


loss_history = []


# Training
for epoch in range(epochs):

    # Forward propagation
    z = X @ w + b
    y_pred = sigmoid(z)


    # Binary Cross Entropy loss
    loss = -np.mean(
        y * np.log(y_pred + 1e-8)
        +
        (1 - y) * np.log(1 - y_pred + 1e-8)
    )

    loss_history.append(loss)


    # Backward propagation
    dw = (1 / len(X)) * X.T @ (y_pred - y)
    db = np.mean(y_pred - y)


    # Gradient descent update
    w -= learning_rate * dw
    b -= learning_rate * db


# Prediction
probabilities = sigmoid(X @ w + b)
predictions = probabilities >= 0.5


# Accuracy
accuracy = np.mean(predictions == y)

print("Weights:", w)
print("Bias:", b)
print("Accuracy:", accuracy)


# Plot loss curve
plt.plot(loss_history)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Logistic Regression Training Loss")

plt.savefig("./loss_curve.png")
plt.close()