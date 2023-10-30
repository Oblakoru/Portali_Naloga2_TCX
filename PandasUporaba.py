import pandas as pd

import seaborn as sns

# Za preinovanje headerja! #header = ['id', 'activity_type', 'distance', 'duration', 'calories', 'hr_avg', 'hr_max',
# 'hr_min', 'altitude_avg', 'altitude_max', 'altitude_min', 'ascent', 'descent', 'steps', #
# 'num_hills', 'avg_altitude', 'avg_ascent', 'distance_hills', 'hills_share', 'number_of_intervalsPower',
# 'min_durationPower', 'max_durationPower', 'avg_durationPower', 'min_distancePower', 'max_distancePower',
# 'avg_distancePower', 'number_of_intervalsHeart', #                           'min_duration_intervalHeart',
# 'max_duration_intervalHeart', 'avg_duration_intervalHeart', 'min_distance_intervalHeart',
# 'max_distance_intervalHeart', 'avg_distance_intervalHeart', 'min_heartrate_intervalHeart',
# 'max_heartrate_intervalHeart', 'avg_heartrate_intervalHeart'] # #dfHeader = pd.read_csv("otherDataPandas.csv",
# header=None) #new_header = ['new', 'column', 'names'] #dfHeader.to_csv("otherDataPandasHeaders.csv", header=header,
# index=False)


#Točka 1
df = pd.read_csv("bikingDataPandas.csv")

# print(df.describe(include=[float, int]))

##Točka 2 in 3
columns_described = df.select_dtypes(include=[float, int]).columns

for col in columns_described:
    if col == "id":
        continue
    column_mean = df[col].mean()
    column_median = df[col].median()
    column_max = df[col].max()
    column_min = df[col].min()
    manjkajoci = df[col].isna().sum()

    print(
        f"Column: {col}, Mean: {column_mean}, Median: {column_median}, Max: {column_max}, Min: {column_min} Stevilo manjkajocih: {manjkajoci}")
    print("--------------------------------------------------------------------------")

##Točka 4? WtF


##Točka 5 in 6 - DONE v mainu

# Točka 7

dfKopija = pd.read_csv("dummy.csv")

print(f"Odstranjen bo: {dfKopija.isna().sum().idxmax()} z vrednostjo: {dfKopija.isna().sum().max()}")
dfOdstranjevanje = dfKopija.drop(columns=dfKopija.isna().sum().idxmax())
dfOdstranjevanje.to_csv("dummyKopija.csv", index=False)

#Točka 8

df_min_max_scaled = dfKopija.copy()

df_min_max_scaled["age"] = (df_min_max_scaled["age"] - df_min_max_scaled["age"].min()) / (df_min_max_scaled["age"].max() - df_min_max_scaled["age"].min())

# view normalized data
print(df_min_max_scaled)


#Točka 9



df = pd.read_csv("dummy.csv")

# Define the ranges and labels for BMI categories
bins = [0, 18.5, 30, 60, 100]  # Ranges for underweight, normal, overweight, and obese
labels = ['Mlad', 'Srednje mlad', 'Star', 'Zelo star']

# Discretize the 'BMI' column into categories
df['Diskretizacija'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

print(df)
