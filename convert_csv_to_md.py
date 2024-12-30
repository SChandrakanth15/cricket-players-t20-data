import csv

# Read the CSV file
input_file = 't20.csv'
output_file = 'cricket_players.md'

# Read CSV and calculate column widths
with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)  # Read all rows
    headers = rows[0]    # Extract headers
    data = rows[1:]      # Extract data

    # Calculate max width for each column
    column_widths = [max(len(str(item)) for item in col) for col in zip(*rows)]

    # Generate formatted Markdown table
    def format_row(row):
        return "| " + " | ".join(f"{str(cell).ljust(width)}" for cell, width in zip(row, column_widths)) + " |"

    # Build the Markdown table
    markdown_table = format_row(headers) + "\n"
    markdown_table += "| " + " | ".join("-" * width for width in column_widths) + " |\n"
    for row in data:
        markdown_table += format_row(row) + "\n"

# Write the Markdown table to a file
with open(output_file, 'w') as md_file:
    md_file.write(markdown_table)
