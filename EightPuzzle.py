##Avantika Poddar

import AI_problem
class Eight_Puzzle_Problem(AI_problem.abstract_SearchProblem):
    # grid is 9-array of the 3x3 8-puzzle grid in row-major order
    # 0 represents empty block
    def __init__(self, grid):
        self.grid = list(grid)
        for i in range(len(grid)):
            if self.grid[i] == 0:
                self.pos0 = i
                break        

    # We'll define state to be tuple([grid], pos0, [path])
    def getStartState(self):
        return (self.grid, self.pos0, [])

    # Goal state is [1,2,3,4,5,6,7,8,0]
    def isGoalState(self, state):
        grid, pos0, _ = state
        for i in range(8):
            if grid[i] != i+1:
                return False
        return pos0 == 8

    def getSuccessors(self, state):
        moves = []
        grid, pos0, path = state            

        def generateMove(incr, action):
            
            gridCopy = list(grid)
            gridCopy[pos0], gridCopy[pos0 + incr] = gridCopy[pos0 + incr], gridCopy[pos0]
            pathCopy = list(path)
            pathCopy.append(gridCopy)
            moves.append((gridCopy, pos0 + incr, pathCopy))

        if pos0 >= 3: # Slide empty block UP
            generateMove(-3, 'U')
            
        if pos0 <= 5: # Slide empty block DOWN
            generateMove(3, 'D')
        if (pos0 % 3) > 0: # Slide empty block LEFT
            generateMove(-1, 'L')
        if (pos0 % 3) < 2: # Slide empty block RIGHT
            generateMove(1, 'R')
        return moves
