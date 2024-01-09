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

class Game:
    def __init__(self, board = [0]*9)-> None:
        self.board:list[int] = board
        self.player = Player.X
        self.gameOver = False
    
    def Reset(self) -> None:
        self.board = [0]*9
        self.player = Player.X
    
    def Play(self, index: int) -> Response:
        if index < 0 or index > 8 or self.board[index] != 0:
            return Response.INVALID_INPUT

        self.board[index] = self.player
        if self._winCheck():
            return Response.WINNER_X if self.player == Player.X else Response.Winner_O
        
        if self._tieCheck():
            return Response.DRAW

        self.Player = Player.X if self.Player == Player.O else Player.O    
        return Response.ONGOING

        
    def _winCheck(self) -> list[set]:
        wins =[{0,3,6},{1,4,7},{2,5,8},{0,1,2},{3,4,5},{6,7,8},{0,4,8},{2,4,6}]
        taken = {i for i,x in enumerate(self.board) if x == self.player}
        return [win for win in wins if win.issubset(taken)]

    def _tieCheck(self) -> bool:
        return 0 not in self.board