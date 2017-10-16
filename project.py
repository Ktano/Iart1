from collections import namedtuple, defaultdict, UserList
from operator import attrgetter, itemgetter
from utils import Stack, FIFOQueue
from search import Problem

class color(int):
    """
    a different integer bigger than zero will represent a different color
    """
    NO_COLOR = 0
    #XXX needed?
    def get_no_color(self): return color(color.NO_COLOR)
    def no_color(self): return self == color.NO_COLOR
    def color(self): return self > color.NO_COLOR

no_color = color(color.NO_COLOR)
        
MatrixDimensions = namedtuple('MatrixDimensions', 'lines, columns')

class pos(namedtuple('pos_namedtuple', 'line, column')):
    """
    represents a position in a matrix
    """
    #XXX needed?
    def make_pos(self, l, c): return self._make((l, c))
    def pos_l(self): return self.line
    def pos_c(self): return self.column

    def make_pos_with_line_offset(self, offset): 
        return self._make((self.line+offset, self.column))

    def is_first_line(self):
        return self.line == 0
    def is_last_line(self, dim):
        return self.line == dim.lines - 1

    def of_previous_line(self):
        return self.make_pos_with_line_offset(-1)
    def of_next_line(self):
        return self.make_pos_with_line_offset(+1)


    def adjacent(self, dim):
        """
        return adjacent positions given the dimensions this position is part of in UDLR (Up, Down, Left, Right) order
        """
        l = []
        if self.line > 0:
            l.append(pos(self.line-1, self.column))
        if self.line < dim.lines - 1:
            l.append(pos(self.line+1, self.column))
        if self.column> 0:
            l.append(pos(self.line, self.column-1))
        if self.column < dim.columns - 1:
            l.append(pos(self.line, self.column+1))
        return l

    def is_adjacent(self, other):
        return set(map(abs, self - other)) == {0, 1}

    def adjacencies_intersection(self, other, dim):
        return set(self.adjacent(dim)).intersection(other.adjacent(dim))

    def complex(self):
        return self.line + self.column * 1j

    def __sub__(self, other):
        c = other.complex() - self.complex()
        return tuple(map(int, (c.real, c.imag)))

    def __repr__(self):
        return repr(tuple(self)) 

class group(UserList):
    """
    a list with pos objects that correspond to the same color adjacent pieces in a board
    """

class List(UserList):

    def all_have_value(self, value):
        return all(v == value for v in self)
    def all_do_not_have_value(self, value):
        return all(v != value for v in self)


class Row(List):
    """
    row of a matrix
    """

class Column(List):
    """
    column of a matrix
    """
#TODO useful??

class Cell(namedtuple('cell_namedtuple', 'value, position')):
    """
    
    """
    def __repr__(self):
        return repr(tuple(self)) 
        

class Matrix(UserList):
    """
    Base classe for the same-game board
    """
    def __init__(self, data):
        super().__init__(data)
        self.dimensions = MatrixDimensions(len(self), len(self[0]))
        self.set_columns()

    def at(self, position):
        return self[position.line][position.column]

    def set_value(self, value, position):
        self[position.line][position.column] = value
        self.columns[position.column][position.line] = value

    def set_values(self, value, positions):
        {self.set_value(value, position) for position in positions}
        self.set_columns()

    def swap_value(self, pos0, pos1):
        self[pos0.line][pos0.column], self[pos1.line][pos1.column] = self[pos1.line][pos1.column], self[pos0.line][pos0.column]
        self.columns[pos0.column][pos0.line] = self.at(pos0)
        self.columns[pos1.column][pos1.line] = self.at(pos1)
        
    def set_columns(self):
        self.columns = [Column(self[i][j] for i in range(self.dimensions.lines)) for j in range(self.dimensions.columns)]

    def check_columns(self, value):
        return [index for index,column in enumerate(self.columns) if column.all_have_value(value)]

    def translate_columns(self):
        for j,column in enumerate(self.columns):
            for i,value in enumerate(column):
                self[i][j] = value
            

    def swap_columns(self, j, k):
        for row in self:
            row[j], row[k] = row[k], row[j]
        self.columns[j], self.columns[k] = self.columns[k], self.columns[j]

    def positions_list(self):
        return [pos(i, j) for (i,_) in enumerate(self) for (j,__) in enumerate(self[i])]
    def positions_matrix(self):
        return [[pos(i, j) for (j,__) in enumerate(self[i])] for (i,_) in enumerate(self)]
    def extended(self):
        return [(cell, pos(i, j)) for (i,_) in enumerate(self) for (j,cell) in enumerate(self[i])]

    def cells(self):
        return Matrix(map(Row, [Cell(value, position) for (value,position) in self.extended()]))

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self)

class board_row(Row):
    """
    row of a board
    """
    def __init__(self, data):
        super().__init__(map(color, data))

class board(Matrix):
    def __init__(self, data):
        super().__init__(map(board_row, data))

    def colors(self):
        d = defaultdict(list)
        {d[a].append(b) for a,b in self.extended()}
        return d

    def find_group(self, positions, sort=True):
        """
        dfs with node expansion based on the properties of the board,
        as if a set of adjacent positions of same color in the same-game are each a connected graph
        """
        frontier = Stack()
        
        frontier.append(positions.pop(0))
        frontier_register = set()
        explored = set()
        while frontier:
            #print('frontier', frontier)
            frontier_register.update(frontier)
            position = frontier.pop()
            explored.add(position)
            for p in set(position.adjacent(self.dimensions)).intersection(positions):
                if p not in explored and p not in frontier:
                    frontier.append(p)
            
        return sorted(frontier_register) if sort else list(frontier_register)

    def find_color_groups(self, positions):
        """
        run dfs behaviour on a ever decreasing positions list, and get all the sets of same colored adjacent positions
        """
        groups = list()
        while positions:
            #print('positions', positions)
            group = self.find_group(positions)
            #print('group', group)
            for p in group[1:]:#first is popped off positions inside dfs, works ok because positions are in order, so the first element of group corresponds to the pop(0)
                del positions[positions.index(p)] 
            groups.append(group) 
        #print('groups', groups)
        #print()
        return groups

    def find_groups(self):
        """
        split the positions by colors and for each of these compute the respective groups 
        """
        groups = list()
        colors = self.colors()
        for color,positions in colors.items():
            #print('color', color)
            groups.extend(self.find_color_groups(positions[:]))
        return groups

    def last_column_not_zeros(self):
        for i,column in enumerate(reversed(self.columns)):
            if column.all_do_not_have_value(no_color):
                return self.dimensions.columns - 1 - i
        return self.dimensions.columns - 1

    def check_board(self):
        new_columns = list() 
        for column in self.columns: 
            new_column = Column() 
            for value in column:#XXX abstract and pass functionality to matrix???
                if value != no_color:
                    new_column.append(value)
            new_columns.append( (len(column)-len(new_column))*[no_color] + new_column )
        self.columns = new_columns 
        self.translate_columns()
            
    def remove_group(self, group):
        cp = board(self)
        print('group', group);print('copy');print(cp)
        cp.set_values(no_color, tuple(pos(*p) for p in group))
        print('copy');print(cp)
        no_color_columns = cp.check_columns(no_color)
        print('columns with no color', no_color_columns)
        for index in no_color_columns:
            cp.swap_columns(index, cp.last_column_not_zeros())
        cp.check_board()
    
        for c in cp.columns:
            print(c)
        return cp

def board_find_groups(_board):
    return board(_board).find_groups()

def board_remove_group(_board, group):
    return board(_board).remove_group(group)

class sg_state:
    """
    class that represents state of the problem
    """
    def __init__(self, _board):
        self.board = board(_board)


class same_game(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(sg_state(initial))
        def __lt__(self,b2):
        return self<b2
    def isEmpty(self):
        for l in self.board:
            for c in l:
                if not no_color(c):
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
    def h(self, state):
        return 1