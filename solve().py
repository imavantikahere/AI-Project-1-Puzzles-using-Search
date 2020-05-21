##Avantika Poddar 
import AI_problem
import AI_program
import AI_search
import FarmerPuzzle
import StonePuzzle
import ManWoman
import EightPuzzle
import PACMAN
import Salesman


def solve(problem, list_search):

    #solve() takes as argument the instance of the problem to be solved and the list of search algorithms as obtained from the "AI_search.py" file
    

    
    puzzle_name= problem.__class__.__name__ #This built in function outputs the class name, which has been set as the name of the puzzle 
    print("Puzzle Name: ", puzzle_name)

    initial_state= problem.getStartState() #To print the initial state separately in the beginning
    solution = list_search[0](problem) #Applying the search algorithm DFS to the problem
    print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
    print ("DFS\t\t", solution[1],"\t\t", len(solution[0]),"\t", solution[2], "\nPath:" ,initial_state[0],"-->",solution[0])

    solution = list_search[1](problem)#Applying the search algorithm BFS to the problem
    print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
    print ("BFS\t\t", solution[1], "\t\t", len(solution[0]),"\t", solution[2], "\nPath:",initial_state[0],"-->", solution[0])

    solution = list_search[2](problem)#Applying the search algorithm UCS to the problem
    print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
    print ("UFS\t\t", solution[1], "\t\t" ,len(solution[0]), "\t",solution[2], "\nPath:", initial_state[0],"-->",solution[0])

    

    if(puzzle_name!="Eight_Puzzle_Problem"):
        solution = list_search[5](problem) #Applying the search algorithm IDDFS to the problem, not applicable for Eight puzzle as nodes generated would be too large, program would crash
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("IDDFS\t\t", solution[1],"\t\t ",len(solution[0]),"\t\t", solution[2],"\nPath:",initial_state[0],"-->",(solution[0]))
    
    
    

    #this portion checks which puzzle is being solved, so that the heuristic for that particular puzzle is run with A* algorithm
    
    if(puzzle_name=="Stone_Puzzle"):
        print("\nHeuristic used(s): HeuristicStone= Number of misplaced stones")

        solution = list_search[4](problem, lambda state: AI_program.heuristicStone(state[0]))#Applying the search algorithm greedy to the problem
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("Greedy\t\t", solution[1], "\t\t" ,len(solution[0]), "\t",solution[2], "\nPath:", initial_state[0],"-->",solution[0])
        
        solution = list_search[3](problem, lambda state: AI_program.heuristicStone(state[0]))
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("A* w/ Heuristic\t", solution[1], "\t\t" ,len(solution[0]),"\t",solution[2], "\nPath:",initial_state[0],"-->", solution[0])
    
    elif (puzzle_name=="Farmer_Sheep_Wolf_Lettuce_Puzzle"):
        print("\nHeuristic used(s): heuristicFWSL= Number of 1s in the state, or number of passengers on 1st side of river")

        
        solution = list_search[4](problem, lambda state: AI_program.heuristicFWSL(state[0]))#Applying the search algorithm greedy to the problem
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("Greedy\t\t", solution[1], "\t\t" ,len(solution[0]), "\t",solution[2], "\nPath:", initial_state[0],"-->",solution[0])
       
        solution = list_search[3](problem, lambda state: AI_program.heuristicFWSL(state[0]))
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("A* w/ Heuristic\t", solution[1], "\t\t" ,len(solution[0]),"\t",solution[2], "\nPath:",initial_state[0],"-->", solution[0])

    elif (puzzle_name=="Man_Woman_Children"):
        
        print("\nHeuristic used(s): heuristicMWC= Number of misplaced humans and boat")

        solution = list_search[4](problem, lambda state: AI_program.heuristicMWC(state[0]))#Applying the search algorithm greedy to the problem
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("Greedy\t\t", solution[1], "\t\t" ,len(solution[0]), "\t",solution[2], "\nPath:", initial_state[0],"-->",solution[0])
        
        solution = list_search[3](problem, lambda state: AI_program.heuristicMWC(state[0]))
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("\nA* w/ Heuristic\t", solution[1], "\t\t" ,len(solution[0]),"\t",solution[2], "\nPath:",initial_state[0],"-->", solution[0])

    elif (puzzle_name=="Eight_Puzzle_Problem"):

        print("\nHeuristic used(s): Manhattan Distance")

        solution = list_search[4](problem, lambda state: AI_program.manhattanDistance(state[0]))#Applying the search algorithm UCS to the problem
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("Greedy\t\t", solution[1], "\t\t" ,len(solution[0]), "\t",solution[2], "\nPath:", initial_state[0],"-->",solution[0])
        
        solution = list_search[3](problem, lambda state: AI_program.manhattanDistance(state[0]))
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("\nA* w/ Heuristic\t", solution[1], "\t\t" ,len(solution[0]),"\t",solution[2], "\nPath:",initial_state[0],"-->", solution[0])
        print("\nHeuristic used(s): Hamming Distance")

        
        solution = list_search[4](problem, lambda state: AI_program.hammingDistance(state[0]))#Applying the search algorithm UCS to the problem
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("Greedy\t\t", solution[1], "\t\t" ,len(solution[0]), "\t",solution[2], "\nPath:", initial_state[0],"-->",solution[0])
        solution = list_search[3](problem, lambda state: AI_program.hammingDistance(state[0]))
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("\nA* w/ Heuristic\t", solution[1], "\t\t" ,len(solution[0]),"\t",solution[2], "\nPath:",initial_state[0],"-->", solution[0])

    elif (puzzle_name=="Travelling_Salesman"):
    

        print("\nHeuristic used(s): Total distance covered per state")

        solution = list_search[4](problem, lambda state: AI_program.heuristicTSP((state[0],state[1])))#Applying the search algorithm UCS to the problem
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("Greedy\t\t", solution[1], "\t\t" ,len(solution[0]), "\t",solution[2], "\nPath:", initial_state[0],"-->",solution[0])
        solution = list_search[3](problem, lambda state: AI_program.heuristicTSP((state[0],state[1])))
        print ("\nAlgorithm", "Nodes generated", "Path Length", "Nodes expanded")
        print ("\nA* w/ Heuristic\t", solution[1], "\t\t" ,len(solution[0]),"\t",solution[2], "\nPath:",initial_state[0],"-->", solution[0])

if __name__ == '__main__':

    #creating instance of puzzle class
    #problem= Salesman.Travelling_Salesman(['A'],[[0,80,42,35],[80,0,30,34],[42,30,0,12],[35,34,12,0]])
    #problem= Salesman.Travelling_Salesman(['A'],[[0,20,42,35],[20,0,30,34],[42,30,0,12],[35,34,12,0]])
    problem= EightPuzzle.Eight_Puzzle_Problem([3,0,7,2,8,1,6,4,5])
    #problem= ManWoman.Man_Woman_Children([1,1,1,1,1])
    #problem= StonePuzzle.Stone_Puzzle(['O','O',' ', 'X','X'])
    #problem= StonePuzzle.Stone_Puzzle(['O','O', 'O',' ', 'X','X','X'])
    #problem= FarmerPuzzle.Farmer_Sheep_Wolf_Lettuce_Puzzle([1,1,1,1])
    #problem= PACMAN.Pacman_Problem(["%%%%%%","%    %", "% %% %", "%    %", "%%%% %","%    %", "%%%%%%"], (1,1), (5,1))
    #creating list of serch algorithms from "AI_search.py" file
    
    list_search= [AI_search.depthFirstSearch, AI_search.breadthFirstSearch, AI_search.uniformCostSearch, AI_search.astarSearch, AI_search.greedySearch, AI_search.iterativeDeepeningDFS]
    #Applying solve() for results
    solve(problem, list_search)


