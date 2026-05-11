import skfuzzy as fuzz

def define_memberships(current_moisture, predicted_moisture, temp, humidity, light, rain, irrigation):

    # Soil input
    current_moisture['very_low'] = fuzz.trimf(current_moisture.universe, [0, 0, 25])
    current_moisture['low'] = fuzz.trimf(current_moisture.universe, [15, 35, 50])
    current_moisture['medium'] = fuzz.trimf(current_moisture.universe, [45, 65, 80])
    current_moisture['high'] = fuzz.trimf(current_moisture.universe, [70, 100, 100])

    # Prediction input
    predicted_moisture['low'] = fuzz.trimf(predicted_moisture.universe, [0, 0, 35])
    predicted_moisture['medium'] = fuzz.trimf(predicted_moisture.universe, [30, 50, 70])
    predicted_moisture['high'] = fuzz.trimf(predicted_moisture.universe, [60, 100, 100])

    # Temperature input
    temp['low'] = fuzz.trimf(temp.universe, [0, 0, 20])
    temp['medium'] = fuzz.trimf(temp.universe, [15, 25, 35])
    temp['high'] = fuzz.trimf(temp.universe, [28, 40, 50])

    # Humidity input
    humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 40])
    humidity['medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
    humidity['high'] = fuzz.trimf(humidity.universe, [60, 100, 100])

    # Light input
    light['low'] = fuzz.trimf(light.universe, [0, 0, 800])
    light['medium'] = fuzz.trimf(light.universe, [600, 1400, 2200])
    light['high'] = fuzz.trimf(light.universe, [1800, 2868, 2868])

    # Rain input
    rain['low'] = fuzz.trimf(rain.universe, [0, 0, 40])
    rain['medium'] = fuzz.trimf(rain.universe, [30, 50, 70])
    rain['high'] = fuzz.trimf(rain.universe, [60, 100, 100])

    # Irrigation output
    irrigation['low'] = fuzz.trimf(irrigation.universe, [0, 0, 40])
    irrigation['medium'] = fuzz.trimf(irrigation.universe, [30, 50, 70])
    irrigation['high'] = fuzz.trimf(irrigation.universe, [60, 100, 100])