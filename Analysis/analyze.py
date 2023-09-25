
import pandas as pd

df = pd.read_csv('/workspaces/alx-higher_level_programming/Analysis/flights.csv')

num_observations = len(df)
num_features = len(df.columns)

print(f"Number of observations: {num_observations}")
print(f"Number of feartures: {num_features}")

sfo_arrivals = len(df[df['DESTINATION_AIRPORT'] == 'SFO'])

airlines_to_sfo = df[df['DESTINATION_AIRPORT'] == 'SFO']['AIRLINE'].nunique()

print(f"Flights arriving at SFO: {sfo_arrivals}")
print(f"Airlines flying to SFO: {airlines_to_sfo}")


# Count missing values in departure delays
missing_departure_delays = df['DEPARTURE_DELAY'].isnull().sum()

# Count missing values in arrival delays
missing_arrival_delays = df['ARRIVAL_DELAY'].isnull().sum()

print(f"Missing departure delays: {missing_departure_delays}")
print(f"Missing arrival delays: {missing_arrival_delays}")

# Remove rows with missing values in both departure and arrival delays
df = df.dropna(subset=['DEPARTURE_DELAY', 'ARRIVAL_DELAY'])

# Calculate average and median departure delay
avg_departure_delay = df['DEPARTURE_DELAY'].mean()
median_departure_delay = df['DEPARTURE_DELAY'].median()

# Calculate average and median arrival delay
avg_arrival_delay = df['ARRIVAL_DELAY'].mean()
median_arrival_delay = df['ARRIVAL_DELAY'].median()

print(f"Average Departure Delay: {avg_departure_delay}")
print(f"Median Departure Delay: {median_departure_delay}")
print(f"Average Arrival Delay: {avg_arrival_delay}")
print(f"Median Arrival Delay: {median_arrival_delay}")


#Question 6

departure_summary = df.groupby('AIRLINE')['DEPARTURE_DELAY'].describe()

# Sort by median departure delay in descending order
departure_summary = departure_summary.sort_values(by='50%', ascending=False)

# Do the same for arrival delay
arrival_summary = df.groupby('AIRLINE')['ARRIVAL_DELAY'].describe()
arrival_summary = arrival_summary.sort_values(by='50%', ascending=False)

print("5-Number Summary of Departure Delay by Airline:")
print(departure_summary)

print("\n5-Number Summary of Arrival Delay by Airline:")
print(arrival_summary)


# Calculate average departure delay for each airline
avg_departure_delays = df.groupby('AIRLINE')['DEPARTURE_DELAY'].mean()

# Find the airline with the highest average departure delay
airline_with_most_delay = avg_departure_delays.idxmax()
most_delayed_airline = avg_departure_delays.max()

# Get the top 10 airlines with the highest average departure delays
top_10_airlines = avg_departure_delays.nlargest(10)

print(f"The airline with the most averaged departure delay is {airline_with_most_delay} with an average delay of {most_delayed_airline} minutes.")
print("\nTop 10 Airlines with the Highest Average Departure Delays:")
print(top_10_airlines)


# Check correlation between departure delay and distance
departure_distance_corr = df['DEPARTURE_DELAY'].corr(df['DISTANCE'])
arrival_distance_corr = df['ARRIVAL_DELAY'].corr(df['DISTANCE'])

print(f"Correlation between Departure Delay and Distance: {departure_distance_corr}")
print(f"Correlation between Arrival Delay and Distance: {arrival_distance_corr}")
