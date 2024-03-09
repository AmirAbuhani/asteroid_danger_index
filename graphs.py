#Amir Abu Hani
# Third File
import matplotlib.pyplot as plt
from processing import neo_data


def min_diameter_velocity():
    # Extract minimum diameter and relative velocity data
    diameters = [neo["estimated_diameter_min_km"] for neo in neo_data]
    velocities = [neo["relative_velocity_kmh"] for neo in neo_data]

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(diameters, velocities, alpha=0.5)
    plt.title("Relation between Minimum Diameter and Relative Velocity")
    plt.xlabel("Minimum Diameter(km)")
    plt.ylabel("Relative Velocity(km/h)")
    plt.grid(True)
    plt.show()


def miss_distance_max_diameter():
    miss_distances = [neo["miss_distance_km"] for neo in neo_data]
    max_diameters = [neo["estimated_diameter_max_km"] for neo in neo_data]

    plt.figure(figsize=(10, 6))
    plt.scatter(max_diameters, miss_distances, alpha=0.5)
    plt.title("Relation between Miss Distance and Max Diameter")
    plt.xlabel("Max Diameter(km)")
    plt.ylabel("Miss Distance(millions of km)")
    plt.grid(True)
    plt.show()


min_diameter_velocity()
miss_distance_max_diameter()
