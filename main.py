import csv
import os
from sport_activities_features import TCXFile
from PodatkiClass import PodatkiClass
from sport_activities_features.hill_identification import HillIdentification
from sport_activities_features.topographic_features import TopographicFeatures
import time

##df.describe(include=[float, int].columns
##Pove kiri stolpci so pravega tipa

#isna.sum

#include=[object]
#unique

#Začatek timerja
start = time.time()

tcx_file = TCXFile()

stevecID = 0

BikingList = []
RunningList = []
OtherList = []

for root, dirs, files in os.walk("Sport5"):
   for datoteka in files:
       try:
           celaPot = os.path.join(root, datoteka)

           # Integralne
           integral_metrics = tcx_file.extract_integral_metrics(celaPot)

           # Hribi in doline
           activity = tcx_file.read_one_file(celaPot)
           Hill = HillIdentification(activity['altitudes'], 30)
           Hill.identify_hills()
           all_hills = Hill.return_hills()


           Top = TopographicFeatures(all_hills)
           num_hills = Top.num_of_hills()
           avg_altitude = Top.avg_altitude_of_hills(activity['altitudes'])
           avg_ascent = Top.avg_ascent_of_hills(activity['altitudes'])
           distance_hills = Top.distance_of_hills(activity['positions'])
           hills_share = Top.share_of_hills(distance_hills, activity['total_distance'])

           #print('num hills: ', num_hills)
           #print('avg_altitude: ', avg_altitude)
           #print('avg_ascent: ', avg_ascent)
           #print('total distance: ', activity['total_distance'] / 1000)
           #print('distance_hills: ', distance_hills)
           #print('hills_share: ', hills_share)

           #print(stevecID)

           podatki = PodatkiClass(stevecID, integral_metrics['activity_type'], integral_metrics['distance'],
                                  integral_metrics['duration'], integral_metrics['calories'],
                                  integral_metrics['hr_avg'], integral_metrics['hr_max'], integral_metrics['hr_min'],
                                  integral_metrics['altitude_avg'], integral_metrics['altitude_max'],
                                  integral_metrics['altitude_min'], integral_metrics['ascent'],
                                  integral_metrics['descent'], integral_metrics['steps'], num_hills, avg_altitude, avg_ascent, distance_hills, hills_share)

           if podatki.activity_type == "Biking":
               BikingList.append(podatki)
           elif podatki.activity_type == "Running":
               RunningList.append(podatki)
           else:
               OtherList.append(podatki)
           stevecID += 1
       except:
           print(f"Napaka pri branju datoteke {datoteka}")
           continue



listInDatoteka = {"bikingData.csv": BikingList, "runningData.csv": RunningList, "otherData.csv": OtherList}


for datoteka, seznam in listInDatoteka.items():
    with open(datoteka, 'w', newline='') as csvfile:
      csv_writer = csv.writer(csvfile)
      csv_writer.writerow(['id', 'activity_type', 'distance', 'duration', 'calories', 'hr_avg', 'hr_max', 'hr_min', 'altitude_avg', 'altitude_max', 'altitude_min', 'ascent', 'descent', 'steps',
                           'num_hills', 'avg_altitude', 'avg_ascent', 'distance_hills', 'hills_share'])

      for podatki_object in seznam:
        csv_writer.writerow([podatki_object.id,
                            podatki_object.activity_type,
                            podatki_object.distance,
                            podatki_object.duration,
                            podatki_object.calories,
                            podatki_object.hr_avg,
                            podatki_object.hr_max,
                            podatki_object.hr_min,
                            podatki_object.altitude_avg,
                            podatki_object.altitude_max,
                            podatki_object.altitude_min,
                            podatki_object.ascent,
                            podatki_object.descent,
                            podatki_object.steps,
                            podatki_object.num_hills,
                            podatki_object.avg_altitude,
                            podatki_object.avg_ascent,
                            podatki_object.distance_hills,
                            podatki_object.hills_share])

    csvfile.close()

end = time.time()
temp = end-start
print(temp)
hours = temp//3600
temp = temp - 3600*hours
minutes = temp//60
seconds = temp - 60*minutes
print('%d:%d:%d' %(hours,minutes,seconds))