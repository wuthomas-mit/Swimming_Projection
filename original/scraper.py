import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Send a GET request to the URL
url = 'https://www.swimcloud.com/swimmer/404486/times/byevent/?event_id=2200Y'  # Replace with your desired URL
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find all instances of <a> tags with the specified pattern in the 'href' attribute
pattern = re.compile(r'/results/\d+/event/\d+/\?id=\d+#time(\d+:\d+\.\d+)')
matching_strings = soup.find_all('a', href=pattern)

# Extract the time from the href attribute
times = []
for string in matching_strings:
    match = re.search(pattern, string['href'])
    if match:
        times.append(match.group(1))

# Create a DataFrame
data = {'Time': times}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
