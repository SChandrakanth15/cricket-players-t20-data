from pymongo import MongoClient

# MongoDB connection URI
uri = "mongodb+srv://chandrakanth:chandrakanth1234@microservicecluster.l8r2t.mongodb.net/?retryWrites=true&w=majority&appName=microserviceCluster"

# Connect to MongoDB
client = MongoClient(uri)
db = client["cricket_information"]  # Database name
collection = db["t20"]  # Collection name

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

# Print Markdown table
print(markdown_table)
