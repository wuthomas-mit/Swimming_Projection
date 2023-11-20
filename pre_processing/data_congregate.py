import os
import pandas as pd

# Folder containing the Excel files
folder_path = "/Users/thomaswu/Downloads/urop"

# Output file name
output_file = "combined_output.xlsx"


# Initialize an empty list to store DataFrames
data_frames = []

# Loop through all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(".xlsx"):
        file_path = os.path.join(folder_path, file_name)
        # Extract the name from the file name
        name = file_name.replace("Times For ", "").replace(".xlsx", "")
        # Read each Excel file into a DataFrame
        # df = pd.read_excel(file_path)
        df = pd.read_excel(file_path, engine='openpyxl')
        # Add a new column with the extracted name
        df['Name'] = name
        # Append the data to the list
        data_frames.append(df)
        

# Combine all DataFrames into one
combined_data = pd.concat(data_frames, ignore_index=True)


# Write the combined DataFrame to a new Excel file
combined_data.to_excel(output_file, index=False)


print(f"Combined data with names written to {output_file}")
