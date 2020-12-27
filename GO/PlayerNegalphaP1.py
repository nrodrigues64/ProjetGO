# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
myPlayer class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import time
import Goban 
from random import shuffle
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
        #areas = self._board._count_areas()
        if(self._mycolor == Goban.Board._BLACK):
            return -1*(black_stones - white_stones)  #+ areas[0]
        else:
            return -1*(white_stones - black_stones)    #+ areas[1]
    

    def negalpha_best_result(self,max_depth, alpha, beta):
        move = []
        if self._board.is_game_over():
            if self._board.result() == "1-0":
                if self._mycolor == Goban.Board._WHITE:
                    return -800, [None]
                else:
                    return 800, [None]
            elif self._board.result() == "0-1":
                if self._mycolor == Goban.Board._BLACK:
                    return -800, [None]
                else:
                    return 800,[None]
            elif self._board.result() == "1/2-1/2":
                return -800, [None]

        if max_depth == 0:
            return  self.capture_diff(), move
        
        moves = self._board.generate_legal_moves()
        shuffle(moves)
        for candidate_move in moves:
            self._board.push(candidate_move)
            val , opponent_move = self.negalpha_best_result(max_depth-1, -1*beta, -1*alpha)
            val *= -1
            self._board.pop()
            if val == alpha:
                move.append(candidate_move)
            if val > alpha:
                alpha = val
                move = [candidate_move]
                if alpha>=beta:
                    return alpha,move
        return alpha,move
        

    def get_liberty(self, moves):
        new_moves = []
        liberty = 0
        for move in moves:
            self._board.push(move)
            new_liberty = 0
            for i in range(81):
                if self._board[i]==self._mycolor:
                    j = self._board._neighborsEntries[i]
                    while(self._board._neighbors[j] != -1):
                        new_liberty += 1
                        j+=1
                    if liberty == new_liberty:
                        new_moves.append(move)
                    if new_liberty > liberty:
                        liberty = new_liberty
                        new_moves = [move]
            self._board.pop()
        print("LIBERTY = ", liberty)
        return new_moves

    def getPlayerMove(self):
        
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS"
        
        moves = self.negalpha_best_result(1, -800, +800)
        new_moves = self.get_liberty(moves[1])
        if len(new_moves) == 0 :
            new_moves.append(-1)
        move = choice(new_moves) 
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



