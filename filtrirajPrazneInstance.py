import pandas as pd

# Read the CSV file into a Pandas DataFrame

#Pr other in running tak vsak manka tk da ne!
df = pd.read_csv("runningData.csv")

# Drop all rows with empty values
df.dropna(inplace=True)

# Write the Pandas DataFrame to a new CSV file
df.to_csv("runningDataFiltered.csv", index=False)