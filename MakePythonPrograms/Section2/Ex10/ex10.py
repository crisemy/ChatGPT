import os
import pandas as pd

# Define the folder path containing the Excel files
folder_path = "excel_files"

# Get the list of files in the folder
files = os.listdir(folder_path)

# Iterate over each file
for file_name in files:
    # Check if the file is an Excel file
    if file_name.endswith(".xlsx") or file_name.endswith(".xls"):
        # Create the file path
        file_path = os.path.join(folder_path, file_name)
        
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Add the "annual_salary" column
        df["annual_salary"] = df["monthly salary"] * 12
        
        # Save the modified DataFrame back to the Excel file
        df.to_excel(file_path, index=False)
        
        print(f"Processed file: {file_name}")
