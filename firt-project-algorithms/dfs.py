class DFS:
    def _call(self, graph, start, end):
        visited = list(graph.keys())
        graph_keys = list(graph.keys())

        stack = []
        stack.append([start,graph[start],[start]])

        while(len(stack) != 0):
            v = stack.pop()

            if(visited[graph_keys.index(v[0])] == 0):
                continue 

            if(v[0]==end):
                path_cost = 0
                for j,k in zip(v[2], v[2][1:]):
                    path_cost += list(graph[j][k].values())[0]
                print('Caminho: ', v[2])
                print('Custo: ', path_cost)
                return v[2]

            visited[graph_keys.index(v[0])] = 0

            for i in list(v[1].keys()):
                stack.append([i, graph[i], v[2] + [i]])