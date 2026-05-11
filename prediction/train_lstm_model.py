import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import EarlyStopping

df = pd.read_csv("../dataset/sensor_data.csv")

data = df[[
    'soil_moisture',
    'temperature',
    'humidity',
    'light_intensity'
]].values

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

sequence_length = 10

x = []
y = []

sessions = df['experiment_id'].unique()

for session in sessions:

    session_df = df[df['experiment_id'] == session]

    session_data = session_df[[
        'soil_moisture',
        'temperature',
        'humidity',
        'light_intensity'
    ]].values

    scaled_session = scaler.transform(session_data)

    for i in range(sequence_length, len(scaled_session)):
        x.append(scaled_session[i - sequence_length:i])

        # Predict future soil moisture
        y.append(scaled_session[i][0])

X = np.array(x)
y = np.array(y)

print(X.shape, y.shape)

# -----------------------------
# BUILD MODEL
# -----------------------------

model = Sequential([
    LSTM(64, input_shape=(X.shape[1], X.shape[2])),
    Dense(32, activation='relu'),
    Dense(1)
])

model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

model.summary()

# -----------------------------
# TRAIN MODEL
# -----------------------------

stopper = EarlyStopping(
    monitor='loss',
    patience=10,
    restore_best_weights=True
)

model.fit(
    X,
    y,
    epochs=100,
    batch_size=8,
    callbacks=[stopper]
)

# -----------------------------
# SAVE MODEL
# -----------------------------

model.save('../models/moisture_predictor_lstm_v1.keras')

print("\nLSTM model trained and saved successfully")