"""Pedro Caetano 56564; Francisco Henriques 75278"""

import search


# TAI color
# sem cor = 0
# com cor > 0
def get_no_color():
    return 0
def no_color(c):
    return c == 0
def color (c):
    return c > 0

# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
    return (l, c)
def pos_l(pos):
    return pos[0]
def pos_c(pos):
    return pos[1]

# TAI grupo
# tuplo (pos1,...posn)

# TAI board
def print_board(board):
    for line in board:
        linetoPrint="["
        for column in line:
            linetoPrint+=str(column) + ","
        linetoPrint=linetoPrint[:len(linetoPrint)-1]
        linetoPrint+="]"
        print(linetoPrint)
