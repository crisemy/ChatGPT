import pandas as pd
import os

# Path to the directory containing the Excel files
directory = "excel_files"

# Get a list of all Excel files in the directory
excel_files = [file for file in os.listdir(directory) if file.endswith(".xlsx")]

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate over each Excel file and merge its data into the DataFrame
for file in excel_files:
    file_path = os.path.join(directory, file)
    data = pd.read_excel(file_path)  # Read the Excel file
    merged_data = pd.concat([merged_data, data], ignore_index=True)  # Concatenate data frames

# Path to the output merged Excel file
output_file = "merged_data.xlsx"

# Write the merged data to a new Excel file
merged_data.to_excel(output_file, index=False)

print("Merged data saved to", output_file)
