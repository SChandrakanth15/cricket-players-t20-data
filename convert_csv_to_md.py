import csv

# Read the CSV file
input_file = 't20.csv'
output_file = 'cricket_players.md'

with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Get the header row

    # Generate Markdown table
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for row in reader:
        markdown_table += "| " + " | ".join(row) + " |\n"

# Write the Markdown table to a file
with open(output_file, 'w') as md_file:
    md_file.write(markdown_table)
