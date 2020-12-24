# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
myPlayer class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban 
from random import choice
from playerInterface import *

class myPlayer(PlayerInterface):
    ''' Example of a random player for the go. The only tricky part is to be able to handle
    the internal representation of moves given by legal_moves() and used by push() and 
    to translate them to the GO-move strings "A1", ..., "J8", "PASS". Easy!

    '''

    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None

    def getPlayerName(self):
        return "Nicolas R - Dimitri D"

    def capture_diff(self):
        black_stones = self._board._nbBLACK
        white_stones = self._board._nbWHITE
        if(self._mycolor == Goban.Board._BLACK):
            return black_stones - white_stones
        else:
            return white_stones - black_stones
    
    def best_result(self, max_depth, eval_fn):
        """if max_depth == 0:
            return eval_fn()"""
        if(self._mycolor == Goban.Board._BLACK):
            best_so_far = -1 * self._board._nbWHITE
        else:
            best_so_far = -1 * self._board._nbBLACK
        move = -1
        for candidate_move in self._board.legal_moves():
            self._board.push(candidate_move)
            #opponent_best_result = self.best_result(max_depth -1, eval_fn)
            our_result = eval_fn()
            print("noir:",self._board._nbBLACK)
            print("blanc:",self._board._nbWHITE)
            print("our_result:",our_result)
            print("best_so_far:",best_so_far)
            print("move:",move)
            if our_result > best_so_far:
                print("tot")
                print("candidate_move", candidate_move)
                best_so_far = our_result
                move = candidate_move
                print("move_final:",move)
            self._board.pop()
        return move

    


    def getPlayerMove(self):
        
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS"
        
        moves = self._board.legal_moves() # Dont use weak_legal_moves() here!
        #move = choice(moves) 
        move = self.best_result(2, self.capture_diff)
        print("MY MOOVE ", move)
        self._board.push(move)
        # New here: allows to consider internal representations of moves
        print("I am playing ", self._board.move_to_str(move))
        print("My current board :")
        self._board.prettyPrint()
        # move is an internal representation. To communicate with the interface I need to change if to a string
        return Goban.Board.flat_to_name(move) 

    def playOpponentMove(self, move):
        print("Opponent played ", move) # New here
        # the board needs an internal represetation to push the move.  Not a string
        self._board.push(Goban.Board.name_to_flat(move)) 

    def newGame(self, color):
        self._mycolor = color
        self._opponent = Goban.Board.flip(color)

    def endGame(self, winner):
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")



