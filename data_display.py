import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
import numpy as np
from scipy.optimize import curve_fit

def logarithmic_func(x, a, b):
    return a * np.log(x) + b
log_fit_params = {}
data_dict = {}

# Load the combined data from the JSON file
with open('data/combined_data.json', 'r') as file:
    combined_data = json.load(file)

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
            data_dict[event_name] = data_points
            sorted_dates = [x[0].strftime('%b %d %Y') for x in data_points]
            sorted_times = [x[1] for x in data_points]

            plt.figure(figsize=(12, 8)) 
            plt.plot(sorted_dates, sorted_times, '-o', label='Data Points')

             # Fit the function
            x = np.arange(1, len(sorted_dates) + 1)  # Using 1-based index for the swims
            popt, _ = curve_fit(logarithmic_func, x, sorted_times)
            log_fit_params[event_name] = popt
            plt.plot(sorted_dates, logarithmic_func(x, *popt), label='Logarithmic Fit')


            plt.xlabel('Date')
            plt.ylabel('Time (seconds)')
            plt.title(f'Performance Over Time for Person {person_key} - Event: {event_name} - Gender: {gender}')

            # Set y-axis limits dynamically
            plt.ylim(min(sorted_times) * 0.985, max(sorted_times) * 1.015)

            plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
            plt.legend()
            plt.show()

# # Predicting new data points based on a specific date
# # Assuming 'new_date' as the new input data
# new_date = datetime.strptime('2023-10-15', '%Y-%m-%d').date()  # Sample new date
# for event_name, params in log_fit_params.items():
#     data = data_dict[event_name]
#     swim_for_date = np.where(np.array([x[0] for x in data]) == new_date)[0][0] + 1
#     predicted_time = logarithmic_func(swim_for_date, *params)
#     print(f"Predicted time for event {event_name} on {new_date}: {predicted_time} seconds")