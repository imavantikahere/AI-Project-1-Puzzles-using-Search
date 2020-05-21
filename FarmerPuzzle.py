##Avantika Poddar 

import AI_problem

class Farmer_Sheep_Wolf_Lettuce_Puzzle(AI_problem.abstract_SearchProblem):
    # grid is 4- array of the puzzle pattern in row-major order--> [Farmer, Wolf, Sheep, Lettuce] on first side of river-->[1,1,1,1]
    def __init__(self,grid):
        self.grid = grid; #grid is the state of the system, initially [F, W, S, L] on first side of river
        
    #We'll define state to be tuple([grid], pos0, [path])
    def getStartState(self):
        return (self.grid,None,[]) #pos is None is here as it does not make sense to have a position attribute here and so it works well with the abstract method
 
    # Goal state is [0,0,0,0] which means everyone is on 2nd side of river
    def isGoalState(self, state):

       
       arr= [0,0,0,0] #goal state, array made for comparison
       if  state[0] == arr:
           return 1
            
       return 0

    def getSuccessors(self, state):
        moves = [] #list of child nodes
        grid, temp,path = state

#below line of code is to make sure the sheep does not eat the cabbage and the wolf does not eat the sheep

        if (((grid[0]!= grid[1]) and (grid[1]==grid[2])) or ((grid[0]!=grid[2]) and (grid[2]==grid[3]))):
            return []
        
        def generateMove( gridCopy):
            #this function appends the child node to the move list
            pathCopy = list(path)
            pathCopy.append(gridCopy)
            moves.append((gridCopy,None, pathCopy))

        
        
           #action= 'Farmer crosses alone'
        gridCopy1 = list(grid)
        gridCopy1= [int(not grid[0]),grid[1], grid[2], grid[3]]
        generateMove(gridCopy1)

            
    
        if grid[0]== grid[2] :
            #action ='Farmer crosses with sheep' if farmer and sheep are on same side
            gridCopy3 = list(grid)
            gridCopy3=[int(not grid[0]), grid[1], int(not grid[2]), grid[3]]
            generateMove(gridCopy3)

        if grid[0]==grid[1] :
            #action= 'Farmer crosses with wolf' if farmer and wolf are on same side
            gridCopy2 = list(grid)
            gridCopy2= [int(not grid[0]), int(not grid[1]), grid[2], grid[3]]
            generateMove(gridCopy2)
        if grid[0]== grid[3]:
            #action ='Farmer crosses with cabbage' if farmer and cabbage are on same side
            gridCopy4 = list(grid)
            gridCopy4= [int(not grid[0]),  grid[1], grid[2], int(not grid[3])]
            generateMove(gridCopy4)

        
        return moves


