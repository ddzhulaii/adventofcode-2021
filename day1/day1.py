from typing import List


def diff(arr: List[int]):
    return [n-prev_n for n, prev_n in zip(arr[1:], arr[:-1])]

## Part 1
def count_increase(data: List[int]):
    return len(list(filter(
        lambda x: x > 0,
        diff(data)
    )))

## Part 2
def count_window_increase(data: List[int], w=3):
    return len(list(filter(
        lambda x: x > 0,
        diff([sum(data[i:i+w]) for i in range(len(data)) if i+w <= len(data)]),
    )))


if __name__ == "__main__":
    with open("input.txt", "r") as inputfile:
        data = list(map(
            lambda x: int(x.replace("\n", "")),
            inputfile.readlines()
        ))
    print(f"Part 1 answer: {count_increase(data)}\nPart 2 answer: {count_window_increase(data)}")
