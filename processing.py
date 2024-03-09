# Amir Abu Hani
# Second File
import json

from api_request import data

neo_data = []


def process_data():
    for date, neo_list in data["near_earth_objects"].items():
        for neo in neo_list:
            neo_id = neo["id"]
            name = neo["name"]
            estimated_diameter_min_km = neo["estimated_diameter"]["kilometers"]["estimated_diameter_min"]
            estimated_diameter_max_km = neo["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
            miss_distance_km = float(neo["close_approach_data"][0]["miss_distance"]["kilometers"])
            relative_velocity_kmh = float(neo["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"])

            neo_data.append({
                "id": neo_id,
                "name": name,
                "estimated_diameter_min_km": estimated_diameter_min_km,
                "estimated_diameter_max_km": estimated_diameter_max_km,
                "miss_distance_km": miss_distance_km,
                "relative_velocity_kmh": relative_velocity_kmh
            })

    # Write the extracted data to a file
    with open("neo_data.json", "w") as file:
        json.dump(neo_data, file, indent=4)


process_data()
