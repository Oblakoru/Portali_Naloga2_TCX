import pandas as pd

df = pd.read_csv("runningData.csv")

df.dropna(inplace=True)

df.to_csv("runningDataFiltered.csv", index=False)