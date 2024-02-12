import numpy as np

# Given parameters
K = 0.1
A = 1
d = 0.1
T_e = 300
T_o = 500
dt = 0.01
t_final = 0.01

# Initialize variables
heat_inputs = np.linspace(0, 100, 11)  # Adjust the range of heat inputs as needed
temperature_changes = []

# Function to solve the differential equation for a given heat input
def solve_heat_equation(heat_input):
    time_points = [0]
    temperature_points = [T_o]

    for t in range(1, int(t_final/dt)+1):
        dQdt = heat_input - K * A * (temperature_points[-1] - T_e) / d
        delta_T = dQdt * dt
        temperature_points.append(temperature_points[-1] + delta_T)
        time_points.append(t * dt)

    return temperature_points[-1] - T_o

# Calculate temperature changes for different heat inputs
for heat_input in heat_inputs:
    temperature_change = solve_heat_equation(heat_input)
    temperature_changes.append(temperature_change)

# Plotting the results
plt.plot(heat_inputs, temperature_changes)
plt.xlabel('Heat Input (J)')
plt.ylabel('Temperature Change (K)')
plt.title('Temperature Change as a function of Heat Input')
plt.show()

# Calculate specific heat capacity (Cp/v) by extracting the slope of the plot
slope = np.polyfit(heat_inputs, temperature_changes, 1)[0]
specific_heat_capacity = slope / A
print(f'Specific Heat Capacity (Cp/v): {specific_heat_capacity} J/(K*m^3)')
