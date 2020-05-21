##Avantika Poddar 
import AI_problem
import AI_program
import AI_search
class Man_Woman_Children(AI_problem.abstract_SearchProblem):
    # grid is 5- array of the puzzle pattern in row-major order--> (Man, Woman, Child1, Child2, Boat) on first side of river: 1 corresponds to position in first side and 0 in second side
    #(1,1,1,1,1) is initial state as all passengers and boat are on first side
    #goal state is (0,0,0,0,0) as all passengers and boat are on second side 
    def __init__(self,grid):
        self.grid = grid;#[M W C1 C2,B} on first side of river -> Man, woman and children with boat all on one side means= [1,1,1,1,1]
        self.pos= 1 #positon of boat: the boat is on side 1 initially
        
    #We'll define state to be tuple([grid], position of boat, [path])
    def getStartState(self):
        return (self.grid,self.pos,[]) #[M, W, C1, C2 ,B] where B= boat on first side --> ([1,1,1,1,1],1,[])
 
    # Goal state is [0,0,0,0,0] with all passengers and boat on second side
    def isGoalState(self, state):

       arr= [0,0,0,0,0] #goal state array
       if  state[0] == arr: #checks with goal state array: returns true if it matches goal, 0 otherwise
           return 1
            
       return 0

    def getSuccessors(self, state): #returns sucessors of nodes popped in the memory stack
        
        moves = [] 
        grid, pos, path = state
        
        def generateMove( gridCopy, pos1):
            pathCopy = list(path)
            pathCopy.append(gridCopy)
            moves.append((gridCopy,pos1, pathCopy))


        if(pos==grid[0]):
             #action= 'Man goes to other side' if boat and man are on same side
            gridCopy1 = list(grid)
            gridCopy1= [int(not grid[0]),grid[1], grid[2], grid[3],int(not grid[4])]
            generateMove(gridCopy1,int(not pos))
           
        if pos== grid[1] :
            #action ='Woman goes to other side' if boat and woman are on same side
            gridCopy3 = list(grid)
            gridCopy3=[grid[0], int (not grid[1]),  grid[2], grid[3], int(not grid[4])]
            generateMove(gridCopy3, int(not pos))

        if pos==grid[2] :
            #action= 'Child 1 crosses alone' if the child and boat are on same side
            gridCopy2 = list(grid)
            gridCopy2= [ grid[0], grid[1],int(not grid[2]),  grid[3], int( not grid[4])]
            generateMove(gridCopy2, int(not pos))
        if pos== grid[3]:
            #action ='Child 2 crosses alone' if thr child and boat are on same side
            gridCopy4 = list(grid)
            gridCopy4= [grid[0],  grid[1], grid[2], int(not grid[3]), int(not grid[4])]
            generateMove(gridCopy4, int (not pos))
        if(pos==grid[2] and pos==grid[3]):
            #action= 'Both child 1 and 2 cross' if both children and boat are on same size
            gridCopy5 = list(grid)
            gridCopy5= [grid[0],  grid[1], int(not grid[2]), int(not grid[3]), int(not grid[4])]
            generateMove(gridCopy5, int (not pos))
        
        return moves



