from dfs import DFS
from bfs import BFS
from greedy import GREEDY
from astar import ASTAR
import argparse

rooms_graph = {
    'A':{'C':{'weight': 2}},
    'B':{'C':{'weight': 1}, 'D':{'weight': 2}},
    'C':{'B':{'weight': 1}, 'G':{'weight': 2}},
    'D':{'B':{'weight': 2}, 'E':{'weight': 1.5}},
    'E':{'D':{'weight': 1.5}, 'F':{'weight':1.5}},
    'F':{'E':{'weight': 1.5}, 'J':{'weight': 2}},
    'G':{'C':{'weight': 2}, 'K':{'weight': 1}, 'H':{'weight': 2}},
    'H':{'G':{'weight': 2}, 'K':{'weight': 2}, 'I':{'weight': 2}, 'L':{'weight': 2.5}},
    'I':{'H':{'weight': 2}, 'J':{'weight': 2}},
    'J':{'F':{'weight': 2}, 'I':{'weight': 2}, 'M':{'weight': 1.5}},
    'K':{'G':{'weight': 1}, 'H':{'weight': 2}, 'N':{'weight': 1.5}},
    'L':{'H':{'weight': 2.5}, 'M':{'weight': 2}},
    'M':{'J':{'weight': 1.5}, 'L':{'weight': 2}, 'P':{'weight': 2.5}},
    'N':{'K':{'weight': 1.5}, 'O':{'weight': 1.5}, 'Q':{'weight': 2}},
    'O':{'N':{'weight': 1.5}, 'P':{'weight': 3}},
    'P':{'M':{'weight': 2.5}, 'O':{'weight': 3}, 'T':{'weight': 1.5}},
    'Q':{'N':{'weight': 2}, 'R':{'weight': 1.5}},
    'R':{'Q':{'weight': 1.5}, 'S':{'weight': 1}},
    'S':{'R':{'weight': 1}, 'T':{'weight': 1.5}},
    'T':{'S':{'weight': 1.5}, 'P':{'weight': 1.5}, 'U':{'weight': 1.5}},
    'U':{'T':{'weight': 1.5}}
}

rooms_coords = {
    'A' : (2,13),
    'B' : (1,10),
    'C' : (3,10),
    'D' : (2,7),
    'E' : (2,4),
    'F' : (2,1),
    'G' : (5,12),
    'H' : (6,9),
    'I' : (5,6),
    'J' : (5,2),
    'K' : (7,12),
    'L' : (8,6),
    'M' : (8,2),
    'N' : (10,12),
    'O' : (10,9),
    'P' : (11,4),
    'Q' : (14,12),
    'R' : (14,9),
    'S' : (14,7),
    'T' : (14,4),
    'U' : (14,1)
}

def manhattan_d(end):
    manhattan_distance = {}
    for key, value in rooms_coords.items():
        manhattan_distance[key] = abs(value[0] - rooms_coords[end][0]) + abs(value[1] - rooms_coords[end][1])
    return manhattan_distance

parser = argparse.ArgumentParser()
parser.add_argument('--alg', type=str, default='bfs')
parser.add_argument('--begin', type=str, default='A')
parser.add_argument('--end', type=str, default='U')
args = parser.parse_args()

bfs = BFS()
dfs = DFS()
greedy = GREEDY()
astar = ASTAR()

algs = {
    'bfs': bfs, 
    'dfs': dfs,
    'greedy': greedy,
    'astar': astar
}

manhattan = manhattan_d(args.end)


if(args.alg == 'greedy' or args.alg == 'astar'):
    algs[args.alg]._call(manhattan, rooms_graph, args.begin, args.end)
else:
    algs[args.alg]._call(rooms_graph, args.begin, args.end)