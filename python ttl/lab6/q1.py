import numpy as np

data = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

mean = np.mean(data)

median = np.median(data)

from scipy.stats import mode
mode_result = mode(data)
mode_value = mode_result.mode[0]
mode_count = mode_result.count[0]

std_dev = np.std(data)

point1 = np.array([1, 2, 3])
point2 = np.array([4, 5, 6])
euclidean_distance = np.linalg.norm(point1 - point2)

def d4_distance(point1, point2):
    return np.sum(np.abs(point1 - point2))

def d8_distance(point1, point2):
    return np.max(np.abs(point1 - point2))

manhattan_distance = d4_distance(point1, point2)

chebyshev_distance = d8_distance(point1, point2)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode_value, "(count:", mode_count, ")")
print("Standard Deviation:", std_dev)
print("Euclidean Distance:", euclidean_distance)
print("Manhattan Distance (d4):", manhattan_distance)
print("Chebyshev Distance (d8):", chebyshev_distance)