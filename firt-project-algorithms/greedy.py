from queue import PriorityQueue

class GraphNode:
    def __init__(self, state, parent, path_cost):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
    def __str__(self):
        return self.state
    def __eq__(self, other):
        return self.state == other.state
    def __lt__(self, other):
        return self.state < other.state

class GREEDY:

    def _call(self, manhattan, graph, start, end):
        self.graph = graph

        visited = set()

        queue = PriorityQueue()
        queue.put((0, GraphNode(start, None, 0))) 
        v=None
        while(not queue.empty()):
            _, v = queue.get()
            visited.add(v.state)

            if(v.state == end):
                break
            
            new_states = self.get_possible_states(v)
            for i in new_states:
                if(i.state not in visited):
                    queue.put((manhattan[i.state], i))
                    visited.add(i.state)
        path = []
        cost = v.path_cost
        while start != v.state:
            path.insert(0, v.state)
            v = v.parent
        path.insert(0, start)
        print('Caminho: ', path)
        print('Custo: ', cost)
        return path

    def get_possible_states(self, room):
        possible_states = []
        for i in self.graph[room.state].keys():
            possible_states.append(GraphNode(i, room, room.path_cost + list(self.graph[room.state][i].values())[0]))
        return possible_states
