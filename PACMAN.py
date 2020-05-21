
##Avantika Poddar 

import AI_problem

class Pacman_Problem(AI_problem.abstract_SearchProblem):
  # grid is a 2D array
  # pacman & food are tuples (r,c)
  def __init__(self, grid, pacman, food):
    self.grid = grid
    self.rows = len(grid)
    self.columns = len(grid[0])
    self.pacman = pacman
    self.food = food
      
  # Since this problem requires us to output the path taken
  # to reach the food pellet, we'll store the path in the state
  # state has this form:
  # tuple(tuple(r,c), [tuple(r1,c1), tuple(r2,c2), ...])
  # where the first tuple is the current position of pacman
  # and the list stores the path taken to reach here
  def getStartState(self):
    return (self.pacman, None, [self.pacman])

  def isGoalState(self, state):
    return state[0] == self.food

  def getSuccessors(self, state):        
    moves = []
    path = state[2]
    
    def getMove(r, c):
      if self.grid[r][c] != '%':
        newPath = list(path)
        move = (r, c)
        newPath.append(move)
        moves.append((move, None, newPath))
    
    if state[0][0] > 0:    # Go UP
      getMove(state[0][0]-1, state[0][1])
    if state[0][1] > 0:    # Go LEFT
      getMove(state[0][0], state[0][1]-1)
    if state[0][1] < self.columns - 1: # Go RIGHT
      getMove(state[0][0], state[0][1]+1)
    if state[0][0] < self.rows -1: # Go DOWN
      getMove(state[0][0]+1, state[0][1])
    return moves


