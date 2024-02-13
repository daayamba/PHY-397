# PHY 397
# Submission of assignment
# Group members:
1. David Ayamba
2. Moses Kukubor
3. Benjamin Ofori
4. Joshua Odartei
5. Julius Blaboe
# Heat Transfer Simulation
This repository contains Python code for simulating heat transfer in a solid using a numerical approach. 
The simulation is based on a simple heat transfer equation, and it calculates the temperature of the solid over time.

# Table of Contents
Introduction

Requirements

Parameters

Results

# Introduction
The provided Python code simulates heat transfer in a solid using the Euler method. 

The heat transfer equation considers the thermal conductivity of the solid, surface area, thickness, and initial and external temperatures.

# Requirements
To run the code, you need:

Python (version 3.x)

Matplotlib (for plotting)


# Parameters
Adjust the parameters in the script to customize the simulation:

K: Thermal conductivity of the solid

A: Surface area of the solid

d: Thickness of the solid

T_e: External temperature

T_o: Initial temperature

dt: Time step for the simulation

t_final: Final time for the simulation

# Results
The script generates two plots:

# Temperature as a function of time: 
Observes how the temperature of the solid changes over the specified time period.

# Temperature Change as a function of Heat Input: 
Investigates the relationship between different heat inputs and the resulting temperature changes.

# The specific heat capacity (Cp/v) is calculated by extracting the slope of the second plot.
