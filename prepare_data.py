import os
import zipfile

import gdown

# Replace the 'FILE_ID' below with the actual file ID from your Google Drive link
file_id = '1YjCt-RZUyEHslqmA3yJHJi-Tk6SNFlbP'  # e.g., '1a2b3c4d5e6f7g8h9i0j'

# Create the full download URL
url = f'https://drive.google.com/uc?id={file_id}'

# Specify the output filename for the downloaded file
output_zip = 'data.zip'  # Change the output name if necessary

# Define a folder name or file to check if extraction is already done
extracted_folder = 'sample_data'

# Check if the folder already exists
if os.path.exists(extracted_folder):
    print(f"The folder '{extracted_folder}' already exists. Skipping download and extraction.")
else:
    # Check if the .zip file is already downloaded
    if not os.path.exists(output_zip):
        # Download the file from Google Drive
        print("Downloading the file...")
        gdown.download(url, output_zip, quiet=False)
    else:
        print(f"'{output_zip}' already exists. Skipping download.")

    # Unzip the file
    print("Unzipping the file...")
    with zipfile.ZipFile(output_zip, 'r') as zip_ref:
        # Extract all contents to the current directory
        zip_ref.extractall()

    # Check if the extraction created the intended folder
    if os.path.exists(extracted_folder):
        print(f"Unzipped contents are placed in {os.path.abspath(extracted_folder)}")
    else:
        print("Extraction was unsuccessful. Please check the zip file.")

    # Optionally, delete the zip file after extraction
    os.remove(output_zip)
    print(f"Removed the zip file: {output_zip}")
