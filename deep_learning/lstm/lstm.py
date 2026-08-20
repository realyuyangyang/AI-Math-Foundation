import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

torch.manual_seed(42)
np.random.seed(42)

num_samples = 1000
seq_len = 20

X = np.random.randn(num_samples, seq_len, 1).astype(np.float32)
y = (X.sum(axis=1) > 0).astype(np.float32)

X_train = torch.tensor(X[:800])
y_train = torch.tensor(y[:800])
X_test = torch.tensor(X[800:])
y_test = torch.tensor(y[800:])

train_loader = DataLoader(
    TensorDataset(X_train, y_train),
    batch_size=32,
    shuffle=True
)


class LSTMClassifier(nn.Module):
    def __init__(self, input_size=1, hidden_size=32, num_layers=1):
        super().__init__()
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True
        )
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        output, (h_n, c_n) = self.lstm(x)
        logits = self.fc(h_n[-1])
        return logits


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = LSTMClassifier().to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

loss_history = []

for epoch in range(30):
    model.train()
    total_loss = 0.0

    for batch_X, batch_y in train_loader:
        batch_X = batch_X.to(device)
        batch_y = batch_y.to(device)

        optimizer.zero_grad()
        logits = model(batch_X)
        loss = criterion(logits, batch_y)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    average_loss = total_loss / len(train_loader)
    loss_history.append(average_loss)

    print(f"Epoch {epoch + 1:02d}, Loss: {average_loss:.4f}")

model.eval()

with torch.no_grad():
    logits = model(X_test.to(device))
    probabilities = torch.sigmoid(logits)
    predictions = (probabilities >= 0.5).float()
    accuracy = (predictions.cpu() == y_test).float().mean()

print(f"Test Accuracy: {accuracy.item():.4f}")

plt.plot(loss_history)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("LSTM Training Loss")
plt.tight_layout()
plt.savefig("./loss_curve.png")
plt.show()
