import os
import pandas as pd

# Function to process each Excel file in the folder
def process_excel_file(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    df = df.drop(columns=['Alt. Adj. Time'])

    # Convert the 'Time' column to a string with the desired format
    df['Time'] = df['Time'].dt.strftime('%M:%S.%f')[:-3]

    # Save the modified DataFrame back to the Excel file
    df.to_excel(file_path, sheet_name='Sheet1', index=False)

# Specify the folder containing the Excel files
folder_path = "/Users/thomaswu/Downloads/50FREEDATA"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        file_path = os.path.join(folder_path, filename)
        process_excel_file(file_path)

print("Processing completed.")
