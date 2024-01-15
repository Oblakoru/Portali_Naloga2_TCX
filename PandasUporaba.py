import os
import warnings
import numpy as np
import pandas as pd


def remove_extension(filename):
    base, ext = os.path.splitext(filename)
    return base

# Točka 1
pot = "runningDataPandas.csv"
df = pd.read_csv(pot)


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



#Axis 0 - gledanje samo po vertikali
steviloPraznih = df.isna().sum(axis=0)
stolpecZaOdstranitev = steviloPraznih.idxmax()
print(stolpecZaOdstranitev)

if steviloPraznih.max() != 0:
    print(f"Odstranjen bo: {df.isna().sum().idxmax()} z vrednostjo: {df.isna().sum().max()}")

    df = df.drop(columns=stolpecZaOdstranitev)

else:
    print("Odstranjen ne bo noben stolpec, saj ni manjkajočih podatkov!")


#Točka 7

df["caloriesNormalized"] = (df["calories"] - df["calories"].min()) / (df["calories"].max() - df["calories"].min())

df.to_csv(f"{remove_extension(pot)}Normalizirano.csv", index=False)


#Točka 8, 9, 10

bins = [0, 500, 800, 1500, np.inf]
labels = ['Povprecen trening', 'Dober trening', 'Zelo dober Trening', 'Neverjeten trening']

df['Diskretizacija'] = pd.cut(df['calories'], bins=bins, labels=labels)

df.to_csv(f"{remove_extension(pot)}Final.csv", index=False)


## Kategorije
df = pd.read_csv("runningDataPandasFinal.csv")

kategoricni = df.select_dtypes(include=[object]).columns

for col in kategoricni:
    print(f"Ime stolpca: {col} vrednosti: {df[col].unique()}")



