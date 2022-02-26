import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)] # Use a single list to represnet 3x3 board

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 and so on (says what # corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # If valid move, then make move (square to letter)
        # then return true, if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if 3 in a row (diag, row, and colmun)
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        # check diag
        # only if square in an even # (0, 2, 4, 6, 8)
        # only possible moves to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #      ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game (the letter) or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # winner will be returned this breakign the loop
    while game.empty_squares():
        # recieve the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('') # empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player
                # if letter == 'X':
                #     letter = 'O'
                # else:
                #     letter = 'X'

        # mimic a human play + make things easier to read when game is printed
        if print_game:
            time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


# change the player setting below to HumanPlayer to play yourself

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    # Uncomment "for _ in range(runs):"  and "runs = 100" line below to run a simualtion, change the number to how ever many runs you want
    # make sure you change the players to a random and a smart player. 
    # also add "result = " before play of you are running a sim
    # and change the "print_game=True" to "print_game=False" so it does not print every single game
    # for _ in range(1000):
    # if you enable sim, indent the lines below form x_player to play(....)
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
    # Uncomment the section below from if to ties += 1
        # if result == 'X':
        #     x_wins +=1
        # elif result == 'O':
        #     o_wins += 1
        # else: 
        #     ties += 1

    # Uncomment this to view the results of the sim
    #print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties')
