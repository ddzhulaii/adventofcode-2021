def read_line(line):
    line = line.replace("\n", "")
    start, end = line.split(" -> ")
    start_x, start_y, end_x, end_y = (*start.split(","), *end.split(","))
    return ((int(start_x), int(start_y)), (int(end_x), int(end_y)))


def read_input(filename):
    with open(filename, "r") as inputfile:
        inp = inputfile.readlines()
    return list(map(read_line, inp))


def get_max_coords(coords):
    max_x = max([c[0] for coord in coords for c in coord])
    max_y = max([c[1] for coord in coords for c in coord])
    return max_x, max_y


def get_slope_intercept(start, end):
    if end[0] == start[0]:
        return (None, None)
    elif end[1] == start[1]:
        return (None, None)
    slope = (end[1] - start[1]) / (end[0] - start[0])
    intercept = start[1] - (slope * start[0])

    return (slope, intercept)


def get_line_points(start, end, slope, intercept, isdiagonal):
    is_desc_x = start[0] > end[0]
    is_desc_y = start[1] > end[1]
    points = None
    try:
        assert isdiagonal
        assert slope is not None
        assert intercept is not None
        end_point = end[0]-1 if is_desc_x else end[0]+1
        points = [
            (x, int(slope * x + intercept))
            for x in range(start[0], end_point, -1 if is_desc_x else 1)
        ]
    except AssertionError:
        if end[0] == start[0]:  # x is not changing
            end_point = end[1]-1 if is_desc_y else end[1]+1
            points = [
                (end[0], y)
                for y in range(start[1], end_point, -1 if is_desc_y else 1)
            ]
        elif end[1] == start[1]:  # y is not changing
            end_point = end[0]-1 if is_desc_x else end[0]+1
            points = [
                (x, end[1])
                for x in range(start[0], end_point, -1 if is_desc_x else 1)
            ]
    return points


def update_mat(mat, points):
    for point in points:
        mat[point[1]][point[0]] += 1
    return mat


def calc_vent_mat(data, isdiagonal=False):
    x, y = get_max_coords(data)
    mat = [[0 for _ in range(x+1)] for _ in range(y+1)]
    for line in data:
        m, b = get_slope_intercept(*line)
        pnts = get_line_points(*line, m, b, isdiagonal)
        if pnts is not None:
            update_mat(mat, pnts)
    return mat


if __name__ == "__main__":
    inp = read_input("input.txt")
    vh_mat = calc_vent_mat(inp, isdiagonal=False)
    full_mat = calc_vent_mat(inp, isdiagonal=True)
    vh_mat_intersect_sum = sum([num >= 2 for row in vh_mat for num in row])
    full_mat_intersect_sum = sum([num >= 2 for row in full_mat for num in row])
    print(f"Part 1 Answer: {vh_mat_intersect_sum}\nPart 2 Answer: {full_mat_intersect_sum}")
