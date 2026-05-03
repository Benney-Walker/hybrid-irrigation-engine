import skfuzzy as fuzz

def define_memberships(soil, temp, humidity, light, rain, irrigation):

    # Soil input
    soil['very_low'] = fuzz.trimf(soil.universe, [0, 0, 20])
    soil['low'] = fuzz.trimf(soil.universe, [10, 30, 50])
    soil['medium'] = fuzz.trimf(soil.universe, [40, 60, 80])
    soil['high'] = fuzz.trimf(soil.universe, [70, 100, 100])

    # Temperature input
    temp['low'] = fuzz.trimf(temp.universe, [0, 0, 20])
    temp['medium'] = fuzz.trimf(temp.universe, [15, 25, 35])
    temp['high'] = fuzz.trimf(temp.universe, [28, 40, 50])

    # Humidity input
    humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 40])
    humidity['medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
    humidity['high'] = fuzz.trimf(humidity.universe, [60, 100, 100])

    # Light input
    light['low'] = fuzz.trimf(light.universe, [0, 0, 300])
    light['medium'] = fuzz.trimf(light.universe, [200, 500, 800])
    light['high'] = fuzz.trimf(light.universe, [700, 1000, 1000])

    # Rain input
    rain['low'] = fuzz.trimf(rain.universe, [0, 0, 40])
    rain['medium'] = fuzz.trimf(rain.universe, [30, 50, 70])
    rain['high'] = fuzz.trimf(rain.universe, [60, 100, 100])

    # Irrigation output
    irrigation['low'] = fuzz.trimf(irrigation.universe, [0, 0, 40])
    irrigation['medium'] = fuzz.trimf(irrigation.universe, [30, 50, 70])
    irrigation['high'] = fuzz.trimf(irrigation.universe, [60, 100, 100])