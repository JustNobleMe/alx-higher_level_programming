
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

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

# Group the data by day of the week (assuming you have a 'day_of_week' column)
day_of_week_departure_delay = df.groupby('DAY_OF_WEEK')['DEPARTURE_DELAY'].mean()
print("Average Departure Delay by Day of the Week:")
print(day_of_week_departure_delay)

# Filter data for positive departure delays
positive_departure_delay_data = df[df['DEPARTURE_DELAY'] > 0]

# Check correlation between distance and arrival delay for positive departure delays
distance_arrival_corr = positive_departure_delay_data['DISTANCE'].corr(positive_departure_delay_data['ARRIVAL_DELAY'])

print(f"Correlation between Distance and Arrival Delay for Positive Departure Delays: {distance_arrival_corr}")


#SEASONAL MONTH

# Convert the 'month' column to a datetime format
df['MONTH'] = pd.to_datetime(df['MONTH'], format='mixed')

# Group the data by month and calculate the average departure delay
monthly_departure_delays = df.groupby(df['MONTH'].dt.month)['DEPARTURE_DELAY'].mean()

# Create a line plot to visualize the seasonal pattern
plt.figure(figsize=(12, 6))
monthly_departure_delays.plot(marker='o', linestyle='-')
plt.xlabel('Month')
plt.ylabel('Average Departure Delay (minutes)')
plt.title('Seasonal Pattern of Departure Delays')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True)
plt.show()

#REMOVE MISSING COLUMNS
df = df.dropna(subset=['WEATHER_DELAY'])

# Check for missing values after removal
missing_values = df.isnull().sum()


# Convert categorical variables like 'AIRLINE' into dummy variables (one-hot encoding)
df = pd.get_dummies(df, columns=['AIRLINE'], drop_first=True)

# Define predictors and target variable
predictors = ['LATE_AIRCRAFT_DELAY', 'AIR_SYSTEM_DELAY', 'DEPARTURE_DELAY', 'WEATHER_DELAY', 'SECURITY_DELAY', 'DAY_OF_WEEK', 'DISTANCE'] + list(df.columns[df.columns.str.startswith('AIRLINE_')])  # Include one-hot encoded airline columns
X = df[predictors]
y = df['ARRIVAL_DELAY']


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Calculate IQR and define upper and lower bounds for outliers
Q1 = df['ARRIVAL_DELAY'].quantile(0.25)
Q3 = df['ARRIVAL_DELAY'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
df = df[(df['ARRIVAL_DELAY'] >= lower_bound) & (df['ARRIVAL_DELAY'] <= upper_bound)]

# Log-transform ARRIVAL_DELAY
# df['log_ARRIVAL_DELAY'] = df['ARRIVAL_DELAY'].apply(lambda x: math.log1p(x))  # Adding 1 to handle zero values

# # Define predictors and target variable
# predictors = ['LATE_AIRCRAFT_DELAY', 'AIR_SYSTEM_DELAY', 'DEPARTURE_DELAY', 'WEATHER_DELAY', 'SECURITY_DELAY', 'DAY_OF_WEEK', 'DISTANCE'] + list(df.columns[df.columns.str.startswith('AIRLINE_')])

# # Fit the linear regression model
# X = df[predictors]
# y = df['log_ARRIVAL_DELAY']
# X = sm.add_constant(X)  # Add a constant term (intercept) to the model
# model = sm.OLS(y, X).fit()

# # Summary of the regression model
# print(model.summary())
