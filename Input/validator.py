def validate_input(env):
    required = [
        "soilMoisture", "temperature",
        "humidity", "lightIntensity", "rainProbability"
    ]

    for key in required:
        if key not in env or env[key] is None:
            raise ValueError(f"Missing value for {key}")

    return env