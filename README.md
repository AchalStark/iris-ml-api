# Iris Species Prediction API

## What the model predicts
Predicts the species of an iris flower (setosa, versicolor, or virginica)
from its sepal and petal measurements in centimeters.

## Endpoints
- `GET /health` returns the API status and whether the model loaded
- `POST /predict` returns a species prediction

## Example request
`POST /predict`

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Example response:

```json
{
  "prediction": 0,
  "species": "setosa"
}
```

## Run locally
```bash
git clone <your-repo-url>
cd <your-repo-name>
python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
Open http://localhost:8000/docs

## Live URL
https://iris-ml-api-g2jf.onrender.com
