# -*- coding: utf-8 -*-
"""
    This file contains the main program of the game Wum Pus.
"""
import sys
import random
import wum_pus

while 1:
    start = wum_pus.main_menu()
    if start == True:
        pass
    else:
        wum_pus.rules()
        continue
    squares_list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
    random.shuffle(squares_list)
    board = {"wum":squares_list[0], "bat1":squares_list[1], "bat2":squares_list[2], "well1":squares_list[3], "well2":squares_list[4], "player":squares_list[5]}
    arrows = 3
    while 1 :
            wum_pus.print_board
            print "Vous êtes actuellement dans la case", board["player"]
            print "Il vous reste : ",arrows,"flèche(s)"
            possibilities = wum_pus.which_possibilities(board["player"])
            wum_pus.neighbours(possibilities, board)
            mode = wum_pus.which_action()
            if mode == 0:
                break
            elif mode == 2:
                arrows = arrows-1
            square = wum_pus.where_to_act(possibilities, mode)
            if square == 0:
                break
            final = wum_pus.consequence(mode,board,square)
            if final == True:
                break
            if arrows == 0:
                print "Vous n'avez plus assez de flèches pour tuer le Wum Pus. L'aventure s'arrête ici."
                break
