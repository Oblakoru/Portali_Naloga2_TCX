import os
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

def remove_extension(filename):
    base, ext = os.path.splitext(filename)
    return base


# Točka 1
pot = "runningDataPandas.csv"
df = pd.read_csv(pot)

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

#potDoDatotekeOdstranitev = "runningDataPandas.csv"

#dfOdtranitevStolpca = pd.read_csv(potDoDatotekeOdstranitev)

#Axis 0 pomen da gleda sam po vertikali
steviloPraznih = df.isna().sum(axis=0)
#print(steviloPraznih)
stolpecZaOdstranitev = steviloPraznih.idxmax()


if steviloPraznih.max() != 0:
    print(f"Odstranjen bo: {df.isna().sum().idxmax()} z vrednostjo: {df.isna().sum().max()}")
    dfOdstranjevanje = df.drop(columns=df.isna().sum().idxmax())


    ####TUle še daj na konc!
    #dfOdstranjevanje.to_csv(f"{remove_extension(df)}Odstranjeno.csv", index=False)
else:
    print("Odstranjen ne bo noben stolpec, saj ni manjkajočih podatkov!")


#Točka 7

#potDoDatotekeNormalizacija = "runningDataPandas.csv"

#dfNormalizacija = pd.read_csv(potDoDatotekeNormalizacija)



df["caloriesNormalized"] = (df["calories"] - df["calories"].min()) / (df["calories"].max() - df["calories"].min())

df.to_csv(f"{remove_extension(pot)}Normalizirano.csv", index=False)

#print(dfNormalizacija)

#Točka 8, 9, 10

bins = [0, 500, 800, 1500, np.inf]
labels = ['Povprecen', 'Izjemen', 'Zelo dober Trening', 'Neverjetno']

df['Diskretizacija'] = pd.cut(df['calories'], bins=bins, labels=labels, right=False)

df.to_csv(f"{remove_extension(pot)}Final.csv", index=False)

df = pd.read_csv("runningDataPandasFinal.csv")

numericniStoplci = df.select_dtypes(include=[object]).columns

for col in numericniStoplci:
    print(f"Ime stolpca: {col} vrednosti: {df[col].unique()}")



