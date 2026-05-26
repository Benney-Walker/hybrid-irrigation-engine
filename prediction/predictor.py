import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler

# -----------------------------
# LOAD MODEL
# -----------------------------

model = load_model('models/moisture_predictor_lstm_v2.keras')

# -----------------------------
# SCALER
# -----------------------------

scaler = MinMaxScaler()

# Fake fit for consistent dimensions
scaler.fit([
    [0, 0, 0, 0],
    [100, 50, 100, 4000]
])

# -----------------------------
# PREDICTION FUNCTION
# -----------------------------

def predict_environment(history):

    # -----------------------------
    # BUILD NORMALIZED SEQUENCE
    # -----------------------------

    sequence = []

    for row in history:

        values = [
            row['soilMoisture'],
            row['temperature'],
            row['humidity'],
            row['lightIntensity']
        ]

        normalized = scaler.transform([values])[0]

        sequence.append(normalized)

    # -----------------------------
    # CONVERT TO LSTM INPUT SHAPE
    # -----------------------------

    sequence = np.array([sequence])

    # Shape becomes:
    # (1, sequence_length, 4)

    # -----------------------------
    # PREDICT FUTURE MOISTURE
    # -----------------------------

    prediction = model.predict(sequence, verbose=0)

    predicted_moisture_normalized = prediction[0][0]

    # Reverse normalization
    predicted_moisture = predicted_moisture_normalized * 100

    # -----------------------------
    # RETURN CURRENT ROW
    # WITH PREDICTION ADDED
    # -----------------------------

    current_data = history[0]

    current_data['predicted_moisture'] = round(predicted_moisture, 2)

    print(current_data)

    return current_data