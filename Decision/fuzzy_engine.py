import numpy as np
from skfuzzy import control as ctrl
from Decision.membership import define_memberships
from Decision.rules import get_rules

def run_fuzzy(env):

    # Variables
    soil = ctrl.Antecedent(np.arange(0, 101, 1), 'soilMoisture')
    temp = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')
    humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
    light = ctrl.Antecedent(np.arange(0, 1001, 1), 'lightIntensity')
    rain = ctrl.Antecedent(np.arange(0, 101, 1), 'rainProbability')

    irrigation = ctrl.Consequent(np.arange(0, 101, 1), 'irrigation')

    # Membership
    define_memberships(soil, temp, humidity, light, rain, irrigation)

    # Rules
    rules = get_rules(soil, temp, humidity, light, rain, irrigation)

    # System
    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    # Inputs
    sim.input['soilMoisture'] = env["soilMoisture"]
    sim.input['temperature'] = env["temperature"]
    sim.input['humidity'] = env["humidity"]
    sim.input['lightIntensity'] = env["lightIntensity"]
    sim.input['rainProbability'] = env["rainProbability"]

    sim.compute()

    return sim.output['irrigation']