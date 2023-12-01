import numpy as np
import random


class State:
    boardSize = 10

    def __init__(self, s=None):
        if s is None:
            self.boardType = random.randint(0, 5)
            if self.boardType == 0:
                #                       0, 1, 2, 3, 4, 5, 6, 7, 8, 9          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
                self.board = np.array([[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0 | S  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],  # 1 | ~  =  ~  ~  ~  ~  ~  ~  =  =
                                       [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],  # 2 | ~  ~  =  ~  =  ~  =  ~  ~  ~
                                       [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],  # 3 | ~  ~  =  ~  ~  ~  ~  ~  =  ~
                                       [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # 4 | ~  ~  ~  ~  =  ~  =  ~  =  ~
                                       [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 5 | =  =  =  ~  ~  ~  ~  ~  ~  ~
                                       [3, 1, 1, 1, 1, 0, 1, 1, 0, 1],  # 6 | @  ~  ~  ~  ~  =  ~  ~  =  ~
                                       [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],  # 7 | =  =  =  ~  ~  =  ~  ~  ~  ~
                                       [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # 8 | ~  ~  =  ~  =  =  =  ~  =  =
                                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 9 | ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       ])
                self.goalpos = [6, 0]
            elif self.boardType == 1:
                #                       0, 1, 2, 3, 4, 5, 6, 7, 8, 9          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
                self.board = np.array([[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0 | S  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],  # 1 | ~  =  ~  ~  ~  ~  ~  ~  =  =
                                       [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],  # 2 | ~  ~  =  ~  =  ~  =  ~  ~  ~
                                       [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],  # 3 | ~  ~  =  ~  ~  ~  ~  ~  =  ~
                                       [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # 4 | ~  ~  ~  ~  =  ~  =  ~  =  ~
                                       [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 5 | =  =  =  ~  ~  ~  ~  ~  ~  ~
                                       [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],  # 6 | ~  ~  ~  ~  ~  =  ~  ~  =  ~
                                       [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],  # 7 | =  =  =  ~  ~  =  ~  ~  ~  ~
                                       [3, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # 8 | @  ~  =  ~  =  =  =  ~  =  =
                                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 9 | ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       ])
                self.goalpos = [8, 0]
            elif self.boardType == 2:
                #                       0, 1, 2, 3, 4, 5, 6, 7, 8, 9          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
                self.board = np.array([[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0 | S  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],  # 1 | ~  =  ~  ~  ~  ~  ~  ~  =  =
                                       [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],  # 2 | ~  ~  =  ~  =  ~  =  ~  ~  ~
                                       [1, 1, 0, 1, 1, 3, 1, 1, 0, 1],  # 3 | ~  ~  =  ~  ~  @  ~  ~  =  ~
                                       [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # 4 | ~  ~  ~  ~  =  ~  =  ~  =  ~
                                       [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 5 | =  =  =  ~  ~  ~  ~  ~  ~  ~
                                       [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],  # 6 | ~  ~  ~  ~  ~  =  ~  ~  =  ~
                                       [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],  # 7 | =  =  =  ~  ~  =  ~  ~  ~  ~
                                       [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # 8 | ~  ~  =  ~  =  =  =  ~  =  =
                                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 9 | ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       ])
                self.goalpos = [3, 5]
            elif self.boardType == 3:
                #                       0, 1, 2, 3, 4, 5, 6, 7, 8, 9          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
                self.board = np.array([[2, 1, 1, 1, 1, 1, 1, 1, 1, 3],  # 0 | S  ~  ~  ~  ~  ~  ~  ~  ~  @
                                       [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],  # 1 | ~  =  ~  ~  ~  ~  ~  ~  =  =
                                       [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],  # 2 | ~  ~  =  ~  =  ~  =  ~  ~  ~
                                       [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],  # 3 | ~  ~  =  ~  ~  ~  ~  ~  =  ~
                                       [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # 4 | ~  ~  ~  ~  =  ~  =  ~  =  ~
                                       [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 5 | =  =  =  ~  ~  ~  ~  ~  ~  ~
                                       [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],  # 6 | ~  ~  ~  ~  ~  =  ~  ~  =  ~
                                       [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],  # 7 | =  =  =  ~  ~  =  ~  ~  ~  ~
                                       [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # 8 | ~  ~  =  ~  =  =  =  ~  =  =
                                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 9 | ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       ])
                self.goalpos = [0, 9]
            elif self.boardType == 4:
                #                       0, 1, 2, 3, 4, 5, 6, 7, 8, 9          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
                self.board = np.array([[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0 | S  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],  # 1 | ~  =  ~  ~  ~  ~  ~  ~  =  =
                                       [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],  # 2 | ~  ~  =  ~  =  ~  =  ~  ~  ~
                                       [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],  # 3 | ~  ~  =  ~  ~  ~  ~  ~  =  ~
                                       [1, 1, 1, 1, 0, 1, 0, 1, 0, 3],  # 4 | ~  ~  ~  ~  =  ~  =  ~  =  @
                                       [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 5 | =  =  =  ~  ~  ~  ~  ~  ~  ~
                                       [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],  # 6 | ~  ~  ~  ~  ~  =  ~  ~  =  ~
                                       [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],  # 7 | =  =  =  ~  ~  =  ~  ~  ~  ~
                                       [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # 8 | ~  ~  =  ~  =  =  =  ~  =  =
                                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 9 | ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       ])
                self.goalpos = [4, 9]
            elif self.boardType == 5:
                #                       0, 1, 2, 3, 4, 5, 6, 7, 8, 9          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
                self.board = np.array([[2, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 0 | S  ~  ~  ~  ~  ~  ~  ~  ~  ~
                                       [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],  # 1 | ~  =  ~  ~  ~  ~  ~  ~  =  =
                                       [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],  # 2 | ~  ~  =  ~  =  ~  =  ~  ~  ~
                                       [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],  # 3 | ~  ~  =  ~  ~  ~  ~  ~  =  ~
                                       [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],  # 4 | ~  ~  ~  ~  =  ~  =  ~  =  ~
                                       [0, 0, 0, 1, 1, 1, 1, 1, 1, 1],  # 5 | =  =  =  ~  ~  ~  ~  ~  ~  ~
                                       [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],  # 6 | ~  ~  ~  ~  ~  =  ~  ~  =  ~
                                       [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],  # 7 | =  =  =  ~  ~  =  ~  ~  ~  ~
                                       [1, 1, 0, 1, 0, 0, 0, 1, 0, 0],  # 8 | ~  ~  =  ~  =  =  =  ~  =  =
                                       [1, 1, 1, 1, 1, 1, 1, 1, 1, 3],  # 9 | ~  ~  ~  ~  ~  ~  ~  ~  ~  @
                                       ])
                self.goalpos = [9, 9]
            # position
            self.position = [0, 0]
        else:
            self.board = np.empty_like(s.board)
            self.board[:] = s.board

            self.position = list(s.position)
            self.goalpos = list(s.goalpos)

    # converts to readable string to print
    def __str__(self):
        rstr = ''
        for row in self.board:
            rstr += str(row) + '\n'
        return rstr

    # overload to allow comparison of lists and states with ==
    def __eq__(self, other):
        if isinstance(other, State):
            return np.array_equal(self.board, other.board)
        elif isinstance(other, list):
            return self.board == other
        else:
            return NotImplemented

    # turn into immutable object for set lookup
    def toTuple(self):
        tpl = ()
        for row in self.board:
            tpl += (tuple(row),)
        return tpl


class Node:
    """
    Attributes:
    - p: The parent node.
    - a: The action that led to this node from the parent.
    - c: The cost associated with reaching this node.
    - s: The state represented by this node.
    - d: The depth of this node in the search tree.
    """
    nodeCount = 0

    def __init__(self, p, a, c, s, d):
        # keep track of how many nodes were created
        self.__class__.nodeCount += 1
        self.nodeID = self.nodeCount

        self.parent = p
        self.cost = c
        self.action = a
        self.state = s
        self.depth = d

    def __lt__(self, other):
        # self < other
        return self.depth + calculate_h(self.state.position, self.state.goalpos) < other.depth + calculate_h(
            other.state.position, self.state.goalpos)

    def __str__(self):
        rstr = 'NodeID: ' + str(self.nodeID) + '\n'
        if self.parent is not None:
            rstr += 'Parent: ' + str(self.parent.nodeID) + '\n'
        if self.action is not None:
            rstr += 'Action: ' + self.action + '\n'
        rstr += 'Cost:   ' + str(self.cost) + '\n'
        rstr += 'State:\n' + str(self.state)
        return rstr


# creates and returns a new node which would be child of current node n being passed to the function
def childNode(n, action, problem, d):
    return Node(n, action, n.cost + 1, problem.apply(action, State(n.state)), d)


def calculate_h(position, goal):
    h = abs(goal[0] - position[0]) * abs(goal[1] - position[1])
    return h


class Problem:
    """
    Class that defines a search problem.

    Attributes:
    - actions (list): A list of possible actions in the problem.
    - initialState: The initial state of the problem.
    """

    def __init__(self):
        self.actions = ['U', 'L', 'D', 'R']
        self.initialState = 0

    def apply(self, a, s):

        # positions after move, still refers to s.position object
        post = s.position

        # make a copy
        pre = list(post)

        # compute post position
        if a == 'U':
            post[0] = max(pre[0] - 1, 0)
        elif a == 'L':
            post[1] = max(pre[1] - 1, 0)
        elif a == 'D':
            post[0] = min(pre[0] + 1, s.boardSize - 1)
        elif a == 'R':
            post[1] = min(pre[1] + 1, s.boardSize - 1)
        else:
            print('Undefined action: ' + str(a))
            raise StandardError('Action not defined for this problem!')

        # print(pre, ' ', post,' ',s.board[pre[0]][pre[1]] , '<--', s.board[post[0]][post[1]])
        s.board[pre[0]][pre[1]] = 1
        s.board[post[0]][post[1]] = 2

        return s

    def applicable(self, s):
        actionList = []

        # check if actions are applicable
        y = s.position[0]
        x = s.position[1]

        # Not in top row
        if s.position[0] > 0:
            # Not in wall
            if s.board[y - 1][x] != 0:
                actionList.append('U')

        # not in left most col
        if s.position[1] > 0:
            # Not in wall
            if s.board[y][x - 1] != 0:
                actionList.append('L')

        # not in bottom row
        if s.position[0] < (s.boardSize - 1):
            # Not in wall
            if s.board[y + 1][x] != 0:
                actionList.append('D')

        # not in right col
        if s.position[1] < (s.boardSize - 1):
            # Not in wall
            if s.board[y][x + 1]:
                actionList.append('R')

        return actionList

    # test if current state is goal state or not
    def goalTest(self, s):
        return s.goalpos == s.position


def solution(node):
    # Returns actionList, cost of the solution generated from the node

    actions = []
    cost = node.cost

    while node.parent is not None:
        actions.insert(0,node.action)
        node = node.parent

    return actions, cost
