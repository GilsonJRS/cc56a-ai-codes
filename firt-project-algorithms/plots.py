import networkx as nx
import matplotlib.pyplot as plt

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

graph = nx.Graph(rooms_graph)

pos = {
    'A' : (2,12),
    'B' : (2,10),
    'C' : (4,10),
    'D' : (2,7),
    'E' : (2,4),
    'F' : (2,1),
    'G' : (5,12),
    'H' : (5,8),
    'I' : (5,6),
    'J' : (5,1),
    'K' : (7,12),
    'L' : (8,6),
    'M' : (8,1),
    'N' : (10,12),
    'O' : (10,9),
    'P' : (10,4),
    'Q' : (14,12),
    'R' : (14,9),
    'S' : (14,7),
    'T' : (14,4),
    'U' : (14,1)
}

colors = [
    'red',
    'blue',
    'red',
    'blue',
    'blue',
    'blue',
    'red',
    'red',
    'blue',
    'blue',
    'blue',
    'red',
    'red',
    'blue',
    'blue',
    'red',
    'blue',
    'blue',
    'blue',
    'red',
    'red'
]
#pos = nx.spectral_layout(graph, scale=2)
#plt.figure(figsize=(15,15))
nx.draw_networkx(graph, pos, with_labels=True, node_color=colors)

wei = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=wei)
plt.tight_layout()
plt.savefig('grafo_sala.png')
plt.show()