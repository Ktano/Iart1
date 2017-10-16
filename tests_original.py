from proj import board_find_groups, board_remove_group, sg_state, same_game, print_board
from search import depth_first_tree_search

def xx_recursive_sort(matrix):
    return sorted(map(sorted, matrix))

test_counter = 1

def test_init(f_name, board_raw):
    global test_counter
    print(f_name, test_counter)
    print('board:')
    print_board(board_raw)
    print()
    
def test_before_assert(obtained):
    print('obtained:')
    print(obtained)
    print()

def test_close(f_name):
    global test_counter
    print(f_name, test_counter, 'Success')
    print()
    test_counter += 1

def test_board_find_groups(board_raw, expected):
    f_name = test_board_find_groups.__name__
    test_init(f_name, board_raw)
    obtained = board_find_groups(board_raw)
    test_before_assert(obtained)
    assert xx_recursive_sort(obtained) == expected, 'expected\n' + str(expected)
    test_close(f_name)

def test_board_remove_group(board_raw, group, expected):
    f_name = test_board_remove_group.__name__
    test_init(f_name, board_raw)
    obtained = board_remove_group(board_raw, group)
    test_before_assert(obtained)
    try:
        assert obtained == expected
    except AssertionError:
        global test_counter
        print(test_counter, 'failed')
        print('expected:')
        print_board(expected)
        raise
    test_close(f_name)

test_board_find_groups(
    [[1,2,1,2,1],[2,1,2,1,2],[1,2,1,2,1],[2,1,2,1,2]], 
    [[(0, 0)], [(0, 1)], [(0, 2)], [(0, 3)], [(0, 4)], [(1, 0)], [(1, 1)], [(1, 2)], [(1, 3)], [(1, 4)], [(2, 0)], [(2, 1)], [(2, 2)], [(2, 3)], [(2, 4)], [(3, 0)], [(3, 1)], [(3, 2)], [(3, 3)], [(3, 4)]])

test_board_find_groups(
    [[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]],
    [[(0, 0)], [(0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (3, 0), (3, 1)], [(0, 2)], [(0, 3)], [(1, 3)], [(2, 1)], [(2, 2)], [(2, 3)], [(3, 2), (3, 3)], [(4, 0), (4, 1)], [(4, 2)], [(4, 3), (5, 0), (5, 1), (5, 2), (5, 3), (6, 2), (7, 2)], [(6, 0)], [(6, 1)], [(6, 3), (7, 3), (8, 3)], [(7, 0), (8, 0), (9, 0)], [(7, 1)], [(8, 1), (8, 2), (9, 2)], [(9, 1)], [(9, 3)]])

test_counter = 1

test_board_remove_group(
    [[1,1,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3],[2,2,3,3,3,3]],
    [[0,0],[0,1]],
    [[0, 0, 3, 3, 3, 3], [2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 3, 3], [2, 2, 3, 3, 3, 3]])

test_board_remove_group(
    [[3,3,0,3,3,3],[2,2,0,3,3,3],[2,2,0,3,3,3],[2,2,1,3,3,3],[2,2,1,3,3,3]],
    [[4,2],[3,2]],
    [[3, 3, 3, 3, 3, 0], [2, 2, 3, 3, 3, 0], [2, 2, 3, 3, 3, 0], [2, 2, 3, 3, 3, 0], [2, 2, 3, 3, 3, 0]])

test_board_remove_group(
    [[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]], 
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (3, 0), (3, 1)], 
    [[0, 0, 0, 2], [0, 0, 3, 3], [0, 0, 2, 1], [3, 3, 3, 3], [3, 3, 1, 2], [2, 2, 2, 2], [3, 1, 2, 3], [2, 3, 2, 3], [2, 1, 1, 3], [2, 3, 1, 2]]) 

test_board_remove_group(
    [[1,3,2,1,2,1,2,2,1,2,2,1,1,3,1],[1,3,3,2,1,2,2,2,3,1,2,1,2,3,1],[1,1,1,2,3,2,3,3,2,2,3,1,1,3,1],[1,2,2,2,3,3,3,3,1,2,1,2,1,3,2],[1,3,1,3,2,2,2,2,3,1,1,2,3,2,1],[1,1,2,2,2,1,1,3,2,1,2,3,1,3,1],[3,1,3,2,2,2,3,3,3,1,3,3,2,1,1],[3,2,1,2,1,3,1,2,1,2,3,1,1,3,3],[2,3,1,2,3,3,1,2,3,3,3,2,1,1,1],[2,2,1,1,2,1,2,2,1,1,3,2,2,2,2]], 
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (6, 1), (2, 1), (2, 2)], 
    [[0, 0, 0, 1, 2, 1, 2, 2, 1, 2, 2, 1, 1, 3, 1], [0, 0, 2, 2, 1, 2, 2, 2, 3, 1, 2, 1, 2, 3, 1], [0, 0, 3, 2, 3, 2, 3, 3, 2, 2, 3, 1, 1, 3, 1], [0, 3, 2, 2, 3, 3, 3, 3, 1, 2, 1, 2, 1, 3, 2], [0, 3, 1, 3, 2, 2, 2, 2, 3, 1, 1, 2, 3, 2, 1], [0, 2, 2, 2, 2, 1, 1, 3, 2, 1, 2, 3, 1, 3, 1], [3, 3, 3, 2, 2, 2, 3, 3, 3, 1, 3, 3, 2, 1, 1], [3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 3, 1, 1, 3, 3], [2, 3, 1, 2, 3, 3, 1, 2, 3, 3, 3, 2, 1, 1, 1], [2, 2, 1, 1, 2, 1, 2, 2, 1, 1, 3, 2, 2, 2, 2]])

test_board_remove_group(
    [[4,4,4,2],[4,4,4,3],[4,4,4,1],[4,4,4,4],[4,4,4,2],[4,4,4,4],[4,4,4,3],[4,4,4,3],[4,4,4,4],[4,4,4,2]], 
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (8, 3), (5, 3), (3, 3)], 
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0], [3, 0, 0, 0], [2, 0, 0, 0]])

assert type(sg_state([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]])) is sg_state , '14 failed' 
test_counter = 1
print(test_counter, '14 passed')

assert sg_state([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]).board == [[3, 1, 3, 2], [1, 1, 1, 3], [1, 3, 2, 1], [1, 1, 3, 3], [3, 3, 1, 2], [2, 2, 2, 2], [3, 1, 2, 3], [2, 3, 2, 3], [2, 1, 1, 3], [2, 3, 1, 2]] , '16 failed' 
test_counter += 1
print(test_counter, '16 passed')

assert type(same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]])) is same_game, '18 failed' 
test_counter += 1
print(test_counter, '18 passed')

assert type(same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]).initial) is sg_state, '20 failed' 
test_counter += 1
print(test_counter, '20 passed')

assert same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]).initial.board == [[3, 1, 3, 2], [1, 1, 1, 3], [1, 3, 2, 1], [1, 1, 3, 3], [3, 3, 1, 2], [2, 2, 2, 2], [3, 1, 2, 3], [2, 3, 2, 3], [2, 1, 1, 3], [2, 3, 1, 2]] , '22 failed' 
test_counter += 1
print(test_counter, '22 passed')

assert xx_recursive_sort(same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]).actions(sg_state([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]))) == [[(0, 1), (1, 0), (1, 1), (1, 2), (2, 0), (3, 0), (3, 1)], [(3, 2), (3, 3)], [(4, 0), (4, 1)], [(4, 3), (5, 0), (5, 1), (5, 2), (5, 3), (6, 2), (7, 2)], [(6, 3), (7, 3), (8, 3)], [(7, 0), (8, 0), (9, 0)], [(8, 1), (8, 2), (9, 2)]] , '24 failed' 
test_counter += 1
print(test_counter, '24 passed')

assert same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]).goal_test(sg_state([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]])) == False , '26 failed' 
test_counter += 1
print(test_counter, '26 passed')

assert same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]).result(sg_state([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]),[(6, 3), (7, 3), (8, 3)]).board == [[3, 1, 3, 0], [1, 1, 1, 0], [1, 3, 2, 0], [1, 1, 3, 2], [3, 3, 1, 3], [2, 2, 2, 1], [3, 1, 2, 3], [2, 3, 2, 2], [2, 1, 1, 2], [2, 3, 1, 2]] , '28 failed' 
test_counter += 1
print(test_counter, '28 passed')

assert depth_first_tree_search(same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]])).state.board == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] , '30 failed' 
test_counter += 1
print(test_counter, '30 passed')

assert xx_invalid_solution([[1,2,1,2,1],[2,1,2,1,2],[1,2,1,2,1],[2,1,2,1,2]],depth_first_tree_search(same_game([[1,2,1,2,1],[2,1,2,1,2],[1,2,1,2,1],[2,1,2,1,2]]))) == False , '32 failed' 
test_counter += 1
print(test_counter, '32 passed')

assert xx_invalid_solution([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]],greedy_search(same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2],[2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]))) == False , '34 failed' 
test_counter += 1
print(test_counter, '34 passed')

assert xx_invalid_solution([[1,1,5,3],[5,3,5,3],[1,2,5,4],[5,2,1,4],[5,3,5,1],[5,3,4,4],[5,5,2,5],[1,1,3,1],[1,2,1,3],[3,3,5,5]],astar_search(same_game([[1,1,5,3],[5,3,5,3],[1,2,5,4],[5,2,1,4],[5,3,5,1],[5,3,4,4],[5,5,2,5],[1,1,3,1],[1,2,1,3],[3,3,5,5]]))) == False , '36 failed' 
test_counter += 1
print(test_counter, '36 passed')
