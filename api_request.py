# Amir Abu Hani
# First File
import requests
import json

response = requests.get(
    "https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-03-09&end_date=&api_key=ylyzLvKsEVootebLSik1u8UvdYDjHWSLx5weM1WX")
response.raise_for_status()

data = response.json()

with open("results.json", "w") as file:
    json.dump(data, file, indent=4)
