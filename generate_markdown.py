import os
from pymongo import MongoClient

# MongoDB connection URI (use environment variable for security)
uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")  # Default for local testing
client = MongoClient(uri)

# Database and collection
db = client["cricket_information"]
collection = db["t20"]

# Fetch player data
documents = collection.find({})  # Retrieve all documents

# Generate Markdown table
markdown_table = "| Player Name   | Matches | Runs | Wickets |\n"
markdown_table += "|--------------|---------|------|---------|\n"

for doc in documents:
    player_name = doc.get("player_name", "N/A")
    matches = doc.get("matches", 0)
    runs = doc.get("runs", 0)
    wickets = doc.get("wickets", 0)
    markdown_table += f"| {player_name:<12} | {matches:<7} | {runs:<4} | {wickets:<7} |\n"

# Write Markdown table to a file
output_file = "players.md"
with open(output_file, "w") as f:
    f.write(markdown_table)

# Debugging output
print("Generated players.md at:", os.path.abspath(output_file))
