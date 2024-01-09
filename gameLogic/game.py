from enum import Enum
from functools import lru_cache

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
        self.winRows = []

    def Reset(self) -> None:
        self.board = [0]*9
        self.player = Player.X
        self.gameOver = False
    
    def printBoard(self):
        draw = {Player.X : 'X',Player.O :'O', 0 : '.'}
        for i,box in enumerate(self.board):
            print(draw[box], end = ' ')
            if i % 3 == 2: print()

    def Play(self, index: int) -> dict:
        if index < 0 or index > 8 or self.board[index] != 0 or self.gameOver:
            return {"message":Response.INVALID_INPUT}

        self.board[index] = self.player
        self.winRows = self._winCheck()
        if self.winRows != []:
            self.gameOver = True
            return Response.WINNER_X if self.player == Player.X else Response.Winner_O
        
        if self._tieCheck():
            self.gameOver = True
            return Response.DRAW

        self.player = Player.X if self.player == Player.O else Player.O    
        return Response.ONGOING
    
    def autoPlay(self)-> None:
        _, move = self._algo(tuple(self.board),self.player)
        return self.Play(move)

    def state(self) -> dict:
        return {"board":self.board, "player":self.player, "gameOver":self.gameOver, "winningLine":self.winRows}

    def _winCheck(self, board = None, player = None) -> list[set]:
        if not player: player = self.player 
        if not board : board = self.board
        wins =[{0,3,6},{1,4,7},{2,5,8},{0,1,2},{3,4,5},{6,7,8},{0,4,8},{2,4,6}]
        taken = {i for i,x in enumerate(board) if x == player}
        return [win for win in wins if win.issubset(taken)]

    def _tieCheck(self) -> bool:
        return 0 not in self.board
    
    @lru_cache
    def _algo(self,board: tuple,player:Player):
        
        #Check for Draw
        pendingList = [i for i,x in enumerate(board) if x == 0]
        if pendingList == []: return 0, None

        # Traverse state space tree to next move
        nextBoard = [*board]
        result = -2
        move = None
        for pending in pendingList:
            
            # Check for win
            nextBoard[pending] = player
            if self._winCheck(player=player,board=nextBoard) != []:return 1, pending
            
            nextResult, _ = self._algo(tuple(nextBoard),Player.X if player == Player.O else Player.O)
            
            # win for oponent is loss for us
            nextResult = -nextResult/2
            nextBoard[pending] = 0

            if result < nextResult:
                result = nextResult
                move = pending

        # return the most advantageous answer
        return result, move

if __name__ == "__main__":
    game = Game()
    while not game.gameOver:
        game.autoPlay()
        game.printBoard()
        print()