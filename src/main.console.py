import numpy as np
import random
import time

height = 70
width = 80

nb_turns = 300


def random_cell(max_x, max_y):
    return [
        random.randint(0, max_x - 1),
        random.randint(0, max_y - 1),
    ]


mid_height = int(height / 2)
mid_width = int(width / 2)

aliveCells = [
    [mid_width- 1 , mid_height],
    [mid_width, mid_height - 1],
    [mid_width - 1, mid_height + 1],
    [mid_width, mid_height + 1],
    [mid_width + 1, mid_height + 1],

    [mid_width - 1, mid_height-10],
    [mid_width, mid_height-10],
    [mid_width + 1, mid_height-10],
]

nbCells = height * width
T = np.empty([height, width])

T.fill(0)

for aliveCell in aliveCells:
    T[aliveCell[1], aliveCell[0]] = 1


def display_row(array):
    result = []
    for cell in array:
        result.append((' X ', ' - ')[cell != 1])
    print(''.join(result))


def display_board(nd_array):
    for row in nd_array:
        display_row(row)


def surrounding_cells(nd_array, x, y):
    missing_top = y == 0
    missing_bottom = y == height - 1
    missing_left = x == 0
    missing_right = x == width - 1

    a = []
    if not missing_left:
        a.append(x - 1)
    a.append(x)
    if not missing_right:
        a.append(x + 1)


    b = []
    if not missing_top:
        b.append(y - 1)
    b.append(y)
    if not missing_bottom:
        b.append(y + 1)

    mask = np.ix_(b, a)

    sub_arr = nd_array[mask]

    if missing_left:
        sub_arr = np.insert(sub_arr, [0], [0], axis=1)

    if missing_right:
        sub_arr = np.insert(sub_arr, [2], [0], axis=1)

    if missing_top:
        sub_arr = np.insert(sub_arr, [0], [0, 0, 0], axis=0)

    if missing_bottom:
        sub_arr = np.append(sub_arr, [[0, 0, 0]], axis=0)

    return sub_arr


def new_cell_state(sub_arr):
    nb_ones = (sub_arr == 1).sum()
    if sub_arr[1][1] == 0:
        if nb_ones == 3:
            return 1
        return 0

    nb_ones = nb_ones - 1
    if nb_ones > 3 or nb_ones < 2:
        return 0

    return 1


def process_board(board):
    new_board = np.copy(board);
    for y in range(0, height):
        for x in range(0, width):
            new_state = new_cell_state(surrounding_cells(board, x, y))
            new_board[y][x] = new_state

    return new_board;


display_board(T)
for turn in range(0, nb_turns - 1):
    T = process_board(T)
    print('turn ', turn)
    display_board(T)
