# Data Structures
##Avantika Poddar – 
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def empty(self):
        return len(self.stack) == 0

from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()
    def push(self, item):
        self.queue.append(item)
    def pop(self):
        return self.queue.popleft()
    def empty(self):
        return len(self.queue) == 0

import heapq
class PriorityQueue:
    def __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        self.heap = []
    
    def push(self, item):
        heapq.heappush(self.heap, (self.priorityFunction(item), item))
    
    def pop(self):
        (_, item) = heapq.heappop(self.heap)
        return item
    
    def empty(self):
        return len(self.heap) == 0

# Search Algorithms

def graphSearch(problem, strategy):
    start = problem.getStartState()
    
    explored = set([str(start[0])])
    
    strategy.push(start)
    count=0
    
    while not strategy.empty():
        node = strategy.pop()
        count= count+1
        
        if problem.isGoalState(node):
            # return the solution path and no. of explored nodes
            return (node[2], len(explored),count)
        for move in problem.getSuccessors(node):
            gridCopy = str(move[0])
            if gridCopy not in explored:
                explored.add(gridCopy)
                strategy.push(move)

    return None

def depthFirstSearch(problem):
    return graphSearch(problem, Stack())

def breadthFirstSearch(problem):
    return graphSearch(problem, Queue())

def uniformCostSearch(problem):
    return graphSearch(problem, PriorityQueue(lambda state: len(state[2])))

def astarSearch(problem, heuristic):
    # A* uses path cost from start state + heuristic estimate to a goal
    totalCost = lambda state: len(state[2]) + heuristic(state)
    return graphSearch(problem, PriorityQueue(totalCost))

def greedySearch(problem, heuristic):
    return graphSearch(problem, PriorityQueue(heuristic))


c=0
def depthLimitedDFS(problem, state, depth):
  
  if problem.isGoalState(state):
    return state[2]
  if depth <= 0:
    return None

  for move in problem.getSuccessors(state):

    global c
    c=c+1
    solution = depthLimitedDFS(problem, move, depth-1)
    
    if solution is not None:
      return solution
  return None


def iterativeDeepeningDFS(problem):

  
  global c
  explored=0
  depth = 1
  while True:
    solution = depthLimitedDFS(problem, problem.getStartState(), depth)
    explored= explored + 1
    if solution is not None:
      return (solution,c,explored)
    depth += 1
