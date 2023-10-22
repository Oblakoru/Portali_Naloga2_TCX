import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('bikingDataFiltered.csv')

plt.figure()
plt.scatter(df['duration'], df['calories'])
plt.xlabel('Duration (seconds)')
plt.ylabel('Calories Burned')
plt.title('Calories Burned vs. Duration')
plt.show()

plt.figure()
plt.scatter(df['distance'], df['calories'])
plt.xlabel('Duration (m)')
plt.ylabel('Calories (s)')
plt.title('Distance vs. calories')
plt.show()


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

