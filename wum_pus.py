# -*- coding: utf-8 -*-

"""
    This module contains all the functions required to play Wum Pus.
"""

import sys
import random

def main_menu():
    """
        Displays the title screen and allows the player to choose if he wants to play the game, read the rules or leave the game. This fonction does not call for any parameter.
        
        :return: an information on what the player wants to do
        :rtype: boolean
        
        ..note:: the program is stopped if the player press 'O'
    """
    print """
.==============================================.
|  __    __                     ___            |
| / / /\ \ \_   _ _ __ ___     / _ \_   _ ___  |
| \ \/  \/ / | | | '_ ` _ \   / /_)/ | | / __| |
|  \  /\  /| |_| | | | | | | / ___/| |_| \__ \ |
|   \/  \/  \__,_|_| |_| |_| \/     \__,_|___/ |
|                                              |
'=============================================='
"""
    print ("\n1: Jouer\n\n2: Règles du jeu\n\n0: Quitter\n")
    selection = raw_input()
    while selection != "1" and selection != "2" and selection != "0":
        print ("\n1: Jouer\n2: Règles du jeu\n0: Quitter\n")
        selection = raw_input()
    if selection == "1":
        play = True
    elif selection == "2":
        play = False
    else:
        sys.exit()
    return play


def rules():
    """
    Une petite histoire pour vous aidez un peu.

    Dans le labyrinthe magique où vous venez d'entrer se cache un terrible monstre. Il est accompagné de ses accolytes : 2 chauves souris et a posé des puits afin de vous empéchez de le retrouver.
    Si vous avez le malheur de tomber dans un des puits, la chute vous brisera les os et vous mourrez dans d'atroces souffrances. Le bruit du vent vous indiquera la présence d'un puit dans une des
    cases adjacentes à la votre.
    Les chauves souris, si vous les rencontrez, vous transporterons où elles le voudrons dans le labyrinthe, vous les repèrerez à l'aide du battement de leurs ailes.
    Le monstre, appelé Wum Pus quand à lui dort tranquillement dans l'une des chambres, celui-ci ronfle tellement fort que vous pourrez le repéré et essayer de le tuer à l'aide de vos flèches.
    Méfiez vous tout de même car vous ne disposez que de trois flèches et si vous n'atteignez pas le monstre il se déplacera dans l'une des cases jonchant la sienne, vous pourriez donc vous
    faire dévorer à cause de votre mauvais tir.

    Bonne chance ...
    
    """
    help(rules)
    return


def print_board():
    """
        Displays a static board of the game.
    """
    print ("         12----------7")
    print ("        /  \        /  \ ")
    print ("       /    6------1    \ ")
    print ("      /    /        \    \ ")
    print ("     11---5          2---8 ")  
    print ("      \    \        /    / ")
    print ("       \    4------3    /  ")
    print ("        \  /        \  /   ")
    print ("         10----------9 ")


def which_possibilities(x):
    """
        Returns the 3 possibilities in between wich the player will have to choose, depending on where he is at the beginning of the turn.
    
        :param x: square where the player stands
        :type x: integer
        :return: the 3 possibilities
        :rtype: tuple

        :Example:

        >>> which_possibilities(6)
        (12, 5, 1)
        >>> which_possibilities(1)
        (7, 6, 2)
    
    """
    if x <= 6:
        choice1 = x+6
        if x == 1:
            choice2 = 6
        else:
            choice2 = x-1
        if x == 6:
            choice3 = 1
        else:
            choice3 = x+1
    else:
        choice1 = x-6
        if x == 7:
            choice3 = 12
        else:
            choice3 = x-1
        if x == 12:
            choice2 = 7
        else:
            choice2 = x+1
    return choice1,choice2,choice3


def neighbours(t,b):
    """
        Displays messages depending on the occupant of the squares nearby the player. All those squares are tested and compared to the current board. If they are empty, player receive no specific message.
    
        :param t: numbers of adjacent squares
        :type t: list, tuple
        :param b: game board, allow to test the contents of the squares
        :type b: dictionary
        .. seealso:: which_possibilities()
    """
    for i in t:
        if  b["wum"] == i:
            print "ZZZZZZzzzzzzzzzzzzzzzzzzzz"
        elif (b["well1"] or b["well2"]) == i:
            print "whouuuuuuuuuuuuuuuuu"
        elif (b["bat1"] or b["bat2"]) == i:
            print "flap flap flap flap flap"
    return


def which_action():
    """
        Returns a integer corresponding to the choice of the player of moving through the maze, trying to kill the Wum Pus or leaving the game. This integer have to be 0, 1 or 2. In other case an error message will be send until the player chooses a correct option. This function does not call for any parameter.

        :return: the choice of the player
        :rtype: integer

    """
    print ("Que voulez-vous faire ?")
    choice = raw_input("1: Vous déplacer\n2: Tirer une fleche\n\n0: Retour au menu\n")
    while choice != "1" and choice != "2" and choice != "0":
        print ("Vous devez choisir parmi les options suivante (1, 2 ou 0)")
        choice = raw_input("1: Vous déplacer\n2:Tirer une fleche\n\n0: Retour au menu\n")
    return int(choice)


def where_to_act(a, b):
    """
        Returns a number of square as an integer, chosen by the player according to the direction in which he wants to go or to fire an arrow. Message is displayed depending on which mode is defined.

        :param a: all the square reachable by the player
        :type a: list, tuple
        :param b: mode defined by a previous choice of the player (move or shoot)
        :type b: integer
        :return: the number of the square chosen by the player
        :rtype: integer

        .. seealso:: which_possibilities(), which_action()

    """
    if b == 1:
        print ("Ou voulez-vous allez ?")
    if b == 2:
        print ("Où voulez-vous tirer ?")
    ("1: En face\n2: A gauche\n3: A droite\n\n0: Retour au menu\n")
    direction = raw_input("1: En face\n2: A gauche\n3: A droite\n\n0: Retour au menu\n")
    while direction not in ["0", "1", "2", "3"]:
        print ("Vous devez choisir parmi les options suivante (1, 2, 3 ou 0):")
        direction = raw_input("1: En face\n2: A gauche\n3: A droite\n\n0: Retour au menu\n")
    if direction == "0":
        choice = 0
    elif direction == "1":
        choice = a[0]
    elif direction == "2":
        choice = a[1]
    elif direction == "3":
        choice = a[2]
    return choice


def consequence(a,b,c):
    """
        Determines the events that will happen, according choices previously made by the player (mode and direction). Consequences also depend on the contents of the chosen square.

        :param a: mode defined by a previous choice of the player (move or shoot)
        :type a: integer
        :param b: game board, allow to change the position of the player an to test the contents of the chosen squares
        :type b: dictionary
        :param c: square chosen previously by the player
        :type c: integer
        :return: an information which allows to known if the game has to be stopped or not
        :rtype: boolean
        
        .. seealso:: bat_shifting(), wum_shifting()
    
    """
    if a == 1:
        if b["wum"] == c:
            print ("Vous avez réveillé le Wum Pus ! Celui-ci se jette sur vous et vous dévore. Ici s'achève votre aventure.")
            end = True
        elif b["well1"]== c or b["well2"] == c:
            print ("Un pas de trop dans un puits sans fond. Ici s'achève votre aventure.")
            end = True
        elif b["bat1"]== c or b["bat2"] == c:
            end = bat_shifting(b)
        else:
            b["player"] = c
            end = False
    elif a == 2:
        if b["wum"] == c:
            print ("Bravo ! Vous avez vaincu le Wum Pus ! Vous pouvez maintenant rentrer chez vous et montrer à votre village qui est le plus fin stratège !")
            end = True
        else:
            end = wum_shifting(b)
    return end


def bat_shifting(a):
    """
        Randomly determines a square in which the bat drops the player off. It can not be a square with a bat. If the new square contains Wum Pus or a well, the game will be stopped, otherwise the player will get a new position on the board.
    
        :param a: the game board, allows to change the position of the player an to test the contents of the chosen squares
        :type a: dictionary
        :return: an information which allows to known if the game has to be stopped or not
        :rtype: boolean
    
    """
    nobat = []
    for i in range(1, 13):
        if i != a["bat1"] or i != a["bat2"]:
            nobat.append(i)
        new_square = random.choice(nobat)
    if new_square == a["wum"]:
        print "La chauve souris vous a laissé entre les griffes du Wum Pus, c'en est fini de vous !"    
        death = True
    elif new_square == a["well1"] or new_square == a["well2"]:
        print "La chauve souris vous a laissé dans un puits sans fond, c'en est fini de vous !"
        death = True
    else:
        a["joueur"] = new_square
        death = False
    return death


def wum_shifting(a):
    """
        Randomly chooses a adjacent square to the Wum Pus position. It can not be a well. If it's a bat, Wum Pus is randomly placed in another squared, except those containing well or bat.If the new square contains the player, the game will be stopped, otherwise the Wum Pus will get a new position on the board.

        :param a: the game board, allows to change the position of the Wum Pus an to test the contents of the chosen squares
        :type a: dictionary
        :return: an information which allows to known if the game has to be stopped or not
        :rtype: boolean

    """
    l =list(which_possibilities(a["wum"]))
    empty = []
    if a["well1"] in l:
        l.remove(a["well1"])
    if a["well2"] in l:
        l.remove(a["well2"])
    new_square = random.choice(l)
    if new_square == a["bat1"] or new_square == a["bat2"]:
         for j in range(1,13):
             if j != a["well1"] and j != a["well2"] and j != new_square["bat1"] and j != new_square["bat2"] :
                 empty.append(j)
         new_square = random.choice(empty)
    elif new_square == a["player"]:
        print "Vous avez réveillé le Wum Pus et il vous a retrouvé. Vous avez perdu !"
        death = True
    else:
        print "Vous avez réveillé le Wum Pus"
        death = False
        a["wum"] = new_square
    return death


if __name__ == "__main__":
    import doctest
    doctest.testmod()
