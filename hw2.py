import sys
sys.path.append('aima-python')
from search import *
import math
import time

def mhd(node):
    '''Define your manhattan-distance heuristic for the 8-puzzle here
    '''
    state = node.state

    sum = 0

    for i in range(len(state)):
        if(state[i] != 0):
            curRow = i // 3
            curCol = i % 3
            goalRow = (state[i] - 1) // 3
            goalCol = (state[i] - 1) % 3

            rowDelta = abs(curRow - goalRow)
            colDelta = abs(curCol - goalCol)

            sum += rowDelta + colDelta

    return sum

class HW2:

    def __init__(self):
        pass

    def example_problem(self):
        #EightPuzzle example with A*
        # Default goal is (1, 2, 3, 4, 5, 6, 7, 8, 0)
        #   which represents:   1 2 3
        #                       4 5 6
        #                       7 8 _
        #

        # In this example, we'll construct a puzzle with initial state
        #               1 2 3
        #               4 5 6
        #               _ 7 8
        #
        init = (1, 2, 3, 4, 5, 6, 0, 7, 8)
        puzzle = EightPuzzle(init)

        # Checks whether the initialized configuration is solvable or not
        # this is not a required step, but my be useful in saving you from
        # impossible configurations
        print("Is the puzzle solvable from this initial state?")
        print(puzzle.check_solvability(init))

        print("A* with default heuristic")
        return astar_search(puzzle).solution()

    def problem_1a(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem
            as described in the writeup
        2. return the solution from the A* search algorithm
        '''

        init = (0, 3, 6, 2, 5, 8, 1, 4, 7) 
        puzzle = EightPuzzle(init)


        return iterative_deepening_search(puzzle).solution()
    
    def problem_1b(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem
            as described in the writeup
        2. return the solution from the A* search algorithm
        '''

        init = (0, 3, 6, 2, 5, 8, 1, 4, 7) 
        puzzle = EightPuzzle(init)

        return astar_search(puzzle).solution()

    def problem_1c(self):
        '''
        1. instantiate the search algorithm with the 8 puzzle problem
            as described in the writeup
        2. return the solution from the A* search algorithm
        '''

        init = (6, 0, 2, 5, 1, 3, 4, 8, 7)
        puzzle = EightPuzzle(init)

        return astar_search(puzzle).solution()

    def problem_1d(self):
        '''
        Complete the mhd function (defined above class HW2)

        1. instantiate the search algorithm with the 8 puzzle problem 
        2. write code that will create a different heuristic
        3. return the solution from the A* search algorithm
        '''

        init = (6, 0, 2, 5, 1, 3, 4, 8, 7)
        puzzle = EightPuzzle(init)

        return astar_search(puzzle, mhd).solution()

    def problem_2(self):
        '''
        1. find initial states with optimal solutions of lengths 15, 17, 19 and 21
        2. for each of those, for each heuristic, measure the time it takes to find a solution
        Note: It is not required that your code for this be done specifically in this 
        function. It can be elsewhere in the file if you want to structure the code differently
        The autograder will not test this code, but we will look at it by hand, so if it
        is not all in this function, leave a comment letting us know where to look.
        '''

        puzzle15_init = (3, 6, 8, 2, 5, 0, 1, 4, 7)
        puzzle17_init = (3, 6, 8, 2, 5, 7, 1, 0, 4)
        puzzle19_init = (3, 6, 8, 0, 5, 7, 2, 1, 4)
        puzzle21_init = (6, 0, 8, 3, 5, 7, 2, 1, 4)

        puzzle15 = EightPuzzle(puzzle15_init)
        puzzle17 = EightPuzzle(puzzle17_init)
        puzzle19 = EightPuzzle(puzzle19_init)
        puzzle21 = EightPuzzle(puzzle21_init)

        start = time.time()
        default_15 = astar_search(puzzle15).solution()
        default_15_time = time.time() - start

        start = time.time()
        default_17 = astar_search(puzzle17).solution()
        default_17_time = time.time() - start

        start = time.time()
        default_19 = astar_search(puzzle19).solution()
        default_19_time = time.time() - start

        start = time.time()
        default_21 = astar_search(puzzle21).solution()
        default_21_time = time.time() - start

        start = time.time()
        mhd_15 = astar_search(puzzle15, mhd).solution()
        mhd_15_time = time.time() - start

        start = time.time()
        mhd_17 = astar_search(puzzle17, mhd).solution()
        mhd_17_time = time.time() - start

        start = time.time()
        mhd_19 = astar_search(puzzle19, mhd).solution()
        mhd_19_time = time.time() - start

        start = time.time()
        mhd_21 = astar_search(puzzle21, mhd).solution()
        mhd_21_time = time.time() - start
        
        if(len(default_15) != 15 | len(default_17) != 17 | 
           len(default_19) != 19 | len(default_21) != 21 |
           len(mhd_15) != 15 | len(mhd_17) != 17 | 
           len(mhd_19) != 19 | len(mhd_21) != 21):
            print()
            print("at least one solution was too long or too short")

        else:
            print()
            print("  all solutions were the required length :)")
            print("┌────────┬────────────────────┬────────────────────┐")
            print("│  Size  │    Default Time    │      MHD Time      │")
            print("├────────┼────────────────────┼────────────────────┤")
            print("│   15   │    {:.10f}    │    {:.10f}    │".format(default_15_time, mhd_15_time))
            print("│        │                    │                    │")
            print("│   17   │    {:.10f}    │    {:.10f}    │".format(default_17_time, mhd_17_time))
            print("│        │                    │                    │")
            print("│   19   │    {:.10f}    │    {:.10f}    │".format(default_19_time, mhd_19_time))
            print("│        │                    │                    │")
            print("│   21   │    {:.10f}    │    {:.10f}    │".format(default_21_time, mhd_21_time))
            print("└────────┴────────────────────┴────────────────────┘")
            print()

        return None

    def example_problem_3(self):
        '''Use the InstrumentedProblem class to track stats about a breadth-first
        search on the Romania Map problem.
        '''
        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        g = InstrumentedProblem(GraphProblem('Craiova', 'Zerind', romania_map))
        result = breadth_first_graph_search(g)
        print(g)
        g2 = InstrumentedProblem(GraphProblem('Craiova', 'Zerind', romania_map))
        result2 = iterative_deepening_search(g2)
        print(g2)
        return (g.goal_tests, g2.goal_tests)

    def problem_3a(self):
        '''Use the InstrumentedProblem class to track stats about 
        different searches on the Romania Map problem.
        '''

        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")

        graph1 = InstrumentedProblem(GraphProblem('Timisoara' , 'Pitesti', romania_map))
        graph2 = InstrumentedProblem(GraphProblem('Timisoara' , 'Pitesti', romania_map))
        graph3 = InstrumentedProblem(GraphProblem('Timisoara' , 'Pitesti', romania_map))
        graph4 = InstrumentedProblem(GraphProblem('Timisoara' , 'Pitesti', romania_map))

        g1 = breadth_first_graph_search(graph1)
        print(graph1)
        g2 = depth_first_graph_search(graph2)
        print(graph2)
        g3 = iterative_deepening_search(graph3)
        print(graph3)
        g4 = recursive_best_first_search(graph4)
        print(graph4)
        
        return (graph1, graph2, graph3, graph4)
    
    def problem_3b(self):
        '''Use the InstrumentedProblem class to track stats about
        different searches on the Romania Map problem.
        '''

        print("Su: Successor States created")
        print("Go: Number of Goal State checks")
        print("St: States created")
        print("   Su   Go   St")
        
        graph1 = InstrumentedProblem(GraphProblem('Timisoara' , 'Eforie', romania_map))
        graph2 = InstrumentedProblem(GraphProblem('Timisoara' , 'Eforie', romania_map))
        graph3 = InstrumentedProblem(GraphProblem('Timisoara' , 'Eforie', romania_map))
        graph4 = InstrumentedProblem(GraphProblem('Timisoara' , 'Eforie', romania_map))

        g1 = breadth_first_graph_search(graph1)
        print(graph1)
        g2 = depth_first_graph_search(graph2)
        print(graph2)
        g3 = iterative_deepening_search(graph3)
        print(graph3)
        g4 = recursive_best_first_search(graph4)
        print(graph4)
        
        return (graph1, graph2, graph3, graph4)


def main():
    
    # Create object, hw2, of datatype HW2.
    hw2 = HW2()
 
    # =======================
    # A* with 8-Puzzle 
    # An example for you to follow to get you started on the EightPuzzle
    print('Example Problem result:')
    print('=======================')
    print(hw2.example_problem())

    print()
    
    print('Problem 1a result:')
    print('==================')
    print(hw2.problem_1a())

    print()

    print('Problem 1b result:')
    print('==================')
    print(hw2.problem_1b())

    print()

    print('Problem 1c result:')
    print('==================')
    print(hw2.problem_1c())

    print()

    print('Problem 1d result:')
    print('==================')
    print(hw2.problem_1d())

    print()

    print('Problem 2 result:')
    print('=================')
    print(hw2.problem_2())

    print()

    print(hw2.example_problem_3())

    print()

    print('Problem 3a result:')
    print('==================')
    print(hw2.problem_3a())

    print()

    print('Problem 3b result:')
    print('==================')
    print(hw2.problem_3b())

    print()

    
if __name__ == '__main__':
    main()
