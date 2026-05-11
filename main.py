from input.validator import validate_input
from prediction.predictor import predict_environment
from decision.fuzzy_engine import run_fuzzy
from output.formatter import format_output

def run_engine(data):
    validated = validate_input(data)
    predicted = predict_environment(validated)
    result = run_fuzzy(predicted)
    return format_output(result, data)

if __name__ == "__main__":
    sample = {
        "preparedDataId":123456,
        "soilMoisture": 49,
        "temperature": 37,
        "humidity": 37,
        "lightIntensity": 200,
        "rainProbability": 100
    }

    print(run_engine(sample))