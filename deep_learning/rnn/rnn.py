import torch
import torch.nn as nn
import matplotlib.pyplot as plt


# Simple RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()

        self.rnn = nn.RNN(
            input_size,
            hidden_size,
            batch_first=True
        )

        self.fc = nn.Linear(
            hidden_size,
            output_size
        )

    def forward(self, x):

        out, hidden = self.rnn(x)

        out = self.fc(out[:, -1, :])

        return out


# Generate sequence data
torch.manual_seed(0)

X = torch.linspace(0, 20, 200)

y = torch.sin(X)


sequence_length = 10

inputs = []
targets = []

for i in range(len(X)-sequence_length):

    inputs.append(
        y[i:i+sequence_length]
    )

    targets.append(
        y[i+sequence_length]
    )


inputs = torch.stack(inputs)

targets = torch.stack(targets)


inputs = inputs.unsqueeze(-1)


# Model
model = SimpleRNN(
    input_size=1,
    hidden_size=32,
    output_size=1
)


loss_fn = nn.MSELoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.01
)


loss_history = []


# Training
for epoch in range(200):

    prediction = model(inputs)

    loss = loss_fn(
        prediction.squeeze(),
        targets
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    loss_history.append(
        loss.item()
    )


# Prediction

with torch.no_grad():

    pred = model(inputs).squeeze()


# Plot prediction

plt.figure(figsize=(8,4))

plt.plot(
    targets.numpy(),
    label="True"
)

plt.plot(
    pred.numpy(),
    label="Prediction"
)

plt.legend()

plt.title("RNN Sequence Prediction")

plt.savefig(
    "./rnn_prediction.png"
)


# Plot loss

plt.figure(figsize=(6,4))

plt.plot(loss_history)

plt.title("Training Loss")

plt.xlabel("Epoch")

plt.ylabel("MSE")

plt.savefig(
    "./rnn_loss.png"
)