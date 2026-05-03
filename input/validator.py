def validate_input(env):
    required = [
        "preparedDataId",
        "soilMoisture", "temperature",
        "humidity", "lightIntensity", "rainProbability"
    ]

    # --- VALIDATION ---
    for key in required:
        if key not in env or env[key] is None:
            raise ValueError(f"Missing value for {key}")

    # --- TYPE CHECK (optional but smart) ---
    numeric_fields = [
        "soilMoisture", "temperature",
        "humidity", "lightIntensity", "rainProbability"
    ]

    for field in numeric_fields:
        try:
            env[field] = float(env[field])
        except:
            raise ValueError(f"Invalid numeric value for {field}")

    # --- REMOVE ID BEFORE PROCESSING ---
    cleaned_env = {
        key: env[key]
        for key in env
        if key != "preparedDataId"
    }

    return cleaned_env