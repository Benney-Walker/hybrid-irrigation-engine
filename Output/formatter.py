def format_output(value):
    value = float(value)  # 🔥 convert numpy → native python

    if value < 40:
        label = "LOW"
    elif value < 70:
        label = "MEDIUM"
    else:
        label = "HIGH"

    return {
        "score": round(value, 2),
        "label": label
    }