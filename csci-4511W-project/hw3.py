import sys
sys.path.append('aima-python')
from games import *
import math
from games4e import *

def c4_eval(state):
    '''Example of an odd function: 
    It likes states where an O has an X to the right of it. 
    Nothing else counts.
    '''
    ev = 0
    for col in range(1,6):
        for row in range(1,8):
            if state.board.get((row,col)) == 'O' and state.board.get((row, col+1)) == 'X':
                ev += 10
    return ev 


def count_X_runs(state):
    ev = 0
    cur_run = 0

    for col in range(1,7):
        cur_run = 0
        for row in range(7,0, -1):
            if state.board.get((row,col)) == 'X':
                cur_run += 1
            elif state.board.get((row,col)) == 'O':
                cur_run = 0
            else:
                if cur_run >= 4: return 10000
                if cur_run == 3: ev += 100
                if cur_run == 2: ev += 10
                if cur_run == 1: ev += 1
                cur_run = 0
    
    for row in range(1,8):
        cur_run = 0
        for col in range(1,7):
            if state.board.get((row,col)) == 'X':
                cur_run += 1
            if state.board.get((row,col)) == 'O':
                cur_run = 0
            if col == 6 or (state.board.get((row,col)) != 'X' and state.board.get((row,col)) != 'O'):
                if cur_run >= 4: return 10000
                if cur_run == 3: ev += 100
                if cur_run == 2: ev += 10
                if cur_run == 1: ev += 1
                cur_run = 0

        cur_run = 0
        for col in range(6, 0, -1):
            if state.board.get((row,col)) == 'X':
                cur_run += 1
            if state.board.get((row,col)) == 'O':
                cur_run = 0
            if col == 1 or (state.board.get((row,col)) != 'X' and state.board.get((row,col)) != 'O'):
                if cur_run >= 4: return 10000
                if cur_run == 3: ev += 100
                if cur_run == 2: ev += 10
                if cur_run == 1: ev += 1
                cur_run = 0

    return ev 

def count_O_runs(state):
    ev = 0
    cur_run = 0

    for col in range(1,7):
        cur_run = 0
        for row in range(7,0, -1):
            if state.board.get((row,col)) == 'O':
                cur_run += 1
            elif state.board.get((row,col)) == 'X':
                cur_run = 0
            else:
                if cur_run >= 4: return 10000
                if cur_run == 3: ev += 100
                if cur_run == 2: ev += 10
                if cur_run == 1: ev += 1
                cur_run = 0
    
    for row in range(1,8):
        cur_run = 0
        for col in range(1,7):
            if state.board.get((row,col)) == 'O':
                cur_run += 1
            if state.board.get((row,col)) == 'X':
                cur_run = 0
            if col == 6 or (state.board.get((row,col)) != 'X' and state.board.get((row,col)) != 'O'):
                if cur_run >= 4: return 10000
                if cur_run == 3: ev += 100
                if cur_run == 2: ev += 10
                if cur_run == 1: ev += 1
                cur_run = 0

        cur_run = 0
        for col in range(6, 0, -1):
            if state.board.get((row,col)) == 'O':
                cur_run += 1
            if state.board.get((row,col)) == 'X':
                cur_run = 0
            if col == 1 or (state.board.get((row,col)) != 'X' and state.board.get((row,col)) != 'O'):
                if cur_run >= 4: return 10000
                if cur_run == 3: ev += 100
                if cur_run == 2: ev += 10
                if cur_run == 1: ev += 1
                cur_run = 0

    return ev 

def c4_goodeval_X(state):
    return count_X_runs(state) - count_O_runs(state)

def c4_goodeval_O(state):
    return count_O_runs(state) - count_X_runs(state)

def connect4_eval(state):
    return c4_goodeval_X(state)
    # this is just for the autograder, I used the above functions for my actual evals.

def ab_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game, d=4, eval_fn=c4_eval)

def good_ab_cutoff_player_X(game, state):
    return alpha_beta_cutoff_search(state, game, d=4, eval_fn=c4_goodeval_X)

def good_ab_cutoff_player_O(game, state):
    return alpha_beta_cutoff_search(state, game, d=4, eval_fn=c4_goodeval_O)

class HW3:
    def __init__(self):
        pass

    def example_problem(self):
        tt = TicTacToe()
        tt.play_game(alpha_beta_player,query_player)

    def example_problem2(self):
        c4 = ConnectFour()
        c4.play_game(ab_cutoff_player, query_player)

    def problem_1d(self):
        c4 = ConnectFour()

        X_wins = 0
        O_wins = 0
        for i in range(0,5):
            if c4.play_game(good_ab_cutoff_player_X, random_player) == 1:
                X_wins += 1
            if c4.play_game(random_player, good_ab_cutoff_player_O) == -1:
                O_wins += 1

        print("X: " + str(X_wins) + "/5\nO: " + str(O_wins) + "/5")
        return (X_wins, O_wins)
    
    def play(self):
        c4 = ConnectFour()
        mcts_wins = 0
        ties = 0
        random_wins = 0

        for _ in range(15):
            x = c4.play_game(mcts_player, random_player)
            if x > 0:
                mcts_wins += 1
            elif x == 0:
                ties += 1
            else:
                random_wins += 1

        for _ in range(15):
            x = c4.play_game(random_player, mcts_player)
            if x > 0:
                random_wins += 1
            elif x == 0:
                ties += 1
            else:
                mcts_wins += 1

        print("mcts wins: " + str(mcts_wins))
        print("random wins: " + str(random_wins))
        print("ties: " + str(ties))
    
def main():
    hw3 = HW3()
    # # An example for you to follow to get you started on Games
    # print('Example Problem, playing Tic Tac Toe:')
    # print('=====================================')
    # # hw3.example_problem()

    # print('Example Problem, playing Connect 4 against my odd eval:')
    # print('=======================================================')
    # # uncomment to get it to run problem2
    # hw3.example_problem2()

    # print('Problem 3:')
    # hw3.problem_1d()

    hw3.play()



    
if __name__ == '__main__':
    main()
