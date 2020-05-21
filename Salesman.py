##Avantika Poddar
##Shatha Abduh

import AI_problem
import math

arr= "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #This is done to appropriately convert numbers to characters; 0->A, 1->B, computation done using numbers, but output is of char dorm


class Travelling_Salesman(AI_problem.abstract_SearchProblem):
    #grid is the initial empty list[], basically the list of nodes visited so far
    #d is the distance list of the form [[0,n1,n1....],[n1,0,b3....].....] representing the current position and the distances of all nodes from that position
    
    def __init__(self, grid,d):
        self.grid = list(grid)
        self.d=d
        
    
    # We'll define state to be tuple([grid], d, [path])->([nodes visited so far],[distances], [path])
    
    def getStartState(self):
        return (self.grid,self.d,[])

    # Goal state is when the list consists of all nodes visited once
    def isGoalState(self, state):

        if(len(state[0])) == len(self.d) :
            return 1
        return 0

    #getSuccessors gets all the child nodes of each node popped from memory

    def getSuccessors(self, state):
        moves = [] #list of child nodes
        grid_, d, path = state            

        def generateMove(grid1): #this function appends the new grid and path (child) into move
            
            pathCopy = list(path)
            pathCopy.append(grid1)
            moves.append((grid1, d, pathCopy))

        for i in range(len(self.d)): #for all points available
            if arr[i] not in grid_: #checks if corresponding character is already visited
                grid1= list(grid_) #if not visited, then create copy of old state
                grid1.append(arr[i])#adds the new character to state
                generateMove(grid1) #passed to function to be moves to list of nodes (move[])

        
        return moves
