from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model/diagnosis_model.pkl", "rb"))

# Load dataset columns (for symptom order)
df = pd.read_csv("data/dataset.csv")
symptoms = df.drop("prognosis", axis=1).columns.tolist()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        # Get selected symptoms (from guided UI)
        selected_symptoms = request.form["symptoms"].split(",")

        # Create input vector
        input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]

        # Predict disease
        prediction = model.predict([input_data])[0]

        # -------------------------
        # ADVICE MAPPING
        # -------------------------
        advice_map = {
            "Migraine": "If headaches persist beyond 48 hours or worsen, consult a doctor.",
            "Flu": "Take rest and fluids. Consult a doctor if fever lasts more than 3 days.",
            "Allergy": "Avoid known triggers. Seek medical advice if breathing difficulty occurs.",
            "Diabetes": "Consult a doctor for blood sugar testing and proper management.",
            "Common Cold": "Rest well. See a doctor if symptoms persist beyond a week."
        }

        advice = advice_map.get(
            prediction,
            "If symptoms persist or worsen, please consult a medical professional."
        )

        # -------------------------
        # EXPLANATION TEXT
        # -------------------------
        explanation = (
            "Based on the symptoms you selected, this condition is commonly observed "
            "in similar cases."
        )

        return render_template(
            "index.html",
            symptoms=symptoms,
            prediction=prediction,
            explanation=explanation,
            advice=advice
        )

    return render_template("index.html", symptoms=symptoms)


if __name__ == "__main__":
    app.run(debug=True,port=5000)
