import math

# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 8), (9, 10)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    # Calculate the difference for each coordinate
    x_diff = point2[0] - point1[0]
    y_diff = point2[1] - point1[1]
    return math.sqrt(x_diff**2 + y_diff**2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum Mesafe:", min_distance)
