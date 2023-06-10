import os
import zipfile

# Create the ZIP_files folder if it doesn't exist
zip_folder = "ZIP_files"
if not os.path.exists(zip_folder):
    os.makedirs(zip_folder)

# Iterate over the text_files directory
text_folder = "text_files"
for filename in os.listdir(text_folder):
    if filename.endswith(".txt"):
        file_number = int(filename.split(".")[0].split("TG_STAID")[1])
        zip_number = (file_number - 1) // 10 + 1
        zip_filename = f"ZIP{zip_number}.zip"
        zip_filepath = os.path.join(zip_folder, zip_filename)

        # Check if the ZIP file exists, if not create it
        if not os.path.exists(zip_filepath):
            with zipfile.ZipFile(zip_filepath, "w") as zip_file:
                pass

        # Add the current file to the ZIP file
        with zipfile.ZipFile(zip_filepath, "a") as zip_file:
            file_path = os.path.join(text_folder, filename)
            zip_file.write(file_path, filename)

print("Files have been placed into separate ZIP files.")