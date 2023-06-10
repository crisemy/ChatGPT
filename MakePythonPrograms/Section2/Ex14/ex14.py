import csv

# Specify the input and output file paths
input_file = "stockholm.csv"
output_file = "stockholm_updated.csv"

# Read the input file and update the values
with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    for row in rows:
        # Convert the TG value to a float, divide by 10, and convert back to a string
        row["TG"] = str(float(row["TG"]) / 10)

# Write the updated values to the output file
with open(output_file, "w", newline="") as file:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Values in the TG column of '{input_file}' have been divided by 10 and saved to '{output_file}'.")
