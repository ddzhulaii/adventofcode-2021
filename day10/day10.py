from functools import reduce
from numpy import median

PENALTY_POINTS = {
    "}": 1197,
    ")": 3,
    ">": 25137,
    "]": 57,
}
COMPLETION_POINTS = {
    "}": 3,
    "]": 2,
    ")": 1,
    ">": 4,
}


def read_input(filename):
    with open(filename, "r") as inputfile:
        data = inputfile.readlines()
    return [row.replace("\n", "") for row in data]


def is_matching(open_char, close_char):
    if (open_char == "[") & (close_char == "]"):
        return True
    elif (open_char == "{") & (close_char == "}"):
        return True
    elif (open_char == "(") & (close_char == ")"):
        return True
    elif (open_char == "<") & (close_char == ">"):
        return True
    else:
        return False


def get_close_char(open_char):
    if open_char == "(":
        return ")"
    elif open_char == "[":
        return "]"
    elif open_char == "{":
        return "}"
    else:
        return ">"


def get_completion_score(chars):
    scores = [COMPLETION_POINTS[get_close_char(char)] for char in chars][::-1]
    return reduce(lambda x, y: x*5 + y, scores)


def is_corrupted_line(line):
    open_chars = []

    for char in line:
        if char in ["{", "(", "[", "<"]:
            open_chars.append(char)
        else:
            if len(open_chars) < 1:
                return (open_chars, PENALTY_POINTS[char])
            else:
                open_char = open_chars.pop()
                is_match = is_matching(open_char, char)
                if is_match:
                    continue
                else:
                    return ([], PENALTY_POINTS[char])
    return (open_chars, 0)


if __name__ == "__main__":
    inp = read_input("input.txt")
    incomplete, corrupted_points = list(zip(*[is_corrupted_line(line) for line in inp]))
    incomplete = [x[0] for x in filter(lambda x: x[1] == 0, zip(incomplete, corrupted_points))]
    incompletion_points = [get_completion_score(chars) for chars in incomplete]
    print(f"Part 1 Answer: {sum(corrupted_points)}\nPart 2 Answer: {int(median(incompletion_points))}")
