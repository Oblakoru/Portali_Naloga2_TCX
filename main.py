import csv
import os
from sport_activities_features import TCXFile, IntervalIdentificationByPower, IntervalIdentificationByHeartRate

from PodatkiClass import PodatkiClass
from sport_activities_features.hill_identification import HillIdentification
from sport_activities_features.topographic_features import TopographicFeatures
import time

# Začetek timerja
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

            # Hribi
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

            print("preden")
            print(Top)

            # Za power intervali
            IntervalsPower = IntervalIdentificationByPower(
                activity['distances'],
                activity['timestamps'],
                activity['altitudes'],
                mass=70
            )

            IntervalsPower.identify_intervals()
            # all_intervals_power = IntervalsPower.return_intervals()
            all_intervals_power = IntervalsPower.calculate_interval_statistics()

            #Za heart rate intervali
            IntervalHeart = IntervalIdentificationByHeartRate(
                activity['distances'],
                activity['timestamps'],
                activity['altitudes'],
                activity['heartrates'],
            )
            IntervalHeart.identify_intervals()


            all_intervals_heart = IntervalHeart.calculate_interval_statistics()

            podatki = PodatkiClass(stevecID, integral_metrics['activity_type'], integral_metrics['distance'],
                                   integral_metrics['duration'], integral_metrics['calories'],
                                   integral_metrics['hr_avg'], integral_metrics['hr_max'], integral_metrics['hr_min'],
                                   integral_metrics['altitude_avg'], integral_metrics['altitude_max'],
                                   integral_metrics['altitude_min'], integral_metrics['ascent'],
                                   integral_metrics['descent'], integral_metrics['steps'], num_hills, avg_altitude,
                                   avg_ascent, distance_hills, hills_share,
                                   all_intervals_power["number_of_intervals"], all_intervals_power["min_duration"],
                                   all_intervals_power["max_duration"], all_intervals_power["avg_duration"],
                                   all_intervals_power["min_distance"], all_intervals_power["max_distance"],
                                   all_intervals_power["avg_distance"],
                                   all_intervals_heart["number_of_intervals"],
                                   all_intervals_heart["min_duration_interval"],
                                   all_intervals_heart["max_duration_interval"],
                                   all_intervals_heart["avg_duration_interval"],
                                   all_intervals_heart["min_distance_interval"],
                                   all_intervals_heart["max_distance_interval"],
                                   all_intervals_heart["avg_distance_interval"],
                                   all_intervals_heart["min_heartrate_interval"],
                                   all_intervals_heart["max_heartrate_interval"],
                                   all_intervals_heart["avg_heartrate_interval"]
                                   )

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

listInDatoteka = {"bikingDataPandas.csv": BikingList, "runningDataPandas.csv": RunningList,
                  "otherDataPandas.csv": OtherList}

for datoteka, seznam in listInDatoteka.items():
    with open(datoteka, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            ['id', 'activity_type', 'distance', 'duration', 'calories', 'hr_avg', 'hr_max', 'hr_min', 'altitude_avg',
             'altitude_max', 'altitude_min', 'ascent', 'descent', 'steps',
             'num_hills', 'avg_altitude', 'avg_ascent', 'distance_hills', 'hills_share', 'number_of_intervalsPower',
             'min_durationPower', 'max_durationPower', 'avg_durationPower', 'min_distancePower', 'max_distancePower',
             'avg_distancePower', 'number_of_intervalsHeart',
             'min_duration_intervalHeart', 'max_duration_intervalHeart', 'avg_duration_intervalHeart',
             'min_distance_intervalHeart', 'max_distance_intervalHeart', 'avg_distance_intervalHeart',
             'min_heartrate_intervalHeart', 'max_heartrate_intervalHeart', 'avg_heartrate_intervalHeart'])

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
                                 podatki_object.hills_share,
                                 podatki_object.number_of_intervalsPower,
                                 podatki_object.min_durationPower,
                                 podatki_object.max_durationPower,
                                 podatki_object.avg_durationPower,
                                 podatki_object.min_distancePower,
                                 podatki_object.max_distancePower,
                                 podatki_object.avg_distancePower,
                                 podatki_object.number_of_intervalsHeart,
                                 podatki_object.min_durationHeart,
                                 podatki_object.max_durationHeart,
                                 podatki_object.avg_durationHeart,
                                 podatki_object.min_distanceHeart,
                                 podatki_object.max_distanceHeart,
                                 podatki_object.avg_distanceHeart,
                                 podatki_object.min_heartrateHeart,
                                 podatki_object.max_heartrateHeart,
                                 podatki_object.avg_heartrateHeart]
                                )

    csvfile.close()

end = time.time()
temp = end - start
print(temp)
hours = temp // 3600
temp = temp - 3600 * hours
minutes = temp // 60
seconds = temp - 60 * minutes
print('%d:%d:%d' % (hours, minutes, seconds))
