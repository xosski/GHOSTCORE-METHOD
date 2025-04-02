"""
Simulation: WraithHalo EMP + Cloaking Field
Author: GhostCore Systems
"""

import math

# Constants
radius_km = 5
duration_s = 10
em_peak_mw = 800  # Peak EMP burst (megawatts)
cloak_efficiency = 0.93  # Cloaking probability

# Area coverage (assuming circular projection)
area_sq_km = math.pi * radius_km**2
energy_total_mj = em_peak_mw * duration_s  # Total energy in MJ

# Effective system disruption
system_disruption_index = cloak_efficiency * energy_total_mj / area_sq_km

print(f"Field radius: {radius_km} km")
print(f"Field area: {area_sq_km:.2f} km^2")
print(f"Total energy output: {energy_total_mj} MJ")
print(f"System disruption index: {system_disruption_index:.2f}")
