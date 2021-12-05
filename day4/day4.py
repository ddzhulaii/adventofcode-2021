def str2int(s):
    try:
        return int(s.replace("\n", ""))
    except ValueError:
        return None


def is_bingo(board, num_cols=5):
    try:
        row_check = [len(list(filter(lambda x: x is not None, row))) == 0 for row in board]
        assert sum(row_check) == 0
    except AssertionError:
        return True
    try:
        col_check = [
            len(list(filter(lambda x: x is not None, [row[i] for row in board]))) == 0
            for i in range(num_cols)
        ]
        assert sum(col_check) == 0
    except AssertionError:
        return True
    return False


def read_input(filename):
    with open(filename, "r") as inputfile:
        output = inputfile.read().split("\n\n")
        numbers, boards = output[0], output[1:]

    numbers = [int(num) for num in numbers.split(",")]
    boards = [board.replace("  ", " ") for board in boards]
    boards = [[
        list(filter(lambda x: x is not None, [str2int(num) for num in row.split(" ")]))
        for row in board.split("\n")
        ][:5] for board in boards
    ]
    return (numbers, boards)


def play_bingo(numbers, boards, find_winner=True):
    for number in numbers:
        boards = [
            [[None if num == number else num for num in row] for row in board]
            for board in boards
        ]
        bingo = [is_bingo(board) for board in boards]
        try:
            assert find_winner
            if sum(bingo) > 0:
                return (boards[bingo.index(True)], number)
            else:
                continue
        except:
            if sum(bingo) > 0:
                if len(boards) > 1:
                    winners = [i for i, w in enumerate(bingo) if w]
                    boards = [board for i, board in enumerate(boards) if i not in winners] 
                else:
                    return (boards[0], number)
            else:
                continue


if __name__ == "__main__":
    numbers, boards = read_input("input.txt")
    winner_board, winner_number = play_bingo(numbers, boards)
    loser_board, loser_number = play_bingo(numbers, boards, find_winner=False)
    winner_result = sum(list(filter(None, [num for row in winner_board for num in row]))) * winner_number
    loser_result = sum(list(filter(None, [num for row in loser_board for num in row]))) * loser_number
    print(f"Part 1 Answer: {winner_result}\nPart 2 Answer: {loser_result}")

