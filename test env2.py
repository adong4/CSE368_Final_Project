import collections
import time
from queue import PriorityQueue
from env2 import State, Node, Problem, childNode, calculate_h
from vis2 import visualize


class Searches:
    def BFS(self, problem):
        # write your code here
        stime = time.time()
        explored = collections.deque()
        toExplore = collections.deque([Node(None, None, 0, problem.initialState, 0)])
        # while goal state not achived and to explore not empty -> keep exploring
        while toExplore:
            # get a node from the front
            x = toExplore.popleft()
            # check if node is goal state
            if problem.goalTest(x.state):
                print("BFS ran for: " + str(time.time() - stime) + " seconds")
                # build the path of nodes from start state to goal state
                path = collections.deque()
                pathNode = x
                while pathNode != None:
                    path.appendleft(pathNode)
                    pathNode = pathNode.parent
                # make the graphs
                visualize(path)
                return x
            # not goal state to add it to explored
            explored.appendleft(x.state)
            # and populate toExplore with the children on the end
            for action in Problem.applicable(problem, x.state):
                child = childNode(x, action, problem, x.depth + 1)
                if child not in toExplore and child.state not in explored:
                    toExplore.append(child)

    def DFS(self, problem):
        # write your code here
        stime = time.time()
        explored = collections.deque()
        toExplore = collections.deque([Node(None, None, 0, problem.initialState, 0)])
        # while goal state not achived and to explore not empty -> keep exploring
        while toExplore:
            # get a node from the front
            x = toExplore.popleft()
            # check if node is goal state
            if problem.goalTest(x.state):
                print("DFS ran for: " + str(time.time() - stime) + " seconds")
                # build the path of nodes from start state to goal state
                path = collections.deque()
                pathNode = x
                while pathNode is not None:
                    path.appendleft(pathNode)
                    pathNode = pathNode.parent
                # make the graphs
                visualize(path)
                return x
            # not goal state to add it to explored
            explored.appendleft(x.state)
            # and populate toExplore with the children on the front
            if x.depth <= 60:
                for action in Problem.applicable(problem, x.state):
                    child = childNode(x, action, problem, x.depth + 1)
                    if child not in toExplore and child.state not in explored:
                        toExplore.appendleft(child)

    import time

    def dijkstra(self, problem):
        starttime = time.time()
        queue = []
        visited = []
        dist = {}
        start = Node(None, None, 0, problem.initialState, 0)
        dist[problem.initialState.toTuple()] = [0, start]
        queue.append(start)
        while queue:
            parent = queue.pop(0)
            depth = parent.depth
            if problem.goalTest(parent.state):
                print("Dijkstra ran for: " + str(time.time() - starttime) + " seconds")
                path = collections.deque()
                pathNode = parent
                while pathNode != None:
                    path.appendleft(pathNode)
                    pathNode = pathNode.parent
                # path.reverse()
                # print(path)
                visualize(path)
                return parent
            visited.append(parent.state)
            for action in problem.applicable(parent.state):
                child = childNode(parent, action, problem, depth)
                if child.state not in visited and child not in queue:
                    queue.append(child)
                    if child.state.toTuple() in dist:
                        if dist[child.state.toTuple()][0] > dist[parent.state.toTuple()][0] + child.cost:
                            dist[child.state.toTuple()] = [dist[parent.state.toTuple()][0] + child.cost, child]
                    else:
                        dist[child.state.toTuple()] = [dist[parent.state.toTuple()][0] + child.cost, child]

    def A_star(self, problem):
        # write your code here
        stime = time.time()
        # explored = collections.deque()
        exploreState = collections.deque()
        toExplore = PriorityQueue()
        toExplore.put((0, Node(None, None, 0, problem.initialState, 0)))
        # while goal state not achived and to explore not empty -> keep exploring
        while toExplore:
            # get a node from the front
            cost, x = toExplore.get()
            # check if node is goal state
            if problem.goalTest(x.state):
                print("BFS ran for: " + str(time.time() - stime) + " seconds")
                # build the path of nodes from start state to goal state
                path = collections.deque()
                pathNode = x
                while pathNode != None:
                    path.appendleft(pathNode)
                    pathNode = pathNode.parent
                # make the graphs
                visualize(path)
                return x
            # not goal state to add it to exploreState
            exploreState.append(x.state)
            # and populate toExplore with the children on the front
            if x.depth <= 60:
                for action in Problem.applicable(problem, x.state):
                    child = Searches.childNodeAstar(x, action, x.cost, problem, x.depth + 1)
                    child.cost += calculate_h(child.state.position, child.state.goalpos)
                    if child.state not in exploreState:
                        toExplore.put((child.cost, child))
                        exploreState.append(child.state)

    def childNodeAstar(self, action, cost, problem, d):
        return Node(self, action, cost + 1, problem.apply(action, State(self.state)), d)


search = Searches()

p = Problem()
s = State()

p.initialState = State(s)
print(s.position, " ", s.goalpos)
print(s.board)

print('=== Running BFS ===')
res = search.BFS(p)
print(res)
print("Explored Nodes: " + str(Node.nodeCount) + "\n")
Node.nodeCount = 0

print('=== Running DFS ===')
res = search.DFS(p)
print(res)
print("Explored Nodes: " + str(Node.nodeCount) + "\n")
Node.nodeCount = 0

print('=== Running Dijkstra ===')
res = search.dijkstra(p)
print(res)
print("Explored Nodes: " + str(Node.nodeCount) + "\n")
Node.nodeCount = 0

print('=== Running A* ===')
res = search.A_star(p)
print(res)
print("Explored Nodes: " + str(Node.nodeCount) + "\n")
Node.nodeCount = 0
