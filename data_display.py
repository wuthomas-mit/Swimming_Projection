import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
import numpy as np
from scipy.optimize import curve_fit

# Define the logarithmic function
def logarithmic_func(x, a, b):
    return a * np.log(x) + b

# Load the combined data from the JSON file
with open('data/combined_data.json', 'r') as file:
    combined_data = json.load(file)

# Dictionary to store the parameters for each event
all_log_fit_params = {}

# Iterate through each person
for person_key, person_data in combined_data.items():
    gender = person_data['gender']
    for event_name, event_data in person_data['events'].items():
        if len(event_data['swims']) > 8:
            data_points = []
            for date_key, time_value in event_data['swims'].items():
                date = datetime.strptime(date_key, '%Y%m%d').date()
                data_points.append((date, float(time_value)))

            data_points.sort(key=lambda x: x[0])
            sorted_dates = [x[0].strftime('%b %d %Y') for x in data_points]
            sorted_times = [x[1] for x in data_points]

            plt.figure(figsize=(12, 8)) 
            plt.plot(sorted_dates, sorted_times, '-o', label='Data Points')

            # Fit the function
            x = np.arange(1, len(sorted_dates) + 1)  # Using 1-based index for the swims
            popt, _ = curve_fit(logarithmic_func, x, sorted_times)

            if event_name in all_log_fit_params:
                all_log_fit_params[event_name].append(popt)
            else:
                all_log_fit_params[event_name] = [popt]

            # Plot the fitted curve
            plt.plot(sorted_dates, logarithmic_func(x, *popt), label='Logarithmic Fit')

            plt.xlabel('Date')
            plt.ylabel('Time (seconds)')
            plt.title(f'Performance Over Time for Person {person_key} - Event: {event_name} - Gender: {gender}')

            # Set y-axis limits dynamically
            plt.ylim(min(sorted_times) * 0.985, max(sorted_times) * 1.015)

            plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
            plt.legend()
            plt.show()

# Calculate the average parameters for each event
average_log_fit_params = {}
for event_name, params_list in all_log_fit_params.items():
    average_params = np.mean(params_list, axis=0)
    average_log_fit_params[event_name] = average_params

# Create a generalized logarithmic function using the average parameters
def generalized_logarithmic_func(x, a, b):
    return a * np.log(x) + b

# Function to predict next year's time for an event using the generalized function
# def predict_next_year_time(event_name, year, params):
#     next_year = year + 1
#     return generalized_logarithmic_func(next_year, *params)
