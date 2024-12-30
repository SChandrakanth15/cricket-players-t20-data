import csv

# Relative path to the CSV file
input_file = 't20.csv'

# Read the CSV file
with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Get the header row

    # Add some emojis and start the Markdown table
    markdown_table = "### 🏏 Cricket Players T20 Stats 🏏\n\n"
    markdown_table += ":star2: **Here is the table of cricket players' stats in T20 format:** :star2:\n\n"
    
    # Create the table header
    markdown_table += "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    # Create the table rows with some emoji-based flair (optional)
    for row in reader:
        markdown_table += "| " + " | ".join(row) + " |\n"

    # Add a closing note or emoji for excitement
    markdown_table += "\n:clap: **Thanks for checking out the players' data!** :trophy:"

# Write the Markdown table to GitHub Actions summary
print("::group::Cricket Players Table :star_struck:")
print(markdown_table)
print("::endgroup::")
