# import pandas as pd
# import ast

# # Load the data, skipping the first row
# df = pd.read_csv('usa_data.csv', skiprows=1, names=['person_key', 'event_name', 'gender', 'time1', 'date_key1', 'time2', 'date_key2', 'time3', 'date_key3', 'time4', 'date_key4'])

# # Group the data by 'person_key'
# df_grouped = df.groupby(['person_key', 'gender'])

# # Combine the event data for each person
# combined_data = []
# for (person, gender), group in df_grouped:
#     person_key = int(person)  # Convert back to integer
#     event_data = {}
#     for index, row in group.iterrows():
#         event_name = str(row['event_name'])
#         if event_name not in event_data:
#             event_data[event_name] = {'times': [], 'dates': []}
#         for i in range(1, 5):
#             time_key = row[f'time{i}']
#             date_key = row[f'date_key{i}']
#             event_data[event_name]['times'].append(str(time_key))
#             event_data[event_name]['dates'].append(str(date_key))
#     for event, data in event_data.items():
#         combined_data.append([person_key, event, gender, data['times'], data['dates']])

# # Create a new DataFrame from the combined data
# df_combined = pd.DataFrame(combined_data, columns=['person_key', 'event_name', 'gender', 'times', 'dates'])

# # Save the combined data to a new CSV
# df_combined.to_csv('combined_data.csv', index=False)
import pandas as pd

# Load the data, skipping the first row
df = pd.read_csv('usa_data.csv', skiprows=1, names=['person_key', 'event_name', 'gender', 'time1', 'date_key1', 'time2', 'date_key2', 'time3', 'date_key3', 'time4', 'date_key4'])

# Group the data by 'person_key'
df_grouped = df.groupby(['person_key', 'gender'])

# Combine the event data for each person
combined_data = {}
for (person, gender), group in df_grouped:
    person_key = int(person)  # Convert back to integer
    if person_key not in combined_data:
        combined_data[person_key] = {'gender': gender, 'events': {}}
    for index, row in group.iterrows():
        event_name = str(row['event_name'])
        if event_name not in combined_data[person_key]['events']:
            combined_data[person_key]['events'][event_name] = {'swims': {}}
        for i in range(1, 5):
            date_key = row[f'date_key{i}']
            combined_data[person_key]['events'][event_name]['swims'][date_key] = str(row[f'time{i}'])

# Save the combined data to a new JSON file
import json
with open('combined_data.json', 'w') as file:
    json.dump(combined_data, file, indent=4)


# https://www.swimcloud.com/swimmer/404486/times/byevent/?event_id=2200Y