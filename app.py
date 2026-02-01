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
        selected_symptoms = request.form["symptoms"].split(",")


        # Create input vector
        input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]

        prediction = model.predict([input_data])[0]

        return render_template(
            "index.html",
            symptoms=symptoms,
            prediction=prediction
        )

    return render_template("index.html", symptoms=symptoms)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
