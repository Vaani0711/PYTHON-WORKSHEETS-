import numpy as np

data = np.genfromtxt("robot_path.csv", delimiter=",", skip_header=1)
x = data[:, 0]
y = data[:, 1]

print("\n--- Robot Path Data Preview ---")
print("X positions:", x)
print("Y positions:", y)

dx = np.diff(x)
dy = np.diff(y)
total_distance = np.sum(np.sqrt(dx**2 + dy**2))
print("\nTotal Distance Traveled:", total_distance)

dist_from_origin = np.sqrt(x**2 + y**2)
max_distance = np.max(dist_from_origin)
farthest_point = (x[np.argmax(dist_from_origin)], y[np.argmax(dist_from_origin)])
print("Farthest Distance from Origin:", max_distance)
print("Farthest Point (x, y):", farthest_point)

positions = np.column_stack((x, y))
unique_positions = np.unique(positions, axis=0)
revisited = len(unique_positions) != len(positions)
print("Revisited Any Position?:", revisited)

output = [
    ["Total_Distance_Traveled", total_distance],
    ["Farthest_Distance_From_Origin", max_distance],
    ["Farthest_Point_X", farthest_point[0]],
    ["Farthest_Point_Y", farthest_point[1]],
    ["Revisited_Position", revisited]
]

np.savetxt("robot_path_results.csv", output, delimiter=",", fmt='%s')
print("\nResults saved to robot_path_results.csv")
