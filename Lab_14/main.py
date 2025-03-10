#nieskonczone

# import matplotlib.pyplot as plt

def jarvis1(points: list):
    minX = float('inf')
    minY = float('inf')
    pIndex = None
    qIndex = 0
    result = []

    for i in range(len(points)):
        if points[i][0] <= minX and points[i][1] < minY:
            minX = points[i][0]
            minY = points[i][1]
            pIndex = i

    mostLeftPoint = pIndex
    result.append(points[mostLeftPoint])
    while True:
        try:
            q = points[pIndex + 1]
            qIndex = pIndex + 1
        except IndexError:
            q = points[0]
            qIndex = 0
        for i in range(len(points)):
            condition = ((q[1] - points[pIndex][1]) * (points[i][0] - q[0])) - ((points[i][1] - q[1]) * (q[0] - points[pIndex][0]))
            if condition > 0:
                q = points[i]
                qIndex = i
        result.append(q)
        if qIndex == mostLeftPoint:
            break
        else:
            pIndex = qIndex
    return result

def jarvis2(points: list):
    minX = float('inf')
    minY = float('inf')
    pIndex = None
    qIndex = 0
    result = []

    for i in range(len(points)):
        if points[i][0] <= minX and points[i][1] < minY:
            minX = points[i][0]
            minY = points[i][1]
            pIndex = i

    mostLeftPoint = pIndex
    result.append(points[mostLeftPoint])
    while True:
        try:
            q = points[pIndex + 1]
            qIndex = pIndex + 1
        except IndexError:
            q = points[0]
            qIndex = 0
        for i in range(len(points)):
            condition = ((q[1] - points[pIndex][1]) * (points[i][0] - q[0])) - ((points[i][1] - q[1]) * (q[0] - points[pIndex][0]))
            if condition > 0:
                q = points[i]
                qIndex = i
            if condition == 0 and (points[pIndex][0] < q[0] < points[i][0]
                                   or points[i][0] < q[0] < points[pIndex][0]
                                   or points[pIndex][1] < q[1] < points[i][1]
                                   or points[i][1] < q[1] < points[pIndex][1]):
                q = points[i]
                qIndex = i
        result.append(q)
        if qIndex == mostLeftPoint:
            break
        else:
            pIndex = qIndex
    return result

list1 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

print(jarvis1(list1))
print(jarvis2(list1))