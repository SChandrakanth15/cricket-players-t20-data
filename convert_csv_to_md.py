import csv

# Relative path to the CSV file
input_file = 't20.csv'

# Read the CSV file
with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Get the header row

    # Generate Markdown table
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    for row in reader:
        markdown_table += "| " + " | ".join(row) + " |\n"

# Write the Markdown table to the GitHub Actions summary
print("::group::Cricket Players Table")
print(markdown_table)
print("::endgroup::")
