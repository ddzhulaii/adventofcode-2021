from functools import reduce


def read_input(filename):
    with open(filename, "r") as inputfile:
        data = inputfile.readlines()
    return [list(map(int, list(row.replace("\n", "")))) for row in data]


def validate_point(x, y, width, height):
    try:
        assert x >= 0
        assert y >= 0
        assert x < width
        assert y < height
    except AssertionError:
        return None
    return (x, y)


def get_adjacent_points(x, y, width, height):
    pnts = [
        (x-1, y),
        (x, y-1),
        (x+1, y),
        (x, y+1),
    ]
    pnts = [validate_point(*pnt, width, height) for pnt in pnts]
    return list(filter(None, pnts))


def calc_lowest(data):
    lowest, lowest_coords = [], []
    w, h = len(data[0]), len(data)
    for x in range(w):
        for y in range(h):
            val = data[y][x]
            adj_pnts_coords = get_adjacent_points(x, y, w, h)
            adj_vals = [data[y_][x_] for x_, y_ in adj_pnts_coords]
            if sum([val < adj_val for adj_val in adj_vals]) == len(adj_vals):
                lowest.append(val)
                lowest_coords.append((x, y))
    return (lowest, lowest_coords)


def calc_basin(data):
    lowest, lowest_coords = calc_lowest(data)
    w, h = len(data[0]), len(data)
    basin_sizes = [1]*len(lowest)
    basin_pnts = [] + lowest_coords

    for i, (x, y) in enumerate(lowest_coords):
        adj_pnts_coords = get_adjacent_points(x, y, w, h)
        while len(adj_pnts_coords) > 0:
            pnt = adj_pnts_coords.pop(0)
            if data[pnt[1]][pnt[0]] == 9:
                continue
            adj_pnts = get_adjacent_points(*pnt, w, h)
            adj_vals = [data[y_][x_] for x_, y_ in adj_pnts]
            pnt_res = [
                adj_pnt for adj_pnt, val in zip(adj_pnts, adj_vals)
                if (val != 9) & (val > data[pnt[1]][pnt[0]])
            ]
            if pnt not in basin_pnts:
                basin_sizes[i] += 1
                basin_pnts.append(pnt)
                adj_pnts_coords.extend(pnt_res)
    return basin_sizes
        

if __name__ == "__main__":
    inp = read_input("input.txt")
    lowest, _ = calc_lowest(inp)
    basin_sizes = calc_basin(inp)
    print(f"Part 1 Answer: {sum(lowest)+len(lowest)}\nPart 2 Answer: {reduce(lambda x, y: x*y, sorted(basin_sizes)[-3:])}")
