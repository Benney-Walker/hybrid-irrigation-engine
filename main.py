from input.validator import validate_input
from prediction.predictor import predict_environment
from decision.fuzzy_engine import run_fuzzy
from output.formatter import format_output

def run_engine(data):
    validated = validate_input(data)
    predicted = predict_environment(validated)
    result = run_fuzzy(predicted)
    return format_output(result)

if __name__ == "__main__":
    sample = {
        "soilMoisture": 25,
        "temperature": 34,
        "humidity": 45,
        "lightIntensity": 700,
        "rainProbability": 10
    }

    print(run_engine(sample))