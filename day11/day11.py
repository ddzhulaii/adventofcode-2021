def read_input(filename):
    with open(filename, "r") as inputfile:
        data = inputfile.readlines()
    return [
        list(map(int, list(row.replace("\n", ""))))
        for row in data
    ]


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
        (x-1, y-1),
        (x+1, y-1),
        (x-1, y+1),
        (x+1, y+1),
    ]
    pnts = [validate_point(*pnt, width, height) for pnt in pnts]
    return list(filter(None, pnts))


def get_flash_coords(data):
    return [
        (x, y) for y, row in enumerate(data)
        for x, val in enumerate(row) if val > 9
    ]


def update_flash_matrix(data):
    return [
        [val if val < 10 else 0 for val in row]
        for row in data
    ]


def make_step(data, w, h):
    flash_points = []

    data = [[val+1 for val in row] for row in data]
    flash_coords = get_flash_coords(data)
    flash_points.extend(flash_coords)
    data = update_flash_matrix(data)

    while len(flash_coords) > 0:
        flash_point = flash_coords.pop(0)
        adj_points = get_adjacent_points(*flash_point, w, h)
        # make sure to filter out flashed points
        adj_points = list(filter(lambda x: x not in flash_points, adj_points))
        for x, y in adj_points:
            data[y][x] += 1
        new_flash_coords = get_flash_coords(data)
        data = update_flash_matrix(data)
        flash_coords.extend(new_flash_coords)
        flash_points.extend(new_flash_coords)
    return (data, flash_points)


def count_flashes(data, num_steps=100):
    width, height = len(data[0]), len(data)
    flash_counter = 0
    for _ in range(num_steps):
        data, flashes = make_step(data, width, height)
        flash_counter += len(flashes)
    return (flash_counter, width, height)


def get_all_flashes_step(data, w, h):
    step_counter = 0

    data, flashes = make_step(data, w, h)
    step_counter += 1

    while len(flashes) != (w * h):
        data, flashes = make_step(data, w, h)
        step_counter += 1

    return step_counter


if __name__ == "__main__":
    inp = read_input("input.txt")
    flash_counter, w, h = count_flashes(inp)
    step_counter = get_all_flashes_step(inp, w, h)
    print(f"Part 1 Answer: {flash_counter}\nPart 2 Answer: {step_counter}")
