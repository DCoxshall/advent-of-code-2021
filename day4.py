# Part 1

import copy
from typing import BinaryIO

test_boards = [
    [[22, 13, 17, 11, 0],
     [8, 2, 23, 4, 24],
     [21, 9, 14, 16, 7],
     [6, 10, 3, 18, 5],
     [1, 12, 20, 15, 19]],
    [[3, 15, 0, 2, 22],
     [8, 18, 13, 17, 5],
     [19, 8, 7, 25, 23],
     [20, 11, 10, 24, 4],
     [14, 21, 16, 12, 6]],
    [[14, 21, 17, 24, 4],
     [10, 16, 15, 9, 19],
     [18, 8, 23, 26, 20],
     [22, 11, 13, 6, 5],
     [2, 0, 12, 3, 7]]]

test_input = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
              16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

input_file = open("day4_input.txt", "r")
real_input = input_file.readline()

board_dump = input_file.readlines()[1:]


pntr = 0
temp_list = []
real_boards = []


def finished(board):
    complete = False
    for i in board:
        row_complete = True
        for j in i:
            if j != "#":
                row_complete = False
        if row_complete == True:
            complete = True

    board = list(zip(*board[::-1]))

    for i in board:
        row_complete = True
        for j in i:
            if j != "#":
                row_complete = False
        if row_complete == True:
            complete = True

    return complete


# Converts board_dump into usable array of numbers
temp_list = []
for i in board_dump:
    if i == "\n":
        real_boards.append([j[:-1] for j in temp_list])
        temp_list = []
    else:
        temp_list.append(i)
real_boards.append(temp_list)
for i in range(5):
    if real_boards[-1][i][-1] == "\n":
        real_boards[-1][i] = real_boards[-1][i][:-1]
for i in range(len(real_boards)):
    real_boards[i] = [x.split() for x in real_boards[i]]
for i in range(len(real_boards)):
    for j in range(5):
        for k in range(5):
            real_boards[i][j][k] = int(real_boards[i][j][k])

marking_boards = copy.deepcopy(real_boards)

real_input = [int(x) for x in real_input.split(",")]


def solve(real_input):
    found_last_board = False
    print(real_input)
    while True:
        if found_last_board:
            break
        i = real_input[0]
        real_input = real_input[1:]
        for j in range(len(marking_boards)):
            for k in range(5):
                for l in range(5):
                    if marking_boards[j] != "deletedBoard":
                        if marking_boards[j][k][l] == i:
                            marking_boards[j][k][l] = "#"
                            if finished(marking_boards[j]):
                                marking_boards[j] = "deletedBoard"
            if (len([x for x in marking_boards if x != "deletedBoard"]) == 1) and not found_last_board:
                final_board_index = j
                final_board = [
                    i for i in marking_boards if i != "deletedBoard"][0]
                found_last_board = True

    for i in real_input:
        for j in range(len(final_board)):
            for k in range(5):
                if final_board[j][k] == i:
                    final_board[j][k] = "#"
                    if finished(final_board):
                        final_number = i
                        return (final_board_index, final_number)


result = solve(real_input)
score = result[-1]
marking_boards = [i for i in marking_boards if i != "deletedBoard"]
final_board = marking_boards[0]
temp = 0
for i in final_board:
    for j in i:
        if type(j) == int:
            temp += j
print(result)
print(score)
print(temp)
print(score * temp)
print(marking_boards)
