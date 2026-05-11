import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# -----------------------------
# LOAD MODEL
# -----------------------------

model = load_model('../models/moisture_predictor_lstm_v1.keras')

scaler = MinMaxScaler()

# Fake fit for consistent dimensions
scaler.fit([
    [0, 0, 0, 0],
    [100, 50, 100, 4000]
])

# -----------------------------
# PREDICTION FUNCTION
# -----------------------------

sequence_buffer = []

def predict_environment(data):
    global sequence_buffer

    current = [
        data['soilMoisture'],
        data['temperature'],
        data['humidity'],
        data['lightIntensity']
    ]

    normalized = scaler.transform([current])[0]

    sequence_buffer.append(normalized)

    # Keep only latest 10
    if len(sequence_buffer) > 10:
        sequence_buffer.pop(0)

    # Not enough data yet
    if len(sequence_buffer) < 10:
        data['predicted_moisture'] = data['soilMoisture']
        return data

    sequence = np.array([sequence_buffer])

    prediction = model.predict(sequence, verbose=0)

    predicted_moisture_normalized = prediction[0][0]

    # Reverse normalization manually
    predicted_moisture = predicted_moisture_normalized * 100

    data['predicted_moisture'] = round(predicted_moisture, 2)

    return data