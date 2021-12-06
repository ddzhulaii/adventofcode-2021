from typing import List
from collections import defaultdict

def read_input(filename: str):
    with open(filename, "r") as inputfile:
        data = inputfile.read()
    return list(map(lambda x: int(x.replace("\n", "")), data.split(",")))


def reproduce_lanternfish(initial_state: List[int], days_to_reproduce: int):
    state_counter = defaultdict(lambda: 0)
    for days in set(initial_state):
        state_counter[days] += initial_state.count(days)
    fish_counter = len(initial_state)

    for _ in range(days_to_reproduce):
        new = state_counter.get(0, 0)  # count newborns
        fish_counter += new
        state_counter[0] = 0  # drop counter for "parents" to zero
        for i in range(9):
            state_counter[i] = state_counter.get(i+1, 0)  # update counter for those who have 1+ days left
        state_counter[8] += new  # update counter for newborns
        state_counter[6] += new  # update counter for "parents"
    return fish_counter


if __name__ == "__main__":
    data = read_input("input.txt")
    print(f"Part 1 Answer: {reproduce_lanternfish(data, 80)}\nPart 2 Answer: {reproduce_lanternfish(data, 256)}")
