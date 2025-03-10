# def find_leftmost_point(points):
#     min_x, min_y, index = float('inf'), float('inf'), None
#     for i, (x, y) in enumerate(points):
#         if x < min_x or (x == min_x and y < min_y):
#             min_x, min_y, index = x, y, i
#     return index

# def compute_orientation(p, q, r):
#     return (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])

# def jarvis1(points):
#     p_index = find_leftmost_point(points)
#     start_index = p_index
#     hull = [points[start_index]]

#     while True:
#         q_index = (p_index + 1) % len(points)
#         q = points[q_index]

#         for i in range(len(points)):
#             if compute_orientation(points[p_index], q, points[i]) > 0:
#                 q, q_index = points[i], i

#         hull.append(q)
#         if q_index == start_index:
#             break
#         p_index = q_index

#     return hull

# def jarvis2(points: list):
#     minX = float('inf')
#     minY = float('inf')
#     pIndex = None
#     qIndex = 0
#     result = []

#     for i in range(len(points)):
#         if points[i][0] <= minX and points[i][1] < minY:
#             minX = points[i][0]
#             minY = points[i][1]
#             pIndex = i

#     mostLeftPoint = pIndex
#     result.append(points[mostLeftPoint])
#     while True:
#         try:
#             q = points[pIndex + 1]
#             qIndex = pIndex + 1
#         except IndexError:
#             q = points[0]
#             qIndex = 0
#         for i in range(len(points)):
#             condition = ((q[1] - points[pIndex][1]) * (points[i][0] - q[0])) - ((points[i][1] - q[1]) * (q[0] - points[pIndex][0]))
#             if condition > 0:
#                 q = points[i]
#                 qIndex = i
#             if condition == 0 and (points[pIndex][0] < q[0] < points[i][0]
#                                    or points[i][0] < q[0] < points[pIndex][0]
#                                    or points[pIndex][1] < q[1] < points[i][1]
#                                    or points[i][1] < q[1] < points[pIndex][1]):
#                 q = points[i]
#                 qIndex = i
#         result.append(q)
#         if qIndex == mostLeftPoint:
#             break
#         else:
#             pIndex = qIndex
#     return result

# # Test examples
# points_list = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

# print(jarvis1(points_list))
# print(jarvis2(points_list))

def jarvis1(points: list):
    if len(points) < 3:
        return points

    minX = float('inf')
    minY = float('inf')
    pIndex = None
    result = []

    # Znajdź skrajny lewy punkt (jeśli kilka mają takie same x, to dolny)
    for i in range(len(points)):
        if points[i][0] < minX or (points[i][0] == minX and points[i][1] < minY):
            minX = points[i][0]
            minY = points[i][1]
            pIndex = i

    start = pIndex
    result.append(points[start])
    p = start

    while True:
        q = (p + 1) % len(points)
        for i in range(len(points)):
            # Sprawdź orientację
            if (points[q][1] - points[p][1]) * (points[i][0] - points[q][0]) - (points[i][1] - points[q][1]) * (points[q][0] - points[p][0]) > 0:
                q = i
        p = q
        if p == start:
            break
        result.append(points[p])

    return result

def jarvis2(points: list):
    if len(points) < 3:
        return points

    minX = float('inf')
    minY = float('inf')
    pIndex = None
    result = []

    # Znajdź skrajny lewy punkt (jeśli kilka mają takie same x, to dolny)
    for i in range(len(points)):
        if points[i][0] < minX or (points[i][0] == minX and points[i][1] < minY):
            minX = points[i][0]
            minY = points[i][1]
            pIndex = i

    start = pIndex
    result.append(points[start])
    p = start

    while True:
        q = (p + 1) % len(points)
        for i in range(len(points)):
            # Sprawdź orientację
            condition = (points[q][1] - points[p][1]) * (points[i][0] - points[q][0]) - (points[i][1] - points[q][1]) * (points[q][0] - points[p][0])
            if condition > 0:
                q = i
            elif condition == 0:
                if ((points[i][0] - points[p][0]) ** 2 + (points[i][1] - points[p][1]) ** 2) > ((points[q][0] - points[p][0]) ** 2 + (points[q][1] - points[p][1]) ** 2):
                    q = i
        p = q
        if p == start:
            break
        result.append(points[p])

    return result

# Testowanie dla różnych zestawów punktów
points1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
points2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
list1 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

print("Otoczka dla points1 (jarvis1):", jarvis1(points1))
print("Otoczka dla points2 (jarvis2):", jarvis2(points2))
print("Otoczka dla list1 (jarvis1):", jarvis1(list1))
print("Otoczka dla list1 (jarvis2):", jarvis2(list1))
