
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

# Load data from a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Convert the data into a DataFrame
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])  # Ensure the date column is in datetime format

# Plot the time series data
sns.lineplot(x='date', y='value', data=df)
plt.title('Time Series Graph')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)  # Rotate date labels for better visibility
plt.tight_layout()
plt.show()

[
    {"date": "2021-01-01", "value": 10},
    {"date": "2021-01-02", "value": 15},
    {"date": "2021-01-03", "value": 8}
]
