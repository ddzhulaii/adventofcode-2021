import bitarray

from bitarray.util import ba2int


def read_input(filename):
    with open(filename, "r") as ofile: 
        return [bitarray.bitarray(elem.replace("\n", "")) for elem in ofile.readlines()]


def count_dim_major_elem(col):
    total = len(col)
    major = int(sum(col))
    return (major / total) >= .5


def count_diagnostic(data): 
    dim = len(data[0]) 
    major_bits = bitarray.bitarray([
        count_dim_major_elem([record[i] for record in data])
        for i in range(dim)
    ])
    minor_bits = bitarray.bitarray([not bit for bit in major_bits])
    return (
        ba2int(major_bits),
        ba2int(minor_bits),
    )


def filter_numbers(data, ismajor=True):
    dim = len(data[0])
    for i in range(dim):
        try:
            assert len(data) > 1
        except AssertionError:
            return ba2int(data[0])
        target_bit = count_dim_major_elem([record[i] for record in data])
        target_bit = not target_bit if not ismajor else target_bit
        data = list(filter(lambda x: x[i] == target_bit, data))
    return ba2int(data[0])


if __name__ == "__main__":
    inp = read_input("input.txt")
    epsilon, gamma = count_diagnostic(inp)
    oxygen = filter_numbers(inp)
    scrubber = filter_numbers(inp, False)
    print(f"Part 1 answer: {epsilon*gamma}\nPart 2 answer: {oxygen*scrubber}")
