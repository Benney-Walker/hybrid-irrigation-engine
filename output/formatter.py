def format_output(value, env):
    value = float(value)

    # --- DECISION ---
    if value < 30:
        decision = "NO_IRRIGATION"
    elif value < 60:
        decision = "DELAY"
    else:
        decision = "IRRIGATE"

    # --- WATER QUANTITY (simple mapping for now) ---
    water_quantity = int((value / 100) * 100)  # scale to liters (adjust later)

    # --- CONFIDENCE ---
    confidence = int(value)  # use score as confidence for now

    # --- REASONING ---
    reasons = []

    if env["soilMoisture"] < 40:
        reasons.append("Soil moisture is low")

    if env["temperature"] > 30:
        reasons.append("Temperature is high")

    if env["rainProbability"] > 60:
        reasons.append("High probability of rain")

    if env["humidity"] < 40:
        reasons.append("Low humidity increases evaporation")

    if env["lightIntensity"] > 700:
        reasons.append("High sunlight increases water loss")

    decision_reason = ", ".join(reasons)

    return {
        "preparedDataId": env["preparedDataId"],
        "decision": decision,
        "waterQuantity": water_quantity,
        "confidence": confidence,
        "decisionReason": decision_reason
    }