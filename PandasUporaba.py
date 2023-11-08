import pandas as pd


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


# 4. ) S pomočjo knjižnice sport-activities-features identificirajte intervale (power in heartrate). (Namig: uporabite tudi metodo calculate_interval_statistics). Iz identificiranih podatkov ustvarite novo podatkovno množico, ki bo predstavljala podatke o obeh tipih intervalov na posamezni trening.
# 5. ) Novo nastalo množico združite s tisto, ki ste jo ustvarili v prejšnji nalogi.
# 6. ) Stolpec kateri ima največ manjkajočih podatkov odstranite.
# 7. ) Normalizirajte poljuben stolpec po metodi min-max normalizacije,
# 8.) Poljubni stolpec z numeričnimi podatki diskretizirajte (ustvarite vsaj 3 in največ 7 kategorij) (primer1, primer2, primer3).
#
# 9. ) Za vsak stolpec s kategoričnimi podatki izpišite vse kategorije.
#
# 10. ) Novo združeno in procesirano podatkovno množico zapišite v novo csv datoteko.

##Točka 4, 5 (main) in 6

potDoDatotekeOdstranitev = "runningDataPandas.csv"

dfOdtranitevStolpca = pd.read_csv(potDoDatotekeOdstranitev)

##Axis 0 pomen da gleda sam po vertikali
steviloPraznih = df.isna().sum(axis=0)




print(f"Odstranjen bo: {dfOdtranitevStolpca.isna().sum().idxmax()} z vrednostjo: {dfOdtranitevStolpca.isna().sum().max()}")
dfOdstranjevanje = dfOdtranitevStolpca.drop(columns=dfOdtranitevStolpca.isna().sum().idxmax())
dfOdstranjevanje.to_csv(f"{potDoDatotekeOdstranitev}Odstranjeno.csv", index=False)


#Točka 8

df_min_max_scaled = dfKopija.copy()

df_min_max_scaled["calories"] = (df_min_max_scaled["calories"] - df_min_max_scaled["calories"].min()) / (df_min_max_scaled["calories"].max() - df_min_max_scaled["calories"].min())

print(df_min_max_scaled)

#Točka 9
df = pd.read_csv("runningDataPandasHeaders.csv")

bins = [0, 300, 500, 800, 1500]
labels = ['Povrecen Trening', 'Dober Trening', 'Zelo dober Trening', 'Extremno dober trening']

df['Diskretizacija'] = pd.cut(df['calories'], bins=bins, labels=labels, right=False)

print(df)
