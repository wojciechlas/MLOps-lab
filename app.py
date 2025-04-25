from fastapi import FastAPI
import inference
from api.models.iris import PredictResponse, PredictRequest

app = FastAPI()

model = inference.load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the MLOps Lab!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    """
    Predict the class of the iris flower based on the input features.
    """
    prediction = inference.predict(model, request.dict())
    return PredictResponse(prediction=prediction)
