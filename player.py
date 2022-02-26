import math
import random


class Player():
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    #we want all players to get their next move
    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # it to an integer, and if it's not, then its invalid
            # Checking that this is a correct value by trying to cast
            # if that spot is not available on the board, say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # randomly chooses one
        else:
            # get the square based off the minimax algo
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player):
        max_player = self.letter # self
        other_player = 'O' if player == 'X' else 'X' # other player


    # check if previous move is a winner
    # base case
        if state.current_winner == other_player:
        # return position and score for minimax
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}

        elif not state.empty_squares(): # no empty squares
            return {'position': None, 'score': 0}
    
        if player == max_player: 
            best = {'position': None, 'score': -math.inf} # each score should maximize 
        else: 
            best = {'position': None, 'score': math.inf} # eachs core should minimize
    
        for possible_move in state.available_moves():
            # Step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # Step 2: Recurse ising minimac to simulate a game after making that move
            sim_score = self.minimax(state, other_player) # alternate players
        
            # Step 3: Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # important to not mess up with recursion
        
            # Step 4: Update the dictinaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best
                
        return best


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
