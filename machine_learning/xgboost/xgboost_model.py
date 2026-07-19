import xgboost as xgb
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# =========================
# 1. Generate Dataset
# =========================

X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=10,
    n_redundant=5,
    random_state=42
)


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# 2. Build XGBoost Model
# =========================

model = xgb.XGBClassifier(
    n_estimators=100,
    max_depth=3,
    learning_rate=0.1,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)


# =========================
# 3. Train
# =========================

model.fit(
    X_train,
    y_train
)


# =========================
# 4. Prediction
# =========================

y_pred = model.predict(X_test)


accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Accuracy:", accuracy)


# =========================
# 5. Feature Importance Plot
# =========================

xgb.plot_importance(
    model,
    max_num_features=10
)

plt.title(
    "XGBoost Feature Importance"
)

plt.tight_layout()

plt.savefig(
    "./xgboost_feature_importance.png",
    dpi=300
)

plt.show()