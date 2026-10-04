from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Iris Species Prediction API")

CLASS_NAMES = ["setosa", "versicolor", "virginica"]

model = None
try:
    model = joblib.load("model.pkl")
except Exception as e:
    print(f"Model failed to load: {e}")


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict")
def predict(data: IrisInput):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    try:
        df = pd.DataFrame([data.model_dump()])
        pred = int(model.predict(df)[0])
        return {"prediction": pred, "species": CLASS_NAMES[pred]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))