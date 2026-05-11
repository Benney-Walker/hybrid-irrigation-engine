import numpy as np
from skfuzzy import control as ctrl
from decision.membership import define_memberships
from decision.rules import get_rules

def run_fuzzy(env):

    # Variables
    current_moisture = ctrl.Antecedent(np.arange(0, 101, 1), 'soilMoisture')
    predicted_moisture = ctrl.Consequent(np.arange(0, 101, 1), 'predicted_moisture')
    temp = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
    humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
    light = ctrl.Antecedent(np.arange(0, 3000, 1), 'lightIntensity')
    rain = ctrl.Antecedent(np.arange(0, 101, 1), 'rainProbability')

    irrigation = ctrl.Consequent(np.arange(0, 101, 1), 'irrigation')

    # Membership
    define_memberships(current_moisture, predicted_moisture, temp, humidity, light, rain, irrigation)

    # Rules
    rules = get_rules(current_moisture, predicted_moisture, temp, humidity, light, rain, irrigation)

    # System
    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    # Inputs
    sim.input['soilMoisture'] = env["soilMoisture"]
    sim.input['predicted_moisture'] = env["predicted_moisture"]
    sim.input['temperature'] = env["temperature"]
    sim.input['humidity'] = env["humidity"]
    sim.input['lightIntensity'] = env["lightIntensity"]
    sim.input['rainProbability'] = env["rainProbability"]

    sim.compute()

    return sim.output['irrigation']