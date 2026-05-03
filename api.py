from fastapi import FastAPI
from input.validator import validate_input
from prediction.predictor import predict_environment
from decision.fuzzy_engine import run_fuzzy
from output.formatter import format_output

app = FastAPI()


@app.post("/predict")
def predict(data: dict):
    try:
        validated = validate_input(data)
        predicted = predict_environment(validated)
        result = run_fuzzy(predicted)
        return format_output(result, data)

    except Exception as e:
        return {"error": str(e)}