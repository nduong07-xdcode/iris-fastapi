from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib

model = joblib.load("svm_model.pkl")

app = FastAPI(
    title= "IRIS SVM API",
    description= "xu ly va phan loai hoa qua mo hinh svm",
    version= "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

species = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}

@app.get("/")
def home():
    return {"message": " IRIS SVM API is running one"}
 

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: IrisInput):
    features = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width,
    ]]
    
    prediction = int(model.predict(features)[0])

    return {
        "class_id": prediction,
        "prediction": species[prediction],
    }
