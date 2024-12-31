import os
from pymongo import MongoClient

uri = "mongodb+srv://chandrakanth:chandrakanth1234@microservicecluster.l8r2t.mongodb.net/?retryWrites=true&w=majority&appName=microserviceCluster"
client = MongoClient(uri)
db = client["cricket_information"]
collection = db["t20"]

documents = collection.find({})

markdown_table = "| Player Name   | Matches | Runs | Wickets |\n"
markdown_table += "|--------------|---------|------|---------|\n"

for doc in documents:
    player_name = doc.get("player_name", "N/A")
    matches = doc.get("matches", 0)
    runs = doc.get("runs", 0)
    wickets = doc.get("wickets", 0)
    markdown_table += f"| {player_name:<12} | {matches:<7} | {runs:<4} | {wickets:<7} |\n"

# Write to players.md
with open("players.md", "w") as file:
    file.write(markdown_table)

print(markdown_table)
print("Generated players.md at:", os.path.abspath("players.md"))
