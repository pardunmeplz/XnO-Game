import numpy as np
from enum import Enum

class Player(Enum):
    X = 1
    O = -1

class Message(Enum):
    ONGOING = 0
    WINNER_X = 1
    WINNER_O = 2
    DRAW = 3
    INVALID_INPUT = 4

class Move:
    def Move(self,player:Player,boxNum:int) -> None:
        self.player = player
        self.boxNum = boxNum

class Game:
    def Game(self, board = np.zeros(9))-> None:
        self.board:np.array = board
    
    def Reset(self) -> None:
        self.board = np.zeros(9)

    def play(self, move:Move) -> Message:
        pass
    pass



if __name__ == "__main__":
    newGame = Game()