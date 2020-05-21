#Heuristic functions
##Avantika Poddar 
def hammingDistance(grid): 
    return len([i for i in range(len(grid)) if grid[i] != 0 and grid[i] != i+1])

def manhattanDistance(grid):
    def distance(i):
        return 0 if grid[i] == 0 else abs(((grid[i]-1) / 3) - (i / 3)) + abs(((grid[i]-1) % 3) - (i % 3))
    return sum(distance(i) for i in range(len(grid)))


def heuristicFWSL(problem): #number of 1s in each state of Farmer problem
    count=0
    for i in problem:
        if i==1: count= count+1
    return count

def heuristicStone(grid): #number of misplaced stones in each state of stone puzzle
    count=0
    for i in range(len(grid)-1):
        if i<len(grid)/2:
            if (grid[i] != 'X') : count= count+1
        elif i>len(grid)/2:
            if(grid[i] != 'O'): count= count+1
    return count

def heuristicMWC(problem): #heuristic= no of misplaced humans and boat [1,1,1,1,1] being 5 and [0,0,0,0,0]= 0
    
    return sum(problem)

def heuristicTSP(problem): #Total distance covered of state

    distance=0
    arr= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    grid_, d_ = problem
    
    
    for i in range(len(grid_)-1):
        for j in range(len(arr)):
            if arr[j] == grid_[i]:
                ind= j
            if arr[j] == grid_[i+1]:
                ind_nxt= j

        distance= distance+ d_[ind][ind_nxt]


    for k in range(len(arr)):
        if arr[k]==grid_[len(grid_)-1]:
            break
    distance= distance + d_[k][0]


    return distance

    
    
    
    
