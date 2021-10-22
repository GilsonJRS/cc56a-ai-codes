from queue import Queue


GOAL = [None, 1, 2, 3, 4, 5, 6, 7, 8]

class GraphNode:
    def __init__(self, state, parent, move):
        self.state = state
        self.parent = parent
        self.move = move
        if(self.state):
            self.str_state = ''.join(str(c) for c in self.state)
    def __str__(self):
        return self.str_state

def is_solvable(state):
    inversions = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if(state[j]!=None and state[i]!=None and state[j]>state[i]):
                inversions+=1
    return (inversions%2 == 0)

def move(state, index_1, index_2):
    state[index_1], state[index_2] = state[index_2], state[index_1]
    return state

def get_possible_states(graphnode):
    blank_index = graphnode.state.index(None)
    possible_states = []

    if(blank_index == 0):
        possible_states.append(GraphNode(move(graphnode.state.copy(), 0, 3), graphnode, 'up'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 0, 1), graphnode, 'left'))    
    elif(blank_index == 1):
        possible_states.append(GraphNode(move(graphnode.state.copy(), 1, 0), graphnode, 'right'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 1, 2), graphnode, 'left'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 1, 4), graphnode, 'up'))
    elif(blank_index == 2):
        possible_states.append(GraphNode(move(graphnode.state.copy(), 2, 1), graphnode, 'right'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 2, 5), graphnode, 'up'))
    elif(blank_index == 3):
        possible_states.append(GraphNode(move(graphnode.state.copy(), 3, 0), graphnode, 'down'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 3, 4), graphnode, 'left'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 3, 6), graphnode, 'up'))
    elif(blank_index == 4):
        possible_states.append(GraphNode(move(graphnode.state.copy(), 4, 1), graphnode, 'down'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 4, 3), graphnode, 'right'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 4, 5), graphnode, 'left'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 4, 7), graphnode, 'up'))
    elif(blank_index == 5):
        possible_states.append(GraphNode(move(graphnode.state.copy(), 5, 2), graphnode, 'down'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 5, 4), graphnode, 'right'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 5, 8), graphnode, 'up'))
    elif(blank_index == 6):
        possible_states.append(GraphNode(move(graphnode.state.copy(), 6, 3), graphnode, 'down'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 6, 7), graphnode, 'left'))
    elif(blank_index == 7):
        possible_states.append(GraphNode(move(graphnode.state.copy(), 7, 4), graphnode, 'down'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 7, 6), graphnode, 'right'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 7, 8), graphnode, 'left'))
    elif(blank_index == 8):
        possible_states.append(GraphNode(move(graphnode.state.copy(), 8, 5), graphnode, 'down'))
        possible_states.append(GraphNode(move(graphnode.state.copy(), 8, 7), graphnode, 'right'))

    return possible_states

def dfs(start):
    visited = set() 

    stack = []
    stack.append(GraphNode(start, None, None))

    while(stack):
        v = stack.pop()
        visited.add(v.str_state)

        if(v.state == GOAL):
            return v
        
        new_states = get_possible_states(v)
        for i in new_states:
            if(i.str_state not in visited):
                stack.append(i)
                visited.add(i.str_state)


#start = [6, 1, 8, 4, None, 2, 7, 3, 5]
start = [None,8,7,6,5,4,3,2,1]
goal = dfs(start)
path = []
while start != goal.state:
    path.insert(0, goal.move)
    goal = goal.parent
print(path)