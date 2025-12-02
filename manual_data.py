import os
import requests
import pandas as pd

# Fetch 10 random users from API
url = "https://randomuser.me/api/?results=10"
response = requests.get(url)
response.raise_for_status()

data = response.json()

# Extract useful fields
records = []
for user in data["results"]:
    records.append({
        "name": f"{user['name']['first']} {user['name']['last']}",
        "age": user["dob"]["age"],
        "gender": user["gender"],
        "country": user["location"]["country"],
        "email": user["email"]
    })

df = pd.DataFrame(records)

# Save to folder
os.makedirs("data", exist_ok=True)
df.to_csv("data/api_generated_data.csv", index=False)

print("API Data Fetched & Saved Successfully!")
print(df.head())