from games4e import *
import math

GameState = namedtuple('GameState', 'to_move, table, cards0, cards1, tricks0, tricks1, gamesize, trump')

class SaathAath(Game):
    def __init__(self, cards0, cards1, gamesize = 5, trump = "S"):
        self.initial = GameState(to_move=0,table=None, cards0=cards0, cards1=cards1, tricks0=0, tricks1=0, gamesize = gamesize, trump=trump)

    def suit(self, card):
        return card[1]

    def rank(self, card):
        return card[0]
    
    def randdeal(size):
        cards = []

        match size:
            case 1:
                cards = [(13, "S"), (14, "S"),
                         (14, "C"),
                         (13, "H"), (14, "H"),
                         (14, "D")]

            case 3:
                cards = [(10, "S"), (11, "S"), (12, "S"), (13, "S"), (14, "S"),
                         (11, "C"), (12, "C"), (13, "C"), (14, "C"),
                         (10, "H"), (11, "H"), (12, "H"), (13, "H"), (14, "H"),
                         (11, "D"), (12, "D"), (13, "D"), (14, "D")]

            case 4:
                cards = [(9, "S"), (10, "S"), (11, "S"), (12, "S"), (13, "S"), (14, "S"),
                         (9, "C"), (10, "C"), (11, "C"), (12, "C"), (13, "C"), (14, "C"),
                         (9, "H"), (10, "H"), (11, "H"), (12, "H"), (13, "H"), (14, "H"),
                         (9, "D"), (10, "D"), (11, "D"), (12, "D"), (13, "D"), (14, "D")]
            case 5:
                cards = [(7, "S"), (8, "S"), (9, "S"), (10, "S"), (11, "S"), (12, "S"), (13, "S"), (14, "S"),
                         (8, "C"), (9, "C"), (10, "C"), (11, "C"), (12, "C"), (13, "C"), (14, "C"),
                         (7, "H"), (8, "H"), (9, "H"), (10, "H"), (11, "H"), (12, "H"), (13, "H"), (14, "H"),
                         (8, "D"), (9, "D"), (10, "D"), (11, "D"), (12, "D"), (13, "D"), (14, "D")]
    
        cards0 = {'hand':[],
                  'faceup':[],
                  'facedown':[]}
        
        cards1 = {'hand':[],
                  'faceup':[],
                  'facedown':[]}
        
        for i in range(size):
            choice = random.choice(cards)
            cards0['hand'].append(choice)
            cards.remove(choice)

            choice = random.choice(cards)
            cards0['faceup'].append(choice)
            cards.remove(choice)

            choice = random.choice(cards)
            cards0['facedown'].append(choice)
            cards.remove(choice)

            choice = random.choice(cards)
            cards1['hand'].append(choice)
            cards.remove(choice)

            choice = random.choice(cards)
            cards1['faceup'].append(choice)
            cards.remove(choice)

            choice = random.choice(cards)
            cards1['facedown'].append(choice)
            cards.remove(choice)

        return (cards0, cards1)
    
    def choose_trump(hand):
        s = 0
        c = 0
        d = 0
        h = 0
        for i in range(len(hand)):
            match hand[i][1]: 
                case "S":
                    s += hand[i][0]
                case "C":
                    c += hand[i][0]
                case "D":
                    d += hand[i][0]
                case "H":
                    h += hand[i][0]
        
        if(s >= c and s >= d and s >= h):
            return "S"

        elif(c >= s and c >= d and c >= h):
            return "C"
        
        elif(d >= s and d >= c and d >= h):
            return "D"

        else:
            return "H"

    def actions(self, state):
        ret = []

        # player 0's turn
        if (state.to_move == 0):
            #we are getting actions for a response play, must attempt to match suit
            if state.table is not None:
                suit = self.suit(state.table)
                foundsuit = False

                # check hand and faceup cards for the table suit
                for i in range(len(state.cards0['hand'])):
                    if(state.cards0['hand'][i] and self.suit(state.cards0['hand'][i]) == suit):
                        foundsuit = True
                for i in range(len(state.cards0['faceup'])):
                    if(state.cards0['faceup'][i] and self.suit(state.cards0['faceup'][i]) == suit):
                        foundsuit = True
                
                #player has >=1 card whose suit matches the played card's suit, must play one of those cards
                if(foundsuit):
                    for i in range(len(state.cards0['hand'])):
                        if(state.cards0['hand'][i] and self.suit(state.cards0['hand'][i]) == suit):
                            ret.append(state.cards0['hand'][i])
                    for i in range(len(state.cards0['faceup'])):
                        if(state.cards0['faceup'][i] and self.suit(state.cards0['faceup'][i]) == suit):
                            ret.append(state.cards0['faceup'][i])
            
                #no card that matches played card's suit, can play any card
                else:
                    for i in range(len(state.cards0['hand'])):
                        if(state.cards0['hand'][i]):
                            ret.append(state.cards0['hand'][i])
                    for i in range(len(state.cards0['faceup'])):
                        if(state.cards0['faceup'][i]):
                            ret.append(state.cards0['faceup'][i])
        
            #we are getting actions for a leading play, can play any card
            else:
                for i in range(len(state.cards0['hand'])):
                    if(state.cards0['hand'][i]):
                        ret.append(state.cards0['hand'][i])
                for i in range(len(state.cards0['faceup'])):
                    if(state.cards0['faceup'][i]):
                        ret.append(state.cards0['faceup'][i])
        else:
            # getting actions for a following play, must match the table suit
            if state.table is not None:
                suit = self.suit(state.table)
                foundsuit = False
                for i in range(len(state.cards1['hand'])):
                    if(state.cards1['hand'][i] and self.suit(state.cards1['hand'][i]) == suit):
                        foundsuit = True
                for i in range(len(state.cards1['faceup'])):
                    if(state.cards1['faceup'][i] and self.suit(state.cards1['faceup'][i]) == suit):
                        foundsuit = True
                
                #player has >=1 card whose suit matches the played card's suit, must play one of those cards
                if(foundsuit):
                    for i in range(len(state.cards1['hand'])):
                        if(state.cards1['hand'][i] and self.suit(state.cards1['hand'][i]) == suit):
                            ret.append(state.cards1['hand'][i])
                    for i in range(len(state.cards1['faceup'])):
                        if(state.cards1['faceup'][i] and self.suit(state.cards1['faceup'][i]) == suit):
                            ret.append(state.cards1['faceup'][i])
            
                #no card that matches played card's suit, can play any card
                else:
                    for i in range(len(state.cards1['hand'])):
                        if(state.cards1['hand'][i]):
                            ret.append(state.cards1['hand'][i])
                    for i in range(len(state.cards1['faceup'])):
                        if(state.cards1['faceup'][i]):
                            ret.append(state.cards1['faceup'][i])
        
            #we are getting actions for a leading play, can play any card
            else:
                for i in range(len(state.cards1['hand'])):
                    if(state.cards1['hand'][i]):
                        ret.append(state.cards1['hand'][i])
                for i in range(len(state.cards1['faceup'])):
                    if(state.cards1['faceup'][i]):
                        ret.append(state.cards1['faceup'][i])

        return ret

    def result(self, state, move):
        #remove card from player's hand
        new_cards0 = copy.deepcopy(state.cards0)
        new_cards1 = copy.deepcopy(state.cards1)
        if state.to_move == 0:
            for i in range(len(state.cards0['hand'])):
                if state.cards0['hand'][i] and state.cards0['hand'][i] == move:
                    new_cards0['hand'][i] = None
            for i in range(len(state.cards0['faceup'])):
                if state.cards0['faceup'][i] and state.cards0['faceup'][i] == move:
                    new_cards0['faceup'][i] = state.cards0['facedown'][i]
                    new_cards0['facedown'][i] = None
        
        else:
            for i in range(len(state.cards1['hand'])):
                if state.cards1['hand'][i] and state.cards1['hand'][i] == move:
                    new_cards1['hand'][i] = None
            for i in range(len(state.cards0['faceup'])):
                if state.cards1['faceup'][i] and state.cards1['faceup'][i] == move:
                    new_cards1['faceup'][i] = state.cards1['facedown'][i]
                    new_cards1['facedown'][i] = None

        #responding, need to determine winner
        if state.table is not None:
            winner = -1
            #played the same suit as the lead 
            if self.suit(move) == self.suit(state.table):
                #to_move won
                if self.rank(move) > self.rank(state.table):
                    winner = state.to_move
                    new_tricks0 = state.tricks0 + 1 if state.to_move == 0 else state.tricks0
                    new_tricks1 = state.tricks1 + 1 if state.to_move == 1 else state.tricks1
                #to_move lost
                else:
                    winner = 1 if state.to_move == 0 else 0
                    new_tricks0 = state.tricks0 + 1 if state.to_move == 1 else state.tricks0
                    new_tricks1 = state.tricks1 + 1 if state.to_move == 0 else state.tricks1
            
            #table suit is trump suit
            elif self.suit(state.table) == state.trump:
                #to_move lost
                winner = 1 if state.to_move == 0 else 0
                new_tricks0 = state.tricks0 + 1 if state.to_move == 1 else state.tricks0
                new_tricks1 = state.tricks1 + 1 if state.to_move == 0 else state.tricks1
            
            #to_move played trump
            elif self.suit(move) == state.trump:
                #to_move won
                winner = state.to_move
                new_tricks0 = state.tricks0 + 1 if state.to_move == 0 else state.tricks0
                new_tricks1 = state.tricks1 + 1 if state.to_move == 1 else state.tricks1

            #to_move played off suit
            else:
                #to_move lost
                winner = 1 if state.to_move == 0 else 0
                new_tricks0 = state.tricks0 + 1 if state.to_move == 1 else state.tricks0
                new_tricks1 = state.tricks1 + 1 if state.to_move == 0 else state.tricks1

            ret = GameState(to_move = winner,
                            table = None,
                            cards0 = new_cards0,
                            cards1 = new_cards1,
                            tricks0 = new_tricks0,
                            tricks1 = new_tricks1,
                            gamesize = state.gamesize,
                            trump=state.trump)

        #leading
        else:
            new_table = move
            new_tomove = 1 if state.to_move == 0 else 0

            ret = GameState(to_move = new_tomove,
                            table = new_table,
                            cards0 = new_cards0,
                            cards1 = new_cards1,
                            tricks0 = state.tricks0,
                            tricks1 = state.tricks1,
                            gamesize = state.gamesize,
                            trump=state.trump)
        
        return ret

    def utility(self, state, player):
        if player == 0:
            return state.tricks0 - math.ceil((3 * state.gamesize) / 2)
        else:
            return state.tricks1 - math.floor((3 * state.gamesize) / 2)

    def terminal_test(self, state):
        return not self.actions(state)

    def to_move(self, state):
        return state.to_move

    def display(self, state):
        display = "\n"

        display += "trump: " + str(state.trump) + "\n\n"
        display += "table: " + str(state.table) + "\n\n"
        display += "player 0:"
        if(state.to_move == 0):
            display += ("(TO MOVE)\n")
        else:
            display += "\n"
        display += "  hand:"
        for i in range(len(state.cards0['hand'])):
            display += " " + str(state.cards0['hand'][i])
        display += "\n"

        display += "  faceup:"
        for i in range(len(state.cards0['faceup'])):
            display += " " + str(state.cards0['faceup'][i])
        display += "\n"

        display += "  facedown:"
        for i in range(len(state.cards0['facedown'])):
            display += " " + str(state.cards0['facedown'][i])
        display += "\n"
        display += "  tricks won: " + str(state.tricks0) + "\n\n"

        display += "player 1:"
        if(state.to_move == 1):
            display += ("(TO MOVE)\n")
        else:
            display += "\n"
        display += "  hand:"
        for i in range(len(state.cards1['hand'])):
            display += " " + str(state.cards1['hand'][i])
        display += "\n"

        display += "  faceup:"
        for i in range(len(state.cards1['faceup'])):
            display += " " + str(state.cards1['faceup'][i])
        display += "\n"

        display += "  facedown:"
        for i in range(len(state.cards1['facedown'])):
            display += " " + str(state.cards1['facedown'][i])
        display += "\n"
        display += "  tricks won: " + str(state.tricks1) + "\n"

        print(display)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self, *players):
        """Play an n-person, move-alternating game."""
        state = self.initial
        while True:
            move = players[state.to_move](self, state)
            state = self.result(state, move)
            if self.terminal_test(state):
                self.display(state)
                return self.utility(state, self.to_move(self.initial))


mcts_wins_1 = 0
random_wins_1 = 0
ties_1 = 0

trump = ""
gamesize = int(input("Enter hand size: "))

cards0, cards1 = SaathAath.randdeal(gamesize)
trump = SaathAath.choose_trump(cards0['hand'])

print("random goes first")
for i in range(10):
    print("Game # " + str(i + 1))
    # cards0, cards1 = SaathAath.randdeal(gamesize)
    trump = SaathAath.choose_trump(cards0['hand'])
    saathaath = SaathAath(cards0, cards1, gamesize, trump)
    # saathaath.display(saathaath.initial)

    player0 = random_player
    player1 = mcts_player
    
    x = saathaath.play_game(player0, player1)
    print(x)
    if x > 0 :
            random_wins_1 += 1
    elif x ==  0:
            ties_1 += 1
    else:
            mcts_wins_1 += 1


print("now mcts goes first")
mcts_wins_2 = 0
random_wins_2 = 0
ties_2 = 0

for i in range(10):
    print("Game # " + str(i + 10))
    saathaath = SaathAath(cards0, cards1, gamesize, trump)
    saathaath.display(saathaath.initial)

    player0 = mcts_player
    player1 = random_player

    x = saathaath.play_game(player0, player1)
    print(x)
    if x > 0:
        mcts_wins_2 += 1
    elif x == 0:
        ties_2 += 1
    else:
        random_wins_2 += 1


print("mcts wins when going first: " + str(mcts_wins_2))
print("random wins when going first: " + str(random_wins_1))

print("mcts wins when going second: " + str(mcts_wins_1))
print("random wins when going second: " + str(random_wins_2))

