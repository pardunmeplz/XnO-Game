from enum import Enum

class Player(Enum):
    X = 1
    O = -1
    
class Response(Enum):
    ONGOING = 0
    WINNER_X = 1
    WINNER_O = 2
    DRAW = 3
    INVALID_INPUT = 4

class Move:
    def __init__(self,player: Player,boxNum:int) -> None:
        self.player = player
        self.boxNum = boxNum

class Game:
    def __init__(self, board = [0]*9)-> None:
        self.board:list[int] = board
        self.player = Player.X
    
    def Reset(self) -> None:
        self.board = [0]*9

    def Play(self, move:Move) -> Response:
        if self.board[move.boxNum] != 0:
            return Response.INVALID_INPUT

    def _winCheck(self)-> list[set]:
        wins =[{0,3,6},{1,4,7},{2,5,8},{0,1,2},{3,4,5},{6,7,8},{0,4,8},{2,4,6}]
        taken = {i for i,x in enumerate(self.board) if x == self.player}
        return [win for win in wins if win.issubset(taken)]

    def _tieCheck(self,board):
        return 0 not in board

if __name__ == "__main__":
    newGame = Game()
    newGame.Play(Move(Player.X,3))
    newGame.Reset()

