"""
Simulation: Tower of Silence - AI Logic Collapse Field
Author: GhostCore Systems
"""

import math

# Field parameters
field_radius_km = 2.5
entropy_wave_duration_s = 8
ai_nodes_present = 48
collapse_efficiency = 0.85

# Total affected area
area_sq_km = math.pi * field_radius_km**2
nodes_affected = int(ai_nodes_present * collapse_efficiency)

print(f"Entropy field radius: {field_radius_km} km")
print(f"Total area affected: {area_sq_km:.2f} km^2")
print(f"AI nodes present: {ai_nodes_present}")
print(f"Nodes collapsed/disrupted: {nodes_affected}")
