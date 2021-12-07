from numpy import mean, median, floor, ceil

def read_input(filename):
    with open(filename, "r") as inputfile:
        data = inputfile.read()
    return list(map(lambda x: int(x.replace("\n", "")), data.split(",")))


def count_quadratic_fuel(x, a):
    return abs(x - a) * (abs(x - a) + 1) / 2


def count_optimal_fuel(data, isquadratic=False):
    try:
        assert isquadratic
        mu = mean(data)
        return min(
            sum([count_quadratic_fuel(x, int(floor(mu))) for x in data]),
            sum([count_quadratic_fuel(x, int(ceil(mu))) for x in data]),
        )
    except AssertionError:
        ceil_med, floor_med = ceil(median(data)), floor(median(data))
        if ceil_med == floor_med:
            return sum([abs(x - ceil_med) for x in data])
        return min(
            sum([abs(x - ceil_med) for x in data]),
            sum([abs(x - floor_med) for x in data]),
        )


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1 Answer: {count_optimal_fuel(data, isquadratic=False)}\nPart 2 Answer: {count_optimal_fuel(data, isquadratic=True)}")
