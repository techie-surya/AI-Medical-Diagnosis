// -----------------------------
// MAJOR → MINOR SYMPTOM MAP
// -----------------------------
const symptomMap = {
    fever: [
        "high_fever",
        "chills",
        "sweating",
        "fatigue",
        "body_pain"
    ],
    headache: [
        "headache",
        "nausea",
        "dizziness",
        "blurred_vision"
    ],
    cough: [
        "cough",
        "runny_nose",
        "sore_throat",
        "chest_pain"
    ],
    stomach: [
        "stomach_pain",
        "vomiting",
        "diarrhoea",
        "loss_of_appetite"
    ],
    skin: [
        "itching",
        "skin_rash",
        "red_spots",
        "blisters"
    ]
};

// store selected minor symptoms
let selectedSymptoms = new Set();

// -----------------------------
// SHOW MINOR SYMPTOMS
// -----------------------------
function showMinorSymptoms(category) {
    const container = document.getElementById("minorSymptoms");
    container.innerHTML = "";

    symptomMap[category].forEach(symptom => {
        const label = document.createElement("label");
        label.className = "symptom-item";

        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.value = symptom;

        checkbox.addEventListener("change", function () {
            if (this.checked) {
                selectedSymptoms.add(symptom);
                label.style.background = "#d6ebff";
            } else {
                selectedSymptoms.delete(symptom);
                label.style.background = "#f1f1f1";
            }

            document.getElementById("selectedSymptoms").value =
                Array.from(selectedSymptoms).join(",");
        });

        label.appendChild(checkbox);
        label.appendChild(document.createTextNode(
            symptom.replace("_", " ").toUpperCase()
        ));

        container.appendChild(label);
    });
}

// -----------------------------
// FORM VALIDATION
// -----------------------------
document.querySelector("form").addEventListener("submit", function (e) {
    if (selectedSymptoms.size === 0) {
        e.preventDefault();
        alert("Please select at least one symptom.");
    }
});
