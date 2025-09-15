import numpy as np
data = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(1,2,3,4))
time_data = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, dtype=str, usecols=(0))
temp = data[:,0]
distance = data[:,1]
battery = data[:,2]
humidity = data[:,3]

print("\n--- Sensor Data Preview ---")
print("Temperature:", temp)
print("Distance:", distance)
print("Battery:", battery)
print("Humidity:", humidity)

print("\n--- Averages ---")
print("Humidity Mean:", np.mean(humidity))
print("Temperature Mean:", np.mean(temp))
print("Distance Mean:", np.mean(distance))
print("Battery Mean:", np.mean(battery))

print("\n--- Maximum Values ---")
print("Max Humidity:", max(humidity))
print("Max Temperature:", max(temp))
print("Max Distance:", max(distance))
print("Max Battery:", max(battery))

print("\n--- Index of Maximum ---")
print("Humidity Max Index:", np.argmax(humidity))
print("Temperature Max Index:", np.argmax(temp))
print("Distance Max Index:", np.argmax(distance))
print("Battery Max Index:", np.argmax(battery))

time_of_max_temp = time_data[np.argmax(temp)]
print("\nTime of Highest Temperature:", time_of_max_temp)

battery_low_count = np.sum(battery < 30)
print("Battery readings below 30%:", battery_low_count)

output = [
    ["Temperature_Avg", np.mean(temp)],
    ["Temperature_Min", np.min(temp)],
    ["Temperature_Max", np.max(temp)],

    ["Distance_Avg", np.mean(distance)],
    ["Distance_Min", np.min(distance)],
    ["Distance_Max", np.max(distance)],

    ["Battery_Avg", np.mean(battery)],
    ["Battery_Min", np.min(battery)],
    ["Battery_Max", np.max(battery)],
    
    ["Time_of_Max_Temp", time_of_max_temp],
    ["Battery_Low_Count", battery_low_count]
]

np.savetxt("sensor_results.csv", output, delimiter=",", fmt='%s')
print("\nResults saved to sensor_results.csv")
