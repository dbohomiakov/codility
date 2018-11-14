def solution(A):
    circle_borders = []

    for i, v in enumerate(A):
        events.append((i-v, True))
        events.append((i-v, False))

    events.sort(key=lambda x: (x[0], not x[1]))
    intersections, active_circles = 0, 0

    for _, is_begining in events:
        if is_begining:
            intersections += active_circles
            active_circles += 1
        else:
            active_circles -= 1

        if intersections > 10000000:
            return -1
    return intersections

