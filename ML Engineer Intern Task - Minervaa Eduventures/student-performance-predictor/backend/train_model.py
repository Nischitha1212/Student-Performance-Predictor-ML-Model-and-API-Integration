import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Create a dataset
data = {
    "exam_1": [60, 50, 70, 80, 90],
    "exam_2": [65, 55, 75, 85, 95],
    "exam_3": [70, 60, 80, 90, 100],
    "exam_4": [75, 65, 85, 95, 105],
    "exam_5": [80, 70, 90, 100, 110],
    "attendance": [85, 80, 90, 95, 100],
    "participation": [90, 70, 80, 85, 95],
    "exam_10": [85, 75, 95, 105, 115],
}
df = pd.DataFrame(data)

# Split data
X = df.drop(columns=["exam_10"])
y = df["exam_10"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
with open("model/student_model.pkl", "wb") as f:
    pickle.dump(model, f)
