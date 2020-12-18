import math
import random


class Player:
    def __init__(self, letter):
        #letter can be x or o
        self.letter = letter
        
    #we want all players to get their next move in a given game
    def get_move(self, game):
        pass
    
class RandomComputerPlayer(Player): 
    def __init__(self, letter):
        #letter can be x or o
        super().__init__(letter)
        
    #we want all players to get their next move in a given game
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        #letter can be x or o
        super().__init__(letter)
        
    #we want all players to get their next move in a given game
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')    
            #we are going to check that this is a correctt value by trying cast
            # it to an integer and if its not then we say it is invalid
            #if that spot is not available on the board , we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if these are succesfull then yay!
            except ValueError:
                print('Invalid Square. Try again!!')
                
        return val