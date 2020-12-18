import math
import time     
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()  # we will use a single list to represent the 3x3 board
        self.current_winner = None  # keep track of winner!
    
    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2   etc tells us what number represent which cell of the matrix
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        # if valid move, then make move return true, else return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False   
    
    def winner(self, square, letter):
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # checking column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # checking the diagonal
        # but only if the square is an even number
        # these are the only possible moves for diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
    
    def available_moves(self):
        # other way
        return [i for i, spot in enumerate(self.board) if spot== ' ']

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')


def play(game, x_player, o_player, print_game=True):
    # if we have a winner then we return it or if tie then none
    if print_game:
        game.print_board_nums()
    
    letter = 'X' 
    # iterate game till we have no empty squares
    # we dont have to worry about the winner just yet so well just return when the loop breaks
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        # function for make move!
        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                
            letter = 'O' if letter == 'X' else x_player 
        # tiny break
        time.sleep(1)
    if print_game:
        print('It\'s a tie')
            

if __name__ == '__main__':
    x_player = RandomComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)    
        
        