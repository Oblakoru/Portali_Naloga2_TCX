import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('bikingDataFiltered.csv')

#Graf za predstavitev kalorij ter časa dejavnosti
plt.figure()
plt.scatter(df['duration'], df['calories'])
plt.xlabel('Duration (seconds)')
plt.ylabel('Calories Burned')
plt.title('Calories Burned vs. Duration')
plt.show()

#Graf za predstavitev kaolrij ter dolžine
plt.figure()
plt.scatter(df['distance'], df['calories'])
plt.xlabel('Duration (m)')
plt.ylabel('Calories (s)')
plt.title('Distance vs. calories')
plt.show()


#Tortni graf za percentualno vrsto aktivnosti
df1 = pd.read_csv('bikingData.csv')
df2 = pd.read_csv('otherData.csv')
df3 = pd.read_csv('runningData.csv')

n_instances_1 = len(df1)
n_instances_2 = len(df2)
n_instances_3 = len(df3)

n_instances = [n_instances_1, n_instances_2, n_instances_3]

plt.figure()
plt.pie(n_instances, labels=['Biking', 'Other', 'Running'])
plt.title('Pie Chart of Number of Instances in 3 CSV Files')
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
plt.title('Average Heart Rate for Each Activity Type')
plt.show()






