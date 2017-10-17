from proj import same_game
from search import compare_searchers, depth_first_tree_search,astar_search,greedy_best_first_graph_search

""" Problemas do enunciado"""

problems=[]
problems.append(same_game([[1,2,1,2,1],[2,1,2,1,2],[1,2,1,2,1],[2,1,2,1,2]]))
problems.append(same_game([[1,2,2,3,3],[2,2,2,1,3],[1,2,2,2,2],[1,1,1,1,1]]))
problems.append(same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2], [2,2,2,2],[3,1,2,3],[2,3,2,3],[5,1,1,3],[4,5,1,2]]))
problems.append(same_game([[3,1,3,2],[1,1,1,3],[1,3,2,1],[1,1,3,3],[3,3,1,2], [2,2,2,2],[3,1,2,3],[2,3,2,3],[2,1,1,3],[2,3,1,2]]))
problems.append(same_game([[1,1,5,3],[5,3,5,3],[1,2,5,4],[5,2,1,4],[5,3,5,1], [5,3,4,4],[5,5,2,5],[1,1,3,1],[1,2,1,3],[3,3,5,5]]))

""" Cabecalho """
header=[]
header.append("Search")
for i in range(1,6):
    header.append("Example"+str(i))

#compare_searchers(problems , header,[depth_first_tree_search,astar_search,greedy_best_first_graph_search])

print(astar_search(same_game([[1,1,5,3],[5,3,5,3],[1,2,5,4],[5,2,1,4],[5,3,5,1],[5,3,4,4],[5,5,2,5],[1,1,3,1],[1,2,1,3],[3,3,5,5]])))
