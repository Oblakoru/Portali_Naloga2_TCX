import os
from pathlib import PurePath

import pandas as pd

def remove_extension(filename):
    base, ext = os.path.splitext(filename)
    return base

# Točka 1
df = pd.read_csv("runningDataPandas.csv")

##Describe vrze error
numericniStoplci = df.select_dtypes(include=[float, int]).columns

for col in numericniStoplci:
    if col == "id":
        continue
    povprecje = df[col].mean()
    mediana = df[col].median()
    maxVrednost = df[col].max()
    minVrednost = df[col].min()

    #Isna - missing or null values
    manjkajoci = df[col].isna().sum()

    print(
        f"Column: {col}, povprecje: {povprecje}, Mediana: {mediana}, Max: {maxVrednost}, Min: {minVrednost} Stevilo manjkajocih: {manjkajoci}")
    print("--------------------------------------------------------------------------")


##očka 4, 5 (main) in 6

potDoDatotekeOdstranitev = "runningDataPandas.csv"

dfOdtranitevStolpca = pd.read_csv(potDoDatotekeOdstranitev)

#Axis 0 pomen da gleda sam po vertikali
steviloPraznih = dfOdtranitevStolpca.isna().sum(axis=0)
print(steviloPraznih)
stolpecZaOdstranitev = steviloPraznih.idxmax()


if steviloPraznih.max() != 0:
    print(f"Odstranjen bo: {dfOdtranitevStolpca.isna().sum().idxmax()} z vrednostjo: {dfOdtranitevStolpca.isna().sum().max()}")
    dfOdstranjevanje = dfOdtranitevStolpca.drop(columns=dfOdtranitevStolpca.isna().sum().idxmax())
    dfOdstranjevanje.to_csv(f"{remove_extension(potDoDatotekeOdstranitev)}Odstranjeno.csv", index=False)
else:
    print("Odstranjen ne bo noben stolpec, saj ni manjkajočih podatkov!")



#Točka 7

potDoDatotekeNormalizacija = "runningDataPandas.csv"

dfNormalizacija = pd.read_csv(potDoDatotekeNormalizacija)

dfNormalizacija["caloriesNormalized"] = (dfNormalizacija["calories"] - dfNormalizacija["calories"].min()) / (dfNormalizacija["calories"].max() - dfNormalizacija["calories"].min())

dfNormalizacija.to_csv(f"{remove_extension(potDoDatotekeNormalizacija)}Normalizirano.csv", index=False)

print(dfNormalizacija)

#Točka 9

df = pd.read_csv("bikingDataPandas.csv")



bins = [0, 300, 500, 800, 1500]
labels = ['Povrecen Trening', 'Dober Trening', 'Zelo dober Trening', 'Extremno dober trening']

df['Diskretizacija'] = pd.cut(df['calories'], bins=bins, labels=labels, right=False)

print(df)
