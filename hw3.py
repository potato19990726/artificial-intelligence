import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Define input variables
traffic_congestion = ctrl.Antecedent(np.arange(0, 101, 1), 'traffic_congestion')
road_condition = ctrl.Antecedent(np.arange(0, 101, 1), 'road_condition')
visibility = ctrl.Antecedent(np.arange(0, 1001, 1), 'visibility')
leading_vehicle_distance = ctrl.Antecedent(np.arange(0, 201, 1), 'leading_vehicle_distance')
crosswind_speed = ctrl.Antecedent(np.arange(0, 31, 1), 'crosswind_speed')
road_curvature = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'road_curvature')
lane_count = ctrl.Antecedent(np.arange(0, 6, 1), 'lane_count')

# Define output variable
speed = ctrl.Consequent(np.arange(0, 121, 1), 'speed')

# Define fuzzy sets
traffic_congestion['low'] = fuzz.gaussmf(traffic_congestion.universe, 0, 10)
traffic_congestion['medium'] = fuzz.gaussmf(traffic_congestion.universe, 50, 15)
traffic_congestion['high'] = fuzz.gaussmf(traffic_congestion.universe, 100, 10)

road_condition['dry'] = fuzz.gaussmf(road_condition.universe, 0, 5)
road_condition['wet'] = fuzz.gaussmf(road_condition.universe, 50, 15)
road_condition['very_wet'] = fuzz.gaussmf(road_condition.universe, 100, 5)

visibility['poor'] = fuzz.gaussmf(visibility.universe, 0, 100)
visibility['moderate'] = fuzz.gaussmf(visibility.universe, 500, 150)
visibility['good'] = fuzz.gaussmf(visibility.universe, 1000, 100)

leading_vehicle_distance['close'] = fuzz.gaussmf(leading_vehicle_distance.universe, 0, 5)
leading_vehicle_distance['medium'] = fuzz.gaussmf(leading_vehicle_distance.universe, 100, 30)
leading_vehicle_distance['far'] = fuzz.gaussmf(leading_vehicle_distance.universe, 200, 5)

crosswind_speed['weak'] = fuzz.gaussmf(crosswind_speed.universe, 0, 2)
crosswind_speed['moderate'] = fuzz.gaussmf(crosswind_speed.universe, 15, 4)
crosswind_speed['strong'] = fuzz.gaussmf(crosswind_speed.universe, 30, 2)

road_curvature['straight'] = fuzz.gaussmf(road_curvature.universe, 0, 0.005)
road_curvature['slight_curve'] = fuzz.gaussmf(road_curvature.universe, 0.5, 0.2)
road_curvature['sharp_curve'] = fuzz.gaussmf(road_curvature.universe, 1, 0.005)

lane_count['single'] = fuzz.gaussmf(lane_count.universe, 1, 0.5)
lane_count['double'] = fuzz.gaussmf(lane_count.universe, 2, 0.5)
lane_count['multiple'] = fuzz.gaussmf(lane_count.universe, 4, 0.5)

speed['slow'] = fuzz.gaussmf(speed.universe, 0, 20)
speed['medium'] = fuzz.gaussmf(speed.universe, 60, 20)
speed['fast'] = fuzz.gaussmf(speed.universe, 120, 20)

# Define fuzzy rules
rule1 = ctrl.Rule(traffic_congestion['high'] & road_condition['very_wet'] & visibility['poor'], speed['slow'])
rule2 = ctrl.Rule(traffic_congestion['medium'] & road_condition['wet'] & leading_vehicle_distance['medium'], speed['medium'])
rule3 = ctrl.Rule(traffic_congestion['low'] & road_condition['dry'] & visibility['good'], speed['fast'])
rule4 = ctrl.Rule(leading_vehicle_distance['close'] & road_curvature['sharp_curve'], speed['slow'])
rule5 = ctrl.Rule(crosswind_speed['strong'] & road_curvature['slight_curve'], speed['medium'])
rule6 = ctrl.Rule(visibility['good'] & traffic_congestion['low'] & lane_count['multiple'], speed['fast'])
rule7 = ctrl.Rule(crosswind_speed['moderate'] & leading_vehicle_distance['far'], speed['medium'])
rule8 = ctrl.Rule(road_curvature['straight'] & visibility['moderate'] & traffic_congestion['medium'], speed['medium'])
rule9 = ctrl.Rule(leading_vehicle_distance['far'] & road_condition['dry'], speed['fast'])
rule10 = ctrl.Rule(visibility['poor'] & traffic_congestion['high'], speed['slow'])

# Create control system
speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])

# Create simulator
speed_simulation = ctrl.ControlSystemSimulation(speed_ctrl)

# Set input values
speed_simulation.input['traffic_congestion'] = 30
speed_simulation.input['road_condition'] = 20
speed_simulation.input['visibility'] = 600
speed_simulation.input['leading_vehicle_distance'] = 40
speed_simulation.input['crosswind_speed'] = 7
speed_simulation.input['road_curvature'] = 0.03
speed_simulation.input['lane_count'] = 2

# Calculate output
speed_simulation.compute()

print(f"Recommended speed: {speed_simulation.output['speed']:.2f} km/h")

# Plot results
plt.figure(figsize=(20, 15))

plt.subplot(3, 3, 1)
plt.plot(traffic_congestion.universe, traffic_congestion['low'].mf)
plt.plot(traffic_congestion.universe, traffic_congestion['medium'].mf)
plt.plot(traffic_congestion.universe, traffic_congestion['high'].mf)
plt.title('Traffic Congestion')

plt.subplot(3, 3, 2)
plt.plot(road_condition.universe, road_condition['dry'].mf)
plt.plot(road_condition.universe, road_condition['wet'].mf)
plt.plot(road_condition.universe, road_condition['very_wet'].mf)
plt.title('Road Condition')

plt.subplot(3, 3, 3)
plt.plot(visibility.universe, visibility['poor'].mf)
plt.plot(visibility.universe, visibility['moderate'].mf)
plt.plot(visibility.universe, visibility['good'].mf)
plt.title('Visibility')

plt.subplot(3, 3, 4)
plt.plot(leading_vehicle_distance.universe, leading_vehicle_distance['close'].mf)
plt.plot(leading_vehicle_distance.universe, leading_vehicle_distance['medium'].mf)
plt.plot(leading_vehicle_distance.universe, leading_vehicle_distance['far'].mf)
plt.title('Leading Vehicle Distance')

plt.subplot(3, 3, 5)
plt.plot(crosswind_speed.universe, crosswind_speed['weak'].mf)
plt.plot(crosswind_speed.universe, crosswind_speed['moderate'].mf)
plt.plot(crosswind_speed.universe, crosswind_speed['strong'].mf)
plt.title('Crosswind Speed')

plt.subplot(3, 3, 6)
plt.plot(road_curvature.universe, road_curvature['straight'].mf)
plt.plot(road_curvature.universe, road_curvature['slight_curve'].mf)
plt.plot(road_curvature.universe, road_curvature['sharp_curve'].mf)
plt.title('Road Curvature')

plt.subplot(3, 3, 7)
plt.plot(lane_count.universe, lane_count['single'].mf)
plt.plot(lane_count.universe, lane_count['double'].mf)
plt.plot(lane_count.universe, lane_count['multiple'].mf)
plt.title('Lane Count')

plt.subplot(3, 3, 8)
plt.plot(speed.universe, speed['slow'].mf)
plt.plot(speed.universe, speed['medium'].mf)
plt.plot(speed.universe, speed['fast'].mf)
plt.title('Recommended Speed')

plt.tight_layout()
plt.show()
