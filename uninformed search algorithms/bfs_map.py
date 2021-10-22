from queue import Queue
#import networkx as nx
#import matplotlib.pyplot as plt
#from pyvis.network import Network

graph_cities = {
    'Arad':{'Zerind':{'weight':75}, 'Timisoara':{'weight':118}, 'Sibiu':{'weight':140}},
    'Zerind':{'Oradea':{'weight':71}, 'Arad':{'weight':75}},
    'Oradea':{'Zerind':{'weight':71},'Sibiu':{'weight':151}},
    'Sibiu': {'Arad':{'weight':140}, 'Oradea':{'weight':151}, 'Fagaras':{'weight':99}, 'Rimnicu Vilcea':{'weight':80}},
    'Timisoara': {'Arad':{'weight':118}, 'Lugoj':{'weight':111}},
    'Lugoj': {'Mehadia':{'weight':70}, 'Timisoara':{'weight':111}},
    'Mehadia': {'Dobreta':{'weight':75}, 'Lugoj':{'weight':70}},
    'Dobreta': {'Craiova':{'weight':120}, 'Mehadia':{'weight':75}},
    'Craiova': {'Dobreta':{'weight':120}, 'Rimnicu Vilcea':{'weight':146}, 'Pitesti':{'weight':138}},
    'Rimnicu Vilcea': {'Sibiu': {'weight':80}, 'Pitesti':{'weight':97}, 'Craiova':{'weight':146}},
    'Pitesti': {'Rimnicu Vilcea':{'weight':97}, 'Craiova': {'weight':138}, 'Bucharest': {'weight':101}},
    'Fagaras': {'Sibiu':{'weight':99}, 'Bucharest':{'weight':211}},
    'Bucharest': {'Fagaras':{'weight':211}, 'Pitesti':{'weight':101}, 'Giurgiu':{'weight':90}, 'Urziceni':{'weight':85}},
    'Giurgiu': {'Bucharest':{'weight':90}},
    'Urziceni': {'Bucharest': {'weight':85}, 'Hirsova':{'weight':98}, 'Vaslui':{'weight':142}},
    'Hirsova': {'Urziceni': {'weight':98}, 'Eforie': {'weight':86}},
    'Eforie': {'Hirsova': {'weight':86}},
    'Vaslui': {'Urziceni': {'weight':142}, 'Iasi': {'weight':92}},
    'Iasi': {'Vaslui': {'weight':92}, 'Neamt': {'weight':87}},
    'Neamt': {'Iasi': {'weight':87}}
}

def bfs(graph, start, end):
    visited = list(graph.keys())
    graph_keys = list(graph.keys())

    q = Queue()
    q.put([start,graph[start],[start]])

    visited[graph_keys.index(start)] = 0

    while(not q.empty()):
        v = q.get()

        for i in list(v[1].keys()):
            if(i==end):
                print(v[2]+[end])
                return
            if(visited[graph_keys.index(i)] != 0):
                q.put([i, graph[i], v[2] + [i]])
                visited[graph_keys.index(i)] = 0
            
bfs(graph_cities, 'Arad', 'Iasi')
#graph = nx.Graph(graph_cities)

#pos = nx.spring_layout(graph, k=0.15, iterations=20)
#nx.draw_networkx(graph, pos, with_labels=True)

#wei = nx.get_edge_attributes(graph, 'weight')
#nx.draw_networkx_edge_labels(graph, pos, edge_labels=wei)
#plt.show()

#nt = Network('100%', '100%')
#nt.from_nx(graph)
#nt.show('nx.html')