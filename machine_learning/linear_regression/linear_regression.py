import torch
import matplotlib.pyplot as plt


# Generate data
torch.manual_seed(0)

X = torch.randn(100, 1)
y = 3 * X + 2 + 0.1 * torch.randn(100, 1)


# Initialize parameters
w = torch.randn(1, requires_grad=True)
b = torch.randn(1, requires_grad=True)


# Training settings
lr = 0.01
epochs = 500

losses = []


# Gradient descent
for epoch in range(epochs):

    # Forward
    y_pred = X * w + b

    # MSE loss
    loss = ((y_pred - y) ** 2).mean()

    losses.append(loss.item())

    # Backward
    loss.backward()

    # Update parameters
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

        w.grad.zero_()
        b.grad.zero_()

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.6f}")


print("Weight:", w.item())
print("Bias:", b.item())


# Plot regression result
plt.figure(figsize=(6, 4))

plt.scatter(X.numpy(), y.numpy())
plt.plot(
    X.numpy(),
    (X * w + b).detach().numpy()
)

plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression")

plt.savefig(
    "./linear_regression.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Plot loss curve
plt.figure(figsize=(6, 4))

plt.plot(losses)

plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Training Loss")

plt.savefig(
    "./loss_curve.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()