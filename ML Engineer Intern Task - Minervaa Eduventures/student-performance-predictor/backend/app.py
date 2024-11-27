from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

# FastAPI app
app = FastAPI()

# Load trained model
with open("model/student_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define request structure
class StudentData(BaseModel):
    marks: list
    attendance: float
    participation: float

# Predict endpoint
@app.post("/predict/")
async def predict(data: StudentData):
    input_data = np.array([data.marks + [data.attendance, data.participation]])
    predicted_score = model.predict(input_data)[0]
    return {"predicted_marks": predicted_score}
