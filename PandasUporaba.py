import pandas as pd

df = pd.read_csv("bikingData.csv")


#print(df.describe(include=[float, int]))

columns_described = df.select_dtypes(include=[float, int]).columns

for col in columns_described:
    if col == "id":
        continue
    column_mean = df[col].mean()
    column_median = df[col].median()
    column_max = df[col].max()
    column_min = df[col].min()
    manjkajoci = df[col].isna().sum()

    print(f"Column: {col}, Mean: {column_mean}, Median: {column_median}, Max: {column_max}, Min: {column_min} Stevilo manjkajocih: {manjkajoci}")
    print("--------------------------------------------------------------------------")



from sport_activities_features.interval_identification import (
    IntervalIdentificationByHeartRate,
    IntervalIdentificationByPower,
)
from sport_activities_features.tcx_manipulation import TCXFile


# Reading the TCX file
tcx_file = TCXFile()
activity = tcx_file.read_one_file('Sport5/1/1.tcx')

# Identifying the intervals in the activity by power
Intervals = IntervalIdentificationByPower(
    activity['distances'],
    activity['timestamps'],
    activity['altitudes'],
    mass=70
)

Intervals.identify_intervals()
all_intervals_power = Intervals.return_intervals()
all_intervals_power1 = Intervals.calculate_interval_statistics()

print(all_intervals_power)
print(all_intervals_power1)

# Identifying the intervals in the activity by heart rate
Intervals = IntervalIdentificationByHeartRate(
    activity['distances'],
    activity['timestamps'],
    activity['altitudes'],
    activity['heartrates'],
)
Intervals.identify_intervals()
all_intervals_heart = Intervals.return_intervals()
all_intervals_heart1 = Intervals.calculate_interval_statistics()

print(all_intervals_heart1)



data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'BMI': [22.5, 18.9, 27.6, 30.2, 20.7]
}

df = pd.DataFrame(data)

# Define the ranges and labels for BMI categories
bins = [0, 18.5, 24.9, 29.9, 100]  # Ranges for underweight, normal, overweight, and obese
labels = ['Underweight', 'Normal weight', 'Overweight', 'Obese']

# Discretize the 'BMI' column into categories
df['BMI Category'] = pd.cut(df['BMI'], bins=bins, labels=labels, right=False)

print(df)
