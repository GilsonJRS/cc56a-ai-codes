from queue import Queue

class BFS:
    def _call(self, graph, start, end):
        visited = list(graph.keys())
        graph_keys = list(graph.keys())
        
        q = Queue()
        q.put([start,graph[start],[start]])

        visited[graph_keys.index(start)] = 0

        while(not q.empty()):
            v = q.get()
            
            for i in list(v[1].keys()):
                if(i==end):
                    path = v[2]+[end]
                    path_cost = 0
                    for j,k in zip(path, path[1:]):
                        path_cost += list(graph[j][k].values())[0]
                    print('Caminho :', path)
                    print('Custo: ', path_cost)
                    return path
                if(visited[graph_keys.index(i)] != 0):
                    q.put([i, graph[i], v[2] + [i]])
                    visited[graph_keys.index(i)] = 0
