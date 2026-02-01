import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# =========================
# 1. Load Dataset
# =========================
df = pd.read_csv("data/dataset.csv")

print("Dataset shape:", df.shape)
print("Columns:", df.columns)

# =========================
# 2. Split Features & Target
# =========================
X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# =========================
# 3. Train-Test Split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# =========================
# 4. Train Model
# =========================
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# 5. Evaluate Model
# =========================
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# =========================
# 6. Save Model
# =========================
os.makedirs("model", exist_ok=True)

with open("model/diagnosis_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully in model/diagnosis_model.pkl")
