import requests
import pandas as pd

data_list = []

# Loop through first 10 Star Wars characters using new API
for i in range(1, 10 + 1):
    url = f"https://swapi.py4e.com/api/people/{i}/"
    response = requests.get(url)
    response.raise_for_status()   # better safety
    data = response.json()

    data_list.append({
        "Name": data.get("name"),
        "Height": data.get("height"),
        "Mass": data.get("mass"),
        "Gender": data.get("gender")
    })

# Convert to DataFrame
df = pd.DataFrame(data_list)

# Save to CSV file
df.to_csv("swapi_data.csv", index=False)
print("Star Wars data collected successfully using NEW API!")
print(df.head())