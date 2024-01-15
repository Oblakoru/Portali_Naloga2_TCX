import matplotlib.pyplot as plt
import pandas as pd
from sport_activities_features import TCXFile, HillIdentification
from sport_activities_features.hill_identification import HillIdentification
from sport_activities_features.plot_data import PlotData
from sport_activities_features.tcx_manipulation import TCXFile
from sport_activities_features.interval_identification import (
    IntervalIdentificationByHeartRate,
    IntervalIdentificationByPower,
)
from sport_activities_features.plot_data import PlotData


df = pd.read_csv('bikingDataFiltered.csv')

#Graf za predstavitev kalorij ter časa dejavnosti
plt.figure()
plt.scatter(df['duration'], df['calories'], c='blue')

df = pd.read_csv('runningData.csv')
plt.scatter(df['duration'], df['calories'], c='green')


plt.xlabel('Trajanje(min)')
plt.ylabel('Kalorije')
plt.title('Kalorije|Trajanje Biking in Running')
plt.show()

#Graf za predstavitev kaolrij ter dolžine
plt.figure()
plt.scatter(df['distance'], df['calories'])
plt.xlabel('Dolzina(m)')
plt.ylabel('Kalorije')
plt.title('Kalorije|Dolzina Running')
plt.show()


#Tortni graf za percentualno vrsto aktivnosti
df1 = pd.read_csv('bikingData.csv')
df2 = pd.read_csv('otherData.csv')
df3 = pd.read_csv('runningData.csv')

n_1 = len(df1)
n_2 = len(df2)
n_3 = len(df3)

n_instances = [n_1, n_2, n_3]

plt.figure()
plt.pie(n_instances, labels=['Biking', 'Other', 'Running'], autopct="%1.1f%%")
plt.title('Razmerje aktivnosti')
plt.show()


#Graf za prikaz avg heart rate za vsako aktivnost
avg_hr1CSV = pd.read_csv("bikingData.csv")
avg_hr2CSV = pd.read_csv("otherData.csv")
avg_hr3CSV = pd.read_csv("runningData.csv")

df1_avg = avg_hr1CSV["hr_avg"].mean()
df2_avg = avg_hr2CSV["hr_avg"].mean()
df3_avg = avg_hr3CSV["hr_avg"].mean()

avg_hr_avg = [df1_avg, df2_avg, df3_avg]

plt.figure()
plt.bar(['Biking', 'Other', 'Running'], avg_hr_avg)
plt.title('Povprecni heart rate za aktivnosti')
plt.show()



#Graf za prikaz avg altitude za vsako aktivnost
tcx_file = TCXFile()
data = tcx_file.read_one_file('Sport5/1/2.tcx')

Hill = HillIdentification(data['altitudes'], 30)
Hill.identify_hills()
all_hills = Hill.return_hills()

Map = PlotData()

Map.draw_hills_in_map(data['altitudes'], data['distances'], all_hills)

data = tcx_file.read_one_file('Sport5/1/2.tcx')

Intervals = IntervalIdentificationByPower(data['distances'], data['timestamps'], data ['altitudes'], 70)
Intervals.identify_intervals()
all_intervals = Intervals.return_intervals()
Map = PlotData()
Map.draw_intervals_in_map(data['timestamps'], data['distances'], all_intervals)




