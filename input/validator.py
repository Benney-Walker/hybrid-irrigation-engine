def validate_input(history):

    required = [
        "preparedDataId",
        "soilMoisture",
        "temperature",
        "humidity",
        "lightIntensity",
        "rainProbability"
    ]

    numeric_fields = [
        "soilMoisture",
        "temperature",
        "humidity",
        "lightIntensity",
        "rainProbability"
    ]

    # -----------------------------
    # VALIDATE EACH ROW
    # -----------------------------

    for index, row in enumerate(history):

        # --- REQUIRED FIELD CHECK ---
        for key in required:

            if key not in row or row[key] is None:
                raise ValueError(
                    f"Missing value for '{key}' in row {index}"
                )

        # --- NUMERIC VALIDATION ---
        for field in numeric_fields:

            try:
                row[field] = float(row[field])

            except:
                raise ValueError(
                    f"Invalid numeric value for '{field}' in row {index}"
                )

    # -----------------------------
    # RETURN ORIGINAL STRUCTURE
    # -----------------------------

    return history