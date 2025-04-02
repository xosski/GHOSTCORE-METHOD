"""
Simulation: Abaddon's Harrow Railgun Dynamics
Author: GhostCore Systems
"""

import math

# Constants
slug_mass_kg = 40  # Dense tungsten slug
target_distance_km = 1000  # From orbital platform
rail_length_m = 80
energy_input_mj = 3500  # Megajoules per shot

# Convert MJ to J
energy_input_j = energy_input_mj * 1e6

# Calculate theoretical velocity from E = 1/2 m v^2
velocity_mps = math.sqrt(2 * energy_input_j / slug_mass_kg)

# Time to target assuming vacuum
time_to_impact = (target_distance_km * 1000) / velocity_mps

# Impact kinetic energy
kinetic_energy_mj = 0.5 * slug_mass_kg * velocity_mps**2 / 1e6

print(f"Slug velocity: {velocity_mps:.2f} m/s")
print(f"Time to impact: {time_to_impact:.2f} s")
print(f"Impact kinetic energy: {kinetic_energy_mj:.2f} MJ")
