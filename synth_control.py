import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pysyncon import Dataprep, Synth



# Load your data from Excel
file_path = '/Users/thomaswu/Documents/Programming/Swimming_Projection/combined_output.xlsx'
df = pd.read_excel(file_path)

# Select the fastest swim per year of age
fastest_swims = df.sort_values('Time').groupby(['Name', 'Age']).head(1)

# Pivot the data
pivoted_df = fastest_swims.pivot_table(index='Name', columns='Age', values='Time', aggfunc='first').fillna(np.NaN)

'''


# Count non-zero values for each column
non_zero_counts = pivoted_df.astype(bool).sum(axis=0)

# Sort the columns based on the number of non-zero values in descending order
sorted_columns = non_zero_counts.sort_values(ascending=False)

# Display the result
print(sorted_columns)

'''

# Specify the age range you want to include
age_range_start = 5
age_range_end = 28

# Convert column names to integers and filter columns based on the age range
selected_columns = pivoted_df.loc[:, (pivoted_df.columns.astype(int) >= age_range_start) & (pivoted_df.columns.astype(int) <= age_range_end)]


# # Filter swimmers with times for all ages in the range
# filtered_swimmers = selected_columns.loc[:, (selected_columns.columns >= age_range_start) & (selected_columns.columns <= age_range_end)].astype(bool).all(axis=1)

# # Keep only the rows (swimmers) that have all times
# swimmers_all_times = selected_columns[filtered_swimmers]

'''
# Convert the DataFrame to a numpy array
data_matrix = swimmers_all_times.values

# Perform SVD
U, Sigma, VT = np.linalg.svd(data_matrix, full_matrices=False)

# U: Left singular vectors
# Sigma: Singular values
# VT: Transpose of right singular vectors


# Number of singular values to retain (choose based on the elbow method or other criteria)
k = 1

# Retain only the top k singular values and vectors
U_k = U[:, :k]
Sigma_k = np.diag(Sigma[:k])
VT_k = VT[:k, :]


# Assuming new_swimmer_data is a new swimmer's data
new_swimmer_data = pd.DataFrame({
    'Name': "INPUT",
    'Age': [10, 11, 12, 13, 14, 15, 16],
    'Time': [62.13, 58.96, 53.99, 49.51, 47.5, 45.56, 43.82],  # Fill in the actual time data for the new swimmer
})

'''
# new strat start
# Assuming 'pivoted_df' is the pivoted DataFrame
stacked_df = selected_columns.stack().reset_index()

# Rename the columns for clarity
stacked_df.columns = ['Name', 'Age', 'Time']

#Creating Input Swimmer
new_ages = [10, 11, 12, 13, 14, 15, 16]
new_times = [62.13, 58.96, 53.99, 49.51, 47.5, 45.56, 43.82]

# Create a DataFrame from the new data
new_data = {'Name': 'INPUT', 'Age': new_ages, 'Time': new_times}
new_rows_df = pd.DataFrame(new_data)

# Append the new DataFrame to the existing DataFrame
stacked_df = pd.concat([stacked_df, new_rows_df], ignore_index=True)

names_list = stacked_df['Name'].unique().tolist()
names_list.remove("INPUT")

dataprep_train = Dataprep(
    foo=stacked_df,
    predictors= ["Time"],
    predictors_op= "mean",
    time_predictors_prior=range(10,22),
    dependent="Time",
    unit_variable="Name",
    time_variable="Age",
    treatment_identifier="INPUT",
    controls_identifier= names_list,
    time_optimize_ssr=range(10,22),
)

synth_train = Synth()
# synth_train.fit(dataprep=dataprep_train)
synth_train.fit(dataprep=dataprep_train, optim_method="Nelder-Mead", optim_initial="equal")
print(synth_train.weights())

synth_train.path_plot(time_period=range(10, 22), treatment_time= 16)
synth_train.gaps_plot(time_period=range(10, 22), treatment_time= 16)
