import os
import pandas as pd

def process_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".xlsx"):
            file_path = os.path.join(folder_path, filename)
            process_excel_file(file_path)

def process_excel_file(file_path):
    print(f"Processing {file_path}")

    # Specify the engine when reading the Excel file
    df = pd.read_excel(file_path, engine='openpyxl')

    # Filter rows where the "Event" column contains "100"
    df = df[df['Event'] == 100]

    # Save the modified DataFrame back to the Excel file
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

# Example usage
folder_path = "/Users/thomaswu/Downloads/urop"
process_files_in_folder(folder_path)
