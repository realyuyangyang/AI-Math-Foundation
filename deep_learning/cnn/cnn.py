import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt


# Fake image dataset
# 100 samples, 1 channel, 28x28 image
X = torch.randn(100, 1, 28, 28)

# Binary labels
y = torch.randint(0, 2, (100,))


class CNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=16,
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(
                16,
                32,
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),

            nn.MaxPool2d(2)
        )


        self.fc = nn.Sequential(
            nn.Linear(32 * 7 * 7, 64),
            nn.ReLU(),
            nn.Linear(64, 2)
        )


    def forward(self, x):

        x = self.conv(x)

        x = x.view(
            x.size(0),
            -1
        )

        x = self.fc(x)

        return x



model = CNN()


criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)


loss_history = []


for epoch in range(50):

    output = model(X)

    loss = criterion(
        output,
        y
    )


    optimizer.zero_grad()

    loss.backward()

    optimizer.step()


    loss_history.append(
        loss.item()
    )


    if epoch % 10 == 0:
        print(
            "Epoch:",
            epoch,
            "Loss:",
            loss.item()
        )



plt.plot(loss_history)

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.title("CNN Training Loss")

plt.savefig(
    "./loss_curve.png"
)

plt.show()