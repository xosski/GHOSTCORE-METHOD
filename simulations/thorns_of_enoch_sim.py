"""
Simulation: Thorns of Enoch Plasma Swarm Strike
Author: GhostCore Systems
"""

import random

# Swarm parameters
total_darts = 72
hit_probability = 0.88
plasma_penetration_mj = 0.45
total_hits = 0
total_energy = 0.0

for i in range(total_darts):
    if random.random() <= hit_probability:
        total_hits += 1
        total_energy += plasma_penetration_mj

print(f"Total darts fired: {total_darts}")
print(f"Effective hits: {total_hits}")
print(f"Total penetration energy delivered: {total_energy:.2f} MJ")
