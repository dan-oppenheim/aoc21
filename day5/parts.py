def draw_line(map_points, start, end, include_diagonal=False):
    x0, y0 = start
    x1, y1 = end

    dx = 1 if x0 <= x1 else -1
    dy = 1 if y0 <= y1 else -1
    points = []
    if x0 == x1:
        points = zip([x0] * (abs(y0-y1)+1), range(y0, y1+dy, dy))
    elif y0 == y1:
        points = zip(range(x0, x1+dx, dx), [y0] * (abs(x0-x1)+1))
    elif include_diagonal:
        points = zip(range(x0, x1+dx, dx), range(y0, y1+dy, dy))

    for p in points:
        if p in map_points:
            map_points[p] += 1
        else:
            map_points[p] = 1

def point_generator_from_file(input_file):
    for line in input_file:
        start, end = line.split(' -> ')
        start = start.split(',')
        end = end.split(',')
        yield (int(start[0]), int(start[1])), (int(end[0]), int(end[1]))

def count_overlaps(map_points):
    overlaps = 0
    for p, count in map_points.items():
        if count > 1:
            overlaps += 1
    return overlaps

def day1():
    with open('input.txt') as input_file:
        map_points = {}
        for start, end in point_generator_from_file(input_file):
            draw_line(map_points, start, end)
        print(f"Without diagonals, there are {count_overlaps(map_points)} overlaps")

def day2():
    with open('input.txt') as input_file:
        map_points = {}
        for start, end in point_generator_from_file(input_file):
            draw_line(map_points, start, end, include_diagonal=True)
        print(f"With diagonals there are {count_overlaps(map_points)} overlaps")


day1()
day2()