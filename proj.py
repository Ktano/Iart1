"""Pedro Caetano 56564; Francisco Henriques 75278"""

import copy

from search import Problem


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
def adjancent(pos1,pos2):
    ldif=abs(pos_l(pos1)-pos_l(pos2))
    cdif=abs(pos_c(pos1)-pos_c(pos2))
    if ldif==1 and cdif==0 :
        return True
    elif ldif==0 and cdif==1:
        return True
    else:
        return False


# TAI grupo
# tuplo (pos1,...posn)

def group_adjancent(group, pos):
    for groupPos in group:
        if(adjancent(groupPos,pos)):
            return True
    return False

# TAI board
# list of lists with color [[c1..cn],...,[c1..cn]]
def print_board(board):
    for line in board:
        linetoPrint="["
        for column in line:
            linetoPrint+=str(column) + ","
        linetoPrint=linetoPrint[:len(linetoPrint)-1]
        linetoPrint+="]"
        print(linetoPrint)

# returns the colour of a posistion in the board/
def get_color(board, pos):
    return board[pos_l(pos)][pos_c(pos)]

#def creates a group from a position
def create_group (board, pos):
    group=[pos]
    q=[pos]
    c=get_color(board,pos)
    while q!=[]:
        cpos=q.pop(0)
        #checks top cell
        npos=make_pos(pos_l(cpos)-1,pos_c(cpos))
        if 0<=pos_l(npos)<len(board) and npos not in group and get_color(board,npos)==c:
            group.append(npos)
            q.append(npos)
        #checks bottom cell
        npos=make_pos(pos_l(cpos)+1,pos_c(cpos))
        if 0<=pos_l(npos)<len(board) and npos not in group and get_color(board,npos)==c:
            group.append(npos)
            q.append(npos)
        #checks left cell
        npos=make_pos(pos_l(cpos),pos_c(cpos)-1)
        if 0<=pos_c(npos)<len(board[0]) and npos not in group and get_color(board,npos)==c:
            group.append(npos)
            q.append(npos)
        #checks right cell
        npos=make_pos(pos_l(cpos),pos_c(cpos)+1)
        if 0<=pos_c(npos)<len(board[0]) and npos not in group and get_color(board,npos)==c:
            group.append(npos)
            q.append(npos)
    return group

def board_find_groups(board):
    allgroups=[]
    for l in range(0, len(board)):
        for c in range (0, len(board[0])):
            if no_color(board[l][c]) or cell_in_group(allgroups, make_pos(l,c)):
                continue
            else:
                group=create_group(board,make_pos(l,c))
                allgroups.append(group)
    return allgroups
def cell_in_group(allgroups, pos):
    for group in allgroups:
        for p in group:
            if pos ==p:
                return True
    return False


# removes the provided group from the board and colapses the board
def board_remove_group(board,group):
    newBoard = copy.deepcopy(board)
    for pos in group:
        newBoard[pos_l(pos)][pos_c(pos)]=0
    colapse_lines(newBoard)
    colapse_columns(newBoard)
    return newBoard

#colapses the lines of the board
def colapse_lines(board):
    l=len(board)-1
    c=0
    while l>0:
        while c<len(board[0]):
            if no_color(board[l][c]):
                board[l][c],board[l-1][c]=board[l-1][c],board[l][c]
            c+=1
        l-=1

#colaps the columns of the board
def colapse_columns(board):
    c=0
    while c<len(board):
        if no_color(board[len(board)-1][c]):
            for i in range(0,len(board)): 
                board[i][c],board[i][c+1]=board[i][c+1],board[i][c]
        c+=1

class sg_state:
    def __init__(self,b):
        self.board=b
    def __lt__(self,b2):
        return self<b2
    def isEmpty(self):
        for l in self.board:
            for c in l:
                if no_color(c):
                    return False
        return True
    def result(self,action):
        board=board_remove_group(self.board,action)
        return sg_state(board)
    def groups(self):
        return board_find_groups(self.board)

class same_game(Problem):
    """Models a Same Game Problem as a satisfaction problem.
       A Solution cannot have pieces left on the board."""
    def __init__(self,board):
        super().__init__(sg_state(board))
    def actions(self,state):
        actionlist=[]
        for group in state.groups():
            if len(group)>1:
                actionlist.append(group)
        return actionlist
    def result(self,state,action):
        return state.result(action)
    def goal_test(self, state):
        return state.isEmpty()

