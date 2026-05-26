from fastapi import FastAPI

from input.validator import validate_input
from prediction.predictor import predict_environment
from decision.fuzzy_engine import run_fuzzy
from output.formatter import format_output

app = FastAPI()


@app.post("/predict")
def predict(payload: list):

    try:

        validated_history = validate_input(payload)

        # Returns ONLY current row combined with predicted moisture
        predicted_environment = predict_environment(validated_history)

        # FUZZY DECISION
        command_percentage = run_fuzzy(predicted_environment)

        # REASON PLACEHOLDER
        reason = []

        return format_output(
            command_percentage,
            predicted_environment,
            reason
        )

    except Exception as e:

        return {
            "error": str(e)
        }