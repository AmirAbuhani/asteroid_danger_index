#Amir Abu Hani
# Fourth File
from processing import neo_data
import matplotlib.pyplot as plt


def calculate_danger_index(neo_data, A=1, B=1, C=1):
    danger_index_list = []

    for neo in neo_data:
        asteroid_name = neo["name"]
        avg_diameter = (neo["estimated_diameter_min_km"] + neo["estimated_diameter_max_km"]) / 2
        relative_speed = float(neo["relative_velocity_kmh"])
        miss_distance = float(neo["miss_distance_km"])

        danger_index = A * avg_diameter + B * relative_speed * (1 / (C * miss_distance))
        danger_index_list.append((asteroid_name, danger_index))

    return danger_index_list


# Calculate the danger index using default coefficients (A=1, B=1, C=1)
result = calculate_danger_index(neo_data)
print(result)
# Extract asteroid names and danger indices from the result
asteroid_names = [entry[0] for entry in result]
danger_indices = [entry[1] for entry in result]

# Plot asteroid names against danger indices
plt.figure(figsize=(12, 6))
plt.bar(asteroid_names, danger_indices)
plt.xlabel('Asteroid Name')
plt.ylabel('Danger Index')
plt.title('Danger Index of Asteroids')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

