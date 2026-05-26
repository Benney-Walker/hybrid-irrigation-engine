def format_output(value, env, reason):

    return {

        "preparedDataId": int(env["preparedDataId"]),

        # Convert NumPy values to normal Python float
        "commandPercentage": round(float(value), 2),

        "reason": reason
    }