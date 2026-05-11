from skfuzzy import control as ctrl

def get_rules(current_moisture, predicted_moisture, temp, humidity, light, rain, irrigation):

    return [
        # Extremely dry soil → always irrigate
        ctrl.Rule(current_moisture['very_low'], irrigation['high']),

        # Dry soil + high sunlight → strong irrigation
        ctrl.Rule(current_moisture['low'] & light['high'], irrigation['high']),

        # Medium soil + high sunlight → moderate irrigation
        ctrl.Rule(current_moisture['medium'] & light['high'], irrigation['medium']),

        # Medium soil + low sunlight → low irrigation
        ctrl.Rule(current_moisture['medium'] & light['low'], irrigation['low']),

        # High soil → no irrigation
        ctrl.Rule(current_moisture['high'], irrigation['low'])
    ]