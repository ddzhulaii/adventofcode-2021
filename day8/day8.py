from collections import Counter
from typing import Dict, List


def read_input(filename):
    with open(filename, "r") as inputfile:
        data = [
            line.replace("\n", "").split("|")
            for line in inputfile.readlines()
        ]
    return (
        [row[0][:-1].split(" ") for row in data],
        [row[1][1:].split(" ") for row in data],
    )


def decode_signal_pattern(patterns: List[str]):
    codes = {}
    for pattern in patterns:
        if len(pattern) == 2:
            codes[1] = set(pattern)
        elif len(pattern) == 3:
            codes[7] = set(pattern)
        elif len(pattern) == 4:
            codes[4] = set(pattern)
        elif len(pattern) == 7:
            codes[8] = set(pattern)
    return codes


def process_complex_pattern(codes: Dict[int, set], patterns: List[str]):
    dig5 = [elem for elem in patterns if len(elem) == 5]
    dig5 = [sorted(x) for x in dig5]

    counter = Counter([elem for row in dig5 for elem in row])
    elements = [elem for elem, c in counter.items() if c == 2]
    three = [row for row in dig5 if (elements[0] in row) & (elements[1] in row)][0]
    dig5, elements5 = (
        [x for x in dig5 if x != three],
        [elem for elem, c in counter.items() if c == 1],
    )

    dig6 = [elem for elem in patterns if len(elem) == 6]
    dig6 = [sorted(x) for x in dig6]
    counter = Counter([elem for row in dig6 for elem in row])
    elements = [elem for elem, c in counter.items() if (c != 3) & (elem not in elements5)]
    nine = [row for row in dig6 if (elements[0] in row) & (elements[1] in row)][0]
    dig6, elements6 = (
        [x for x in dig6 if x != nine],
        [elem for elem, c in counter.items() if (c != 3)],
    )

    five = [row for row in dig5 if list(set(elements5) - set(elements6))[0] in row][0]
    two = [row for row in dig5 if row != five][0]
    zero = [row for row in dig6 if len(set(row).intersection(codes[4] - codes[1])) == 1][0]
    six = [row for row in dig6 if len(set(row).intersection(codes[4] - codes[1])) == 2][0]

    codes[0], codes[2], codes[3], codes[5], codes[6], codes[9] = (
        set(zero), set(two), set(three), set(five), set(six), set(nine),
    )
    return codes


def decode_number(codes: Dict[int, set], encoded_number: List[str]):
    encoded_number = [set(val) for val in encoded_number]
    encoded_number = [k for val in encoded_number for k, v in codes.items() if val == v]
    return int("".join(list(map(str, encoded_number))))


if __name__ == "__main__":
    pattern, output = read_input("input.txt")
    simple_pattern = list(map(decode_signal_pattern, pattern))
    complex_pattern = list(map(lambda x: process_complex_pattern(*x), zip(simple_pattern, pattern)))
    output_numbers = list(map(lambda x: decode_number(*x), zip(complex_pattern, output)))
    print(f"Part 1 Answer: {sum([len(pat) in [2, 3, 4, 7] for row in output for pat in row])}\nPart 2 Answer: {sum(output_numbers)}")
