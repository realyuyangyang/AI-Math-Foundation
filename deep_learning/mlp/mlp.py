import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

torch.manual_seed(42)
np.random.seed(42)

X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)


class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(2, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 2)
        )

    def forward(self, x):
        return self.network(x)


model = MLP()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

epochs = 300
loss_history = []

for epoch in range(epochs):
    model.train()

    logits = model(X_train)
    loss = criterion(logits, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    loss_history.append(loss.item())

model.eval()

with torch.no_grad():
    test_logits = model(X_test)
    test_predictions = torch.argmax(test_logits, dim=1)
    test_accuracy = (test_predictions == y_test).float().mean().item()

print(f"Test Accuracy: {test_accuracy:.4f}")

x_min, x_max = X_train[:, 0].min().item() - 0.5, X_train[:, 0].max().item() + 0.5
y_min, y_max = X_train[:, 1].min().item() - 0.5, X_train[:, 1].max().item() + 0.5

xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 300),
    np.linspace(y_min, y_max, 300)
)

grid = torch.tensor(
    np.c_[xx.ravel(), yy.ravel()],
    dtype=torch.float32
)

with torch.no_grad():
    grid_predictions = torch.argmax(model(grid), dim=1).numpy()

grid_predictions = grid_predictions.reshape(xx.shape)

plt.figure(figsize=(7, 5))
plt.contourf(xx, yy, grid_predictions, alpha=0.3)
plt.scatter(
    X_test[:, 0].numpy(),
    X_test[:, 1].numpy(),
    c=y_test.numpy(),
    edgecolors="k"
)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title(f"MLP Decision Boundary | Accuracy: {test_accuracy:.4f}")
plt.tight_layout()
plt.savefig("./mlp_result.png", dpi=300)
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(loss_history)
plt.xlabel("Epoch")
plt.ylabel("Cross-Entropy Loss")
plt.title("MLP Training Loss")
plt.tight_layout()
plt.savefig("./loss_curve.png", dpi=300)
plt.show()
