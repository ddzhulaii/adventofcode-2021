def read_input(filename):
    with open(filename, "r") as input_file:
        for line in input_file.readlines():
            yield line.replace("\n", "").split(" ")


def count_move(direction, step, x, y, aim):
    if direction == "forward":
        return (x+int(step), y+aim*int(step), aim)
    elif direction == "up": 
        return (x, y, aim-int(step))
    else: 
        return (x, y, aim+int(step))


if __name__ == "__main__":
    x, y, aim = 0, 0, 0
    for move in read_input("input.txt"): 
        x, y, aim = count_move(*move, x, y, aim)
    print(f"Part 1 answer: {x*aim}\nPart 2 answer: {x*y}")
