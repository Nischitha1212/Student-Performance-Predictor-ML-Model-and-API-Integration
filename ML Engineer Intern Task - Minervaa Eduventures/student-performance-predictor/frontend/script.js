const form = document.getElementById("predict-form");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const marks = document.getElementById("marks").value.split(",").map(Number);
    const attendance = parseFloat(document.getElementById("attendance").value);
    const participation = parseFloat(document.getElementById("participation").value);

    const response = await fetch("http://127.0.0.1:8000/predict/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ marks, attendance, participation }),
    });

    const result = await response.json();
    document.getElementById("result").innerText = `Predicted Marks: ${result.predicted_marks}`;
});
