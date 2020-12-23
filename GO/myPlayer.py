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
        diff = black_stones - white_stones
        if self._board._nextPlayer == Goban.Board._BLACK:
            return diff
        else:
            return -1 * diff
    
    def alpha_beta_best_result(self, max_depth, eval_fn):
        if max_depth == 0:
            return eval_fn(self)
        best_so_far = self.best_result
        for candidate_move in self._board.legal_moves():
            
            next_state = self._board.play_move(candidate_move)
            opponent_best_result = best_result(next_state, max_depth -1, eval_fn)
            our_result = -1 * opponent_best_result
            if our_result > best_so_far:
                best_so_far = our_result
            if self._board._nextPlayer == Goban.Board._WHITE:
                if best_so_far > best_white:
                    best_white = best_so_far
                outcome_for_black = -1 * best_so_far
                if outcome_for_black < best_black:
                    return best_so_far
            elif self._board._nextPlayer == Goban.Board._BLACK:
                if best_so_far > best_black:
                    best_black = best_so_far
                outcome_for_white = -1 * best_so_far
                if outcome_for_white < best_white:
                    return best_so_far

        return best_so_far

    


    def getPlayerMove(self):
        
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS"
        
        moves = self._board.legal_moves() # Dont use weak_legal_moves() here!
        move = alpha_beta_best_result(self, 2, capture_diff) 
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



