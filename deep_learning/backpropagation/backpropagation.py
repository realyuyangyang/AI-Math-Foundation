import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Generate dataset
# -----------------------------
np.random.seed(0)

X = np.random.randn(200, 2)

y = (X[:, 0] * X[:, 1] > 0).astype(int)
y = y.reshape(-1, 1)


# -----------------------------
# Activation functions
# -----------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    s = sigmoid(x)
    return s * (1 - s)


# -----------------------------
# Initialize parameters
# -----------------------------
input_size = 2
hidden_size = 8
output_size = 1

W1 = np.random.randn(input_size, hidden_size) * 0.1
b1 = np.zeros((1, hidden_size))

W2 = np.random.randn(hidden_size, output_size) * 0.1
b2 = np.zeros((1, output_size))


# -----------------------------
# Training
# -----------------------------
lr = 0.5
epochs = 2000

loss_history = []


for epoch in range(epochs):

    # Forward
    z1 = X @ W1 + b1
    a1 = sigmoid(z1)

    z2 = a1 @ W2 + b2
    y_hat = sigmoid(z2)


    # Loss
    loss = np.mean(
        -(y*np.log(y_hat+1e-8)
        +(1-y)*np.log(1-y_hat+1e-8))
    )

    loss_history.append(loss)


    # -------------------------
    # Backpropagation
    # -------------------------

    # output error
    dz2 = y_hat - y

    dW2 = a1.T @ dz2 / len(X)
    db2 = np.mean(dz2, axis=0, keepdims=True)


    # hidden layer error
    dz1 = (dz2 @ W2.T) * sigmoid_derivative(z1)

    dW1 = X.T @ dz1 / len(X)
    db1 = np.mean(dz1, axis=0, keepdims=True)


    # Update parameters
    W2 -= lr * dW2
    b2 -= lr * db2

    W1 -= lr * dW1
    b1 -= lr * db1


    if epoch % 200 == 0:
        print(
            f"Epoch {epoch}, Loss={loss:.4f}"
        )


# -----------------------------
# Loss curve
# -----------------------------
plt.figure(figsize=(6,4))

plt.plot(loss_history)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Backpropagation Loss")

plt.grid()

plt.savefig(
    "./loss_curve.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# -----------------------------
# Decision boundary
# -----------------------------
xx, yy = np.meshgrid(
    np.linspace(-3,3,300),
    np.linspace(-3,3,300)
)

grid = np.c_[xx.ravel(), yy.ravel()]


z1 = grid @ W1 + b1
a1 = sigmoid(z1)

z2 = a1 @ W2 + b2
pred = sigmoid(z2)

pred = pred.reshape(xx.shape)


plt.figure(figsize=(6,5))

plt.contourf(
    xx,
    yy,
    pred,
    levels=[0,0.5,1],
    alpha=0.3
)

plt.scatter(
    X[:,0],
    X[:,1],
    c=y[:,0],
    edgecolors="k"
)

plt.title(
    "Decision Boundary"
)

plt.xlabel("x1")
plt.ylabel("x2")

plt.savefig(
    "./decision_boundary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("Training finished")
print("Images saved:")
print("loss_curve.png")
print("decision_boundary.png")