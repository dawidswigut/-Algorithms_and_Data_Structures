# SKOŃCZONE

def get_leftmost_point_index(points):
    leftmost_index = 0
    for i in range(1, len(points)):
        if points[i][0] < points[leftmost_index][0] or (points[i][0] == points[leftmost_index][0] and points[i][1] < points[leftmost_index][1]):
            leftmost_index = i
    return leftmost_index

def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (r[1] - q[1]) * (q[0] - p[0])

def jarvis_algorithm_v1(points):
    if len(points) < 3:
        return points
    hull = []
    leftmost_index = get_leftmost_point_index(points)
    p = leftmost_index
    hull.append(points[p])

    while True:
        q = (p + 1) % len(points)
        for r in range(len(points)):
            if orientation(points[p], points[q], points[r]) > 0:
                q = r
        p = q
        hull.append(points[p])
        if p == leftmost_index:
            break
    return hull

def jarvis_algorithm_v2(points):
    if len(points) < 3:
        return points
    convex_hull = []
    leftmost_point_index = get_leftmost_point_index(points)
    current_point_index = leftmost_point_index
    convex_hull.append(points[current_point_index])

    while True:
        next_point_index = (current_point_index + 1) % len(points)

        for i in range(len(points)):
            if i != current_point_index:
                direction = orientation(points[current_point_index], points[next_point_index], points[i])
                if direction > 0 or (direction == 0 and ((points[i][0] - points[current_point_index][0]) ** 2 + (points[i][1] - points[current_point_index][1]) ** 2) > ((points[next_point_index][0] - points[current_point_index][0]) ** 2 + (points[next_point_index][1] - points[current_point_index][1]) ** 2)):
                    next_point_index = i

        current_point_index = next_point_index
        convex_hull.append(points[current_point_index])
        if current_point_index == leftmost_point_index:
            break
    return convex_hull

def main():
    points = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    print(jarvis_algorithm_v1(points))
    print(jarvis_algorithm_v2(points))

if __name__ == '__main__':
    main()