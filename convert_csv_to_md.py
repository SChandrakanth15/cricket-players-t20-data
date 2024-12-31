import csv

# Relative path to the CSV file
input_file = 't20.csv'

# Read the CSV file
with open(input_file, 'r') as t20_csv_file:
    reader = csv.reader(t20_csv_file)
    headers = next(reader)  # Get the header row

    # Create the table header
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    # Create the table rows
    for row in reader:
        markdown_table += "| " + " | ".join(row) + " |\n"

# Write the Markdown table to stdout
print(markdown_table)
