from skfuzzy import control as ctrl


def get_rules(current_moisture,
              predicted_moisture,
              temp,
              humidity,
              light,
              rain,
              irrigation):

    return [

        # Very dry soil but rain expected
        ctrl.Rule(
            current_moisture['very_low'] & rain['high'],
            irrigation['medium']
        ),

        # Moderate irrigation conditions
        ctrl.Rule(
            (
                (current_moisture['low'] & rain['low']) |
                (rain['medium'] & light['low']) |
                (temp['medium']) |
                (temp['low'] & humidity['medium']) |
                (humidity['high'])
            ),
            irrigation['medium']
        ),

        # Low irrigation conditions
        ctrl.Rule(
            (
                (current_moisture['low'] & light['low']) |
                (temp['low'] & humidity['high'])
            ),
            irrigation['low']
        ),

        # High irrigation conditions
        ctrl.Rule(
            (
                (current_moisture['low'] & light['high']) |
                (temp['high'] & predicted_moisture['low'])
            ),
            irrigation['high']
        ),

        # Medium soil + strong sunlight
        ctrl.Rule(
            current_moisture['medium'] & light['high'],
            irrigation['medium']
        ),

        # Medium soil + weak sunlight
        ctrl.Rule(
            current_moisture['medium'] & light['low'],
            irrigation['low']
        ),

        # High moisture
        ctrl.Rule(
            current_moisture['high'],
            irrigation['low']
        )
    ]