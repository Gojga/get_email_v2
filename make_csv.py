import csv

def remove_duplicates_and_save_as_csv(input_file, output_file):
    # Create a set to store unique lines
    unique_lines = set()

    # Read the input file and process each line
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:  # Check if the line is not empty
                unique_lines.add(line)

    # Write the unique lines to a CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in unique_lines:
            # Split the line by comma and add each part as a separate column in the CSV
            parts = line.split(',')
            csv_writer.writerow(parts)

# Specify the input and output file names
input_file = 'email_addresses.txt'
output_file = 'email_addresses.csv'

# Call the function to remove duplicates and save as CSV
remove_duplicates_and_save_as_csv(input_file, output_file)
