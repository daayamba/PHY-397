{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOew5YNuYIMQ+ng+THpG0s+"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "MaWDNAliePky"
      },
      "outputs": [],
      "source": [
        "\n",
        "import numpy as np\n",
        "\n",
        "# Given parameters\n",
        "K = 0.1\n",
        "A = 1\n",
        "d = 0.1\n",
        "T_e = 300\n",
        "T_o = 500\n",
        "dt = 0.01\n",
        "t_final = 0.01\n",
        "\n",
        "# Initialize variables\n",
        "heat_inputs = np.linspace(0, 100, 11)  # Adjust the range of heat inputs as needed\n",
        "temperature_changes = []\n",
        "\n",
        "# Function to solve the differential equation for a given heat input\n",
        "def solve_heat_equation(heat_input):\n",
        "    time_points = [0]\n",
        "    temperature_points = [T_o]\n",
        "\n",
        "    for t in range(1, int(t_final/dt)+1):\n",
        "        dQdt = heat_input - K * A * (temperature_points[-1] - T_e) / d\n",
        "        delta_T = dQdt * dt\n",
        "        temperature_points.append(temperature_points[-1] + delta_T)\n",
        "        time_points.append(t * dt)\n",
        "\n",
        "    return temperature_points[-1] - T_o\n",
        "\n",
        "# Calculate temperature changes for different heat inputs\n",
        "for heat_input in heat_inputs:\n",
        "    temperature_change = solve_heat_equation(heat_input)\n",
        "    temperature_changes.append(temperature_change)\n",
        "\n",
        "# Plotting the results\n",
        "plt.plot(heat_inputs, temperature_changes)\n",
        "plt.xlabel('Heat Input (J)')\n",
        "plt.ylabel('Temperature Change (K)')\n",
        "plt.title('Temperature Change as a function of Heat Input')\n",
        "plt.show()\n",
        "\n",
        "# Calculate specific heat capacity (Cp/v) by extracting the slope of the plot\n",
        "slope = np.polyfit(heat_inputs, temperature_changes, 1)[0]\n",
        "specific_heat_capacity = slope / A\n",
        "print(f'Specific Heat Capacity (Cp/v): {specific_heat_capacity} J/(K*m^3)')"
      ]
    }
  ]
}