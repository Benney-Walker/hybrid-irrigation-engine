from skfuzzy import control as ctrl

def get_rules(soil, temp, humidity, light, rain, irrigation):

    return [
        ctrl.Rule(soil['low'] & rain['low'], irrigation['high']),
        ctrl.Rule(rain['high'], irrigation['low']),
        ctrl.Rule(soil['very_low'] & temp['high'], irrigation['high']),
        ctrl.Rule(soil['medium'] & humidity['medium'], irrigation['medium']),
        ctrl.Rule(temp['low'] & soil['high'], irrigation['low']),
        ctrl.Rule(light['high'] & soil['low'], irrigation['high']),
    ]