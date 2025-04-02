"""
Simulation: The Cross - Overcharged Photon Cannon
Author: GhostCore Systems
"""

# Beam parameters
beam_energy_mj = 1250.0  # Megajoules per discharge
pulse_duration_ms = 950
radiation_surge_multiplier = 1.45

# Output calculations
thermal_output = beam_energy_mj * 0.65
radiation_output = beam_energy_mj * 0.35 * radiation_surge_multiplier

print("=== Firing The Cross ===")
print(f"Total beam energy: {beam_energy_mj:.2f} MJ")
print(f"Thermal output: {thermal_output:.2f} MJ")
print(f"Radiation surge: {radiation_output:.2f} MJ")
