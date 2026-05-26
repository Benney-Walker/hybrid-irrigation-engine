from input.validator import validate_input
from prediction.predictor import predict_environment
from decision.fuzzy_engine import run_fuzzy
from output.formatter import format_output


def run_engine(history):

    validated = validate_input(history)

    predicted = predict_environment(validated)

    result = run_fuzzy(predicted)

    reason = "nothing yet"

    return format_output(result, predicted, reason)


if __name__ == "__main__":

    # ---------------------------------
    # FAKE 10-STEP HISTORY FOR TESTING
    # Latest/current reading is FIRST
    # ---------------------------------

    sample_history = [

        {
            "preparedDataId": 1001,
            "soilMoisture": 68.42,
            "temperature": 31.62,
            "humidity": 30,
            "lightIntensity": 2681.67,
            "rainProbability": 15
        },

        {
            "preparedDataId": 1002,
            "soilMoisture": 68.59,
            "temperature": 31.56,
            "humidity": 31,
            "lightIntensity": 2670.00,
            "rainProbability": 15
        },

        {
            "preparedDataId": 1003,
            "soilMoisture": 68.77,
            "temperature": 31.44,
            "humidity": 31,
            "lightIntensity": 2687.50,
            "rainProbability": 15
        },

        {
            "preparedDataId": 1004,
            "soilMoisture": 68.9,
            "temperature": 31.31,
            "humidity": 31,
            "lightIntensity": 2662.50,
            "rainProbability": 15
        },

        {
            "preparedDataId": 1005,
            "soilMoisture": 69,
            "temperature": 31.19,
            "humidity": 31,
            "lightIntensity": 2692.50,
            "rainProbability": 15
        },

        {
            "preparedDataId": 1006,
            "soilMoisture": 69.2,
            "temperature": 31.06,
            "humidity": 31,
            "lightIntensity": 2710.83,
            "rainProbability": 15
        },

        {
            "preparedDataId": 1007,
            "soilMoisture": 69.40,
            "temperature": 30.94,
            "humidity": 31,
            "lightIntensity": 2734.17,
            "rainProbability": 15
        },

        {
            "preparedDataId": 1008,
            "soilMoisture": 69.65,
            "temperature": 30.75,
            "humidity": 32,
            "lightIntensity": 2757.50,
            "rainProbability": 15
        },

        {
            "preparedDataId": 1009,
            "soilMoisture": 69.85,
            "temperature": 30.62,
            "humidity": 33,
            "lightIntensity": 2778.33,
            "rainProbability": 15
        },

        {
            "preparedDataId": 1010,
            "soilMoisture": 70,
            "temperature": 30.50,
            "humidity": 35,
            "lightIntensity": 2788.33,
            "rainProbability": 15
        }

    ]

    print(run_engine(sample_history))