import pandas as pd

df = pd.read_csv('/Users/thomaswu/Documents/Programming/Swimming_Projection/data/50FREE/50FREESCY.csv', skiprows=1, names=['FullName', 'Event', 'SwimmerAge', 'time1', 'date_key1', 'time2', 'date_key2', 'time3', 'date_key3', 'time4', 'date_key4'])

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
