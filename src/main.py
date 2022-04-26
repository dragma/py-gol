import time
import numpy as np
import random
import tkinter as tk
import time

def current_milli_time():
    return round(time.time() * 1000)

SQUARE_SIZE = 10

height = 100
width = 100

nb_turns = 2


root = tk.Tk()
root.title('Hello world')

my_canvas = tk.Canvas(root, width=width*SQUARE_SIZE, height=height*SQUARE_SIZE, bg='red')
my_canvas.pack()


def random_cell(max_x = width, max_y = height):
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

for i in range(int(height * width / 2)):
    aliveCells.append(random_cell())


nbCells = height * width
T = np.empty([height, width])

T.fill(0)

for aliveCell in aliveCells:
    T[aliveCell[1], aliveCell[0]] = 1
    

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
    return new_board


def display(board, turn): 
    my_canvas.delete("all")
    start = current_milli_time()
    for y, line in enumerate(board):
        for x, cell in enumerate(line):
            x1 = x * SQUARE_SIZE
            y1 = y * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            color=('black', 'white')[cell == 0]
            my_canvas.create_rectangle((x1, y1, x2, y2), fill=color)
    turn += 1
    end = current_milli_time()
    print('turn ', turn, 'took ', end-start, 'ms')
    root.after(10, display, process_board(board), turn)

display(T, 1)

root.mainloop()

