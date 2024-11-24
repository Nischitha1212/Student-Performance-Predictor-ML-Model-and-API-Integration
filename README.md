# Student-Performance-Predictor-ML-Model-and-API-Integration
The **Student Performance Predictor** forecasts future exam scores using past marks, attendance, and participation data. It uses a Random Forest model for accuracy and a FastAPI-based REST API for seamless integration. Ideal for educators to track progress, identify trends, and personalize learning strategies.

Plaintext
student-performance-predictor/
│
├── backend/                     # Backend API
│   ├── app.py                   # FastAPI app
│   ├── model/                   # Model storage
│   │   └── student_model.pkl    # Trained ML model
│   ├── requirements.txt         # Backend dependencies
│   └── student_data.csv         # Dataset
│
├── frontend/                    # Frontend app
│   ├── index.html               # Main HTML file
│   ├── styles.css               # CSS file for styling
│   └── script.js                # JavaScript for API connection
│
└── README.md                    # Project documentation

Setup
Prerequisites
1. Python 3.x
2. pip package manager

Backend Setup
1. Install the required dependencies for the backend:
   cd backend
   pip install -r requirements.txt
   
2. Train the machine learning model (optional if the model is already trained):
   python train_model.py

3. Start the FastAPI server:
   uvicorn app:app --reload

The API will be available at http://127.0.0.1:8000


Frontend Setup
1. Open the frontend/index.html file in your browser. The frontend app will allow users to input student data (marks, attendance, participation) and get predictions from the backend API.

2. Ensure the API URL in the frontend (script.js) matches the backend endpoint:
   const response = await fetch("http://127.0.0.1:8000/predict/", {
   
Testing the API
Use the following data format to test the API with Postman or any other API testing tool:

POST http://127.0.0.1:8000/predict/

{
  "marks": [60, 65, 70, 75, 80],
  "attendance": 85,
  "participation": 90
}

Model Description
The machine learning model uses Random Forest Regressor to predict the student's future exam marks based on the following features:

1. Marks from previous exams.
2. Attendance percentage.
3. Participation in activities.
The model is trained on a small dataset, which can be expanded with more data to improve accuracy.

Connecting Frontend and Backend
1. Start the backend:
   uvicorn backend/app:app --reload
2. Open frontend/index.html in your browser.

Deployment
To deploy this project:

Deploy the backend FastAPI app on any cloud service (e.g., AWS, Heroku, etc.).
Host the frontend on a static file server, or keep it integrated with the backend.

Contributions
Feel free to fork this project and submit pull requests. For issues, please open an issue in the repository.
