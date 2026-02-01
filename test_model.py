import pickle
import pandas as pd

# =========================
# 1. Load Model
# =========================
with open("model/diagnosis_model.pkl", "rb") as file:
    model = pickle.load(file)

# =========================
# 2. Load Dataset (for column order)
# =========================
df = pd.read_csv("data/dataset.csv")
X = df.drop("prognosis", axis=1)

# =========================
# 3. Create Sample Input
# =========================
# Take first row as test input
sample_input = X.iloc[0].values.reshape(1, -1)

# =========================
# 4. Predict Disease
# =========================
prediction = model.predict(sample_input)

print("Predicted Disease:", prediction[0])
