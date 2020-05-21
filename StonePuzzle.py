##Avantika Poddar
import AI_problem
import AI_program
import AI_search
class Stone_Puzzle(AI_problem.abstract_SearchProblem):
    # grid is 2N+1-array of the stone puzzle pattern in row-major order, O is white pebble and X is black pebble
    def __init__(self,grid):
        self.grid = grid;
        
        self.pos0=int (len(self.grid)/2);
        

    #We'll define state to be tuple([grid], pos0, [path]) where grid is current state, pos is position of space and path is the solution space so far
    def getStartState(self):
        return (self.grid, self.pos0, [])
 
    # Goal state is [XXXX... .....OOOO]
    def isGoalState(self, state):
        grid, pos0, _= state
        
        if pos0!= int ((len(grid)-1)/2): return 0  #if space is not in the middle, then it is not the goal state
        for i in range(int((len(grid)-1)/2)):
                if (grid[i] != 'X'):
                    return 0
            
        return 1

    def getSuccessors(self, state):
        moves = []
        grid, pos0, path = state            

        def generateMove( pos,gridCopy):
            pathCopy = list(path)
            pathCopy.append(gridCopy)
            moves.append((gridCopy, pos,pathCopy))

           
        if pos0 > 0 and grid[pos0-1] == 'O': 
            #action= 'MoveToRight'
            gridCopy1 = list(grid)
            gridCopy1[pos0-1], gridCopy1[pos0]= gridCopy1[pos0],gridCopy1[pos0-1]
            pos= pos0-1
            generateMove(pos,gridCopy1)
            
        if (pos0>1 and grid[pos0-2] =='O' and grid[pos0-1]=='X'):
            #action= 'JumpToRight' if white stone is right before a black stone
            gridCopy2 = list(grid)
            gridCopy2[pos0],gridCopy2[pos0-2]= gridCopy2[pos0-2], gridCopy2[pos0]
            pos=pos0-2
            generateMove(pos, gridCopy2)
        if (pos0<len(grid)-1 and grid[pos0+1] == 'X'):
            #action ='MoveToLeft' if there is space infront of a black stone
            gridCopy3 = list(grid)
            gridCopy3[pos0+1], gridCopy3[pos0]= gridCopy3[pos0],gridCopy3[pos0+1]
            pos=pos0 +1
            generateMove(pos,gridCopy3)
        if (pos0<(len(grid)-2) and grid[pos0+2] =='X' and grid[pos0+1]=='O' ):
            #action ='JumpToLeft' if white stone is right after a black stone
            gridCopy4 = list(grid)
            gridCopy4[pos0],gridCopy4[pos0+2]= gridCopy4[pos0+2], gridCopy4[pos0]
            pos= pos0+2
            generateMove(pos, gridCopy4)

        
        return moves


