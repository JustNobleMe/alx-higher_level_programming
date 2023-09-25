import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have already loaded and cleaned the data into a DataFrame called 'df'
df = pd.read_csv('/workspaces/alx-higher_level_programming/Analysis/flights.csv')

# Group the data by airline and calculate the average departure and arrival delays
avg_departure_delays = df.groupby('AIRLINE')['DEPARTURE_DELAY'].mean()
avg_arrival_delays = df.groupby('AIRLINE')['ARRIVAL_DELAY'].mean()

# Create bar plots for average departure delays
plt.figure(figsize=(12, 6))
avg_departure_delays.plot(kind='bar', color='blue')
plt.xlabel('Airline')
plt.ylabel('Average Departure Delay (minutes)')
plt.title('Average Departure Delay by Airline')
plt.xticks(rotation=45)
plt.show()

# Create bar plots for average arrival delays
plt.figure(figsize=(12, 6))
avg_arrival_delays.plot(kind='bar', color='green')
plt.xlabel('Airline')
plt.ylabel('Average Arrival Delay (minutes)')
plt.title('Average Arrival Delay by Airline')
plt.xticks(rotation=45)
plt.show()
