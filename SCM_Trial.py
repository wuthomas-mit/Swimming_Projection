#Import packages
import pandas as pd
import numpy as np
from SyntheticControlMethods import Synth

# Load your data from Excel
file_path = '/Users/thomaswu/Documents/Programming/Swimming_Projection/combined_output_50FREE.xlsx'
df = pd.read_excel(file_path)

# Select the fastest swim per year of age
fastest_swims = df.sort_values('Time').groupby(['Name', 'Age']).head(1)

# Pivot the data
pivoted_df = fastest_swims.pivot_table(index='Name', columns='Age', values='Time', aggfunc='first').fillna(0)

# Specify the age range you want to include
age_range_start = 10
age_range_end = 21

# Convert column names to integers and filter columns based on the age range
selected_columns = pivoted_df.loc[:, (pivoted_df.columns.astype(int) >= age_range_start) & (pivoted_df.columns.astype(int) <= age_range_end)]


# Filter swimmers with times for all ages in the range
filtered_swimmers = selected_columns.loc[:, (selected_columns.columns >= age_range_start) & (selected_columns.columns <= age_range_end)].astype(bool).all(axis=1)

# Keep only the rows (swimmers) that have all times
swimmers_all_times = selected_columns[filtered_swimmers]

# new strat start
# # Assuming 'pivoted_df' is the pivoted DataFrame
# stacked_df = swimmers_all_times.stack().reset_index()

# # Rename the columns for clarity
# stacked_df.columns = ['Name', 'Age', 'Time']

# #Fit classic Synthetic Control
# sc = Synth(stacked_df, "Time", "Name", "Age", 17, "Aaron Sequeira", n_optim=10, pen=0)

# #Visualize synthetic control
# sc.plot(["original", "pointwise", "cumulative"], treated_label="Aaron Sequeira", synth_label="Synthetic Aaron Sequeira", treatment_label="Age")

# Assuming 'pivoted_df' is the pivoted DataFrame
stacked_df = swimmers_all_times.stack().reset_index()

# Rename the columns for clarity
stacked_df.columns = ['Name', 'Age', 'Time']
print(stacked_df)

sc = Synth(stacked_df, "Time", "Name", "Age", 17, "Aaron Sequeira", n_optim=10, pen="auto")

sc.plot(["original", "pointwise", "cumulative"], treated_label="Aaron Sequeira", synth_label="Synthetic Aaron Sequeira", treatment_label="Age")
