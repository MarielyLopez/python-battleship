#_*_coding: utf-8 _*_
#{[],[]} lista de lista
import random
import sys
import os
import time
#single player
table_game = []
#multi player
table_gamep1 = []
attack_table_gamep1 = []
table_gamep2 = []
attack_table_gamep2 = []
#para imprimir
print_table =[]

count_ships_p1 = 0
count_ships_p2 = 0

def createTable():
    for column in range(0, 10):
        table_game.append(["-"] * 10)
        print_table.append(["-"] * 10)
createTable()

def clear():
    """Cleans the data on screen."""
    if os.name == "posix":
        os.system("reset")
    elif os.name == ("nt"):
        os.system("cls")

def clear_list():
    del table_game[0:]
    del table_gamep1[0:]
    del table_gamep2[0:]
    del attack_table_gamep1[0:]
    del attack_table_gamep2[0:]
    del print_table[0:]
    createTable()

def play_again():
    clear_list()
    answer_userplay = True
    while answer_userplay == True:
        time.sleep(2)
        choose_user = raw_input("Do you want to play again y/n?: ")
        choose_user = choose_user.lower()
        if choose_user == "y":
            clear()
            user_menu()
        elif choose_user == "n":
            print "Good bye"
            sys.exit()
        else:
            print "Only can write -y- or -n- \n"

def answer_user(guess_row,guess_column,battle):
    """It checks if the player I win or fail, if the player I do not gain ire to the cycle if."""
    guess_column = int(guess_column)
    guess_row = int(guess_row)
    for c in battle:
        if guess_row == c["row"] and guess_column == c["col"]:
            clear()
            print "Great!!" + "\n" + "Congratulations! You sunk my battleship, and you sunk it hard.!"
            raw_input("Press enter to continue...")
            table_game[guess_row][guess_column] = "*"
            print_table[guess_row][guess_column] = "*"
            board_game(table_game)
            return 1
    if (guess_row < 0 or guess_row >= 10) or (guess_column < 0 or guess_column >= 10):
        clear()
        print "That is not in the ocean!!"
        raw_input("Press enter to continue: ")
        board_game(table_game)
        return 0
    elif table_game[guess_row][guess_column] == "x" or table_game[guess_row][guess_column] == "*":
        clear()
        print "You said that!"
        raw_input("Press enter to continue: ")
        board_game(table_game)
        return 0
    else:
        clear()
        print " You didn't sunk my battleship!!!. juju"
        print " "
        raw_input("Press enter to continue: ")
        table_game[guess_row][guess_column] = "x"
        print_table[guess_column][guess_row] = "x"
        board_game(table_game)
        return 0

#*****************Board game***********************

def generate_board_game():
    for column in range(0, 10):
        table_game.append(["-"] * 10)

def board_game(table_game):
    print " 0 1 2 3 4 5 6 7 8 9"
    number = 0
    for row in table_game:
        print "|" + "|".join(row) + "|" + str(number)#function join () will remove the "" lists.
        number+=1

#*****************Board game b1 ***********************

def generate_board_game():
    for column in range(0, 10):
        table_game_b1.append(["-"] * 10)

def board_game(table_game_b1):
    print " 0 1 2 3 4 5 6 7 8 9"
    number = 0
    for row in table_game_b1:
        print "|" + "|".join(row) + "|" + str(number)#function join () will remove the "" lists.
        number+=1

#*************************Multiplayer****************************
#*****************Board game player 1***********************

def generate_board_game_player_one():
    for columnp1 in range(0, 10):
        table_gamep1.append(["-"] * 10)
        attack_table_gamep1.append(["-"] * 10)

def board_game_player_one(table_gamep1):
    print "Board Game of Gamer one!"
    print " 0 1 2 3 4 5 6 7 8 9"
    number = 0
    for rowp1 in table_gamep1:
        print "|" + "|".join(rowp1) + "|" + str(number)#function join () will remove the "" lists.
        number+=1

#*****************Board game***********************

def generate_board_game_player_two():
    for columnp2 in range(0, 10):
        table_gamep2.append(["-"] * 10)
        attack_table_gamep2.append(["-"] * 10)

def board_game_player_two(table_gamep2):
    print "Board Game of Gamer two!"
    print " 0 1 2 3 4 5 6 7 8 9"
    number = 0
    for rowp2 in table_gamep2:
        print "|" + "|".join(rowp2) + "|" + str(number)#function join () will remove the "" lists.
        number+=1

#*********************************************

#GAMER ALONE
def random_row(table_game):
    return random.randint(0, len(table_game)-1)

def random_column(table_game):
    return random.randint(0, len(table_game[0])-1)

def Number_random():
    return random.randint(1,5)

b1 = [{"row":1,"col":1},{"row":2,"col":2},{"row":3,"col":3},{"row":4,"col":4},{"row":5,"col":5},{"row":6,"col":6},{"row":7,"col":7},{"row":8,"col":8},{"row":1,"col":8},{"row":2,"col":7},{"row":3,"col":6},{"row":4,"col":5},{"row":5,"col":4},{"row":6,"col":3},{"row":7,"col":2},{"row":8,"col":1}]
b2 = [{"row":0,"col":2},{"row":0,"col":3},{"row":0,"col":4},{"row":0,"col":5},{"row":0,"col":6},{"row":0,"col":7},{"row":0,"col":8},{"row":1,"col":1},{"row":2,"col":1},{"row":3,"col":1},{"row":3,"col":2},{"row":3,"col":3},{"row":3,"col":4},{"row":3,"col":5},{"row":3,"col":6},{"row":3,"col":7},{"row":3,"col":8},{"row":6,"col":1},{"row":6,"col":2},{"row":6,"col":3},{"row":6,"col":4},{"row":6,"col":5},{"row":7,"col":5},{"row":8,"col":5},{"row":9,"col":5},{"row":9,"col":4},{"row":9,"col":3},{"row":9,"col":2},{"row":9,"col":1}]
b3 = [{"row":0,"col":2},{"row":4,"col":0},{"row":7,"col":0},{"row":6,"col":1},{"row":2,"col":2},{"row":4,"col":2},{"row":0,"col":4},{"row":2,"col":4},{"row":3,"col":4},{"row":2,"col":5},{"row":6,"col":5},{"row":7,"col":5},{"row":7,"col":8},{"row":1,"col":8},{"row":7,"col":8},{"row":5,"col":7},{"row":7,"col":7}]
b4 = [{"row":0,"col":2},{"row":4,"col":0},{"row":1,"col":2},{"row":6,"col":0},{"row":5,"col":2},{"row":9,"col":2},{"row":0,"col":4},{"row":3,"col":4},{"row":7,"col":5},{"row":0,"col":7},{"row":6,"col":7},{"row":3,"col":8},{"row":9,"col":9},{"row":5,"col":5}]
b5 = [{"row":1,"col":1},{"row":2,"col":2},{"row":5,"col":5},{"row":5,"col":1},{"row":9,"col":0},{"row":8,"col":8},{"row":8,"col":2},{"row":4,"col":3},{"row":7,"col":3},{"row":2,"col":4},{"row":6,"col":4},{"row":8,"col":4},{"row":9,"col":5},{"row":1,"col":5},{"row":4,"col":6},{"row":2,"col":7},{"row":8,"col":7},{"row":5,"col":8},{"row":9,"col":9},{"row":7,"col":9},{"row":4,"col":9},{"row":1,"col":9}]
b6 = [{"row":0,"col":1},{"row":1,"col":1},{"row":2,"col":1},{"row":4,"col":9},{"row":5,"col":9},{"row":3,"col":3},{"row":3,"col":4},{"row":3,"col":5},{"row":0,"col":7},{"row":0,"col":8},{"row":7,"col":9},{"row":7,"col":8},{"row":7,"col":7},{"row":7,"col":6},{"row":7,"col":5}]
b7 = [{"row":5,"col":0},{"row":5,"col":1},{"row":4,"col":2},{"row":3,"col":2},{"row":2,"col":2},{"row":8,"col":4},{"row":7,"col":4},{"row":9,"col":5},{"row":9,"col":4},{"row":9,"col":3},{"row":5,"col":6},{"row":4,"col":6},{"row":3,"col":6},{"row":2,"col":6},{"row":1,"col":6}]

def random_play():
    number = Number_random()
    print number
    if number == 1:
        table = b1
        for boat in table:
            print_table[boat["row"]][boat["col"]] = "A"
        return table
    elif number == 2:
        table = b2
        for boat in table:
            print_table[boat["row"]][boat["col"]] = "B"
        return table
    elif number == 3:
        table = b3
        for boat in table:
            print_table[boat["row"]][boat["col"]] = "C"
        return table
    elif number == 4:
        table = b4
        for boat in table:
            print_table[boat["row"]][boat["col"]] = "D"
        return table
    elif number == 5:
        table = b5
        for boat in table:
            print_table[boat["row"]][boat["col"]] = "E"
        return table
    elif number == 6:
        table = b6
        for boat in table:
            print_table[boat["row"]][boat["col"]] = "F"
        return table
    elif number == 7:
        table = b7
        for boat in table:
            print_table[boat["row"]][boat["col"]] = "G"
        return table

points_single = 0
def ask_user():
    battle = random_play()
    clear()
    print "Single Player"
    print " "
    points_single = 0
    board_game(table_game)
    def turns():
        print ""
        print "Your turn is ", turn
        print ""
        guess_row = raw_input("Guess row: ")
        guess_column = raw_input("Guess column: ")
        clear()
        if False == guess_row.isdigit():
            print "    Insert Numbers, please."
            board_game(table_game)
            
        else:
            score_2 = answer_user(guess_row,guess_column,battle)
    answeruserask = True
    while answeruserask == True:
        turn = 0
        for turn in range(1,5):
            if turn == 4:
                turns()
                board_game(table_game)
                clear()
                print "Game over!!!"
                print 'The ships that you sunk, are marked with "*"'
                print 'The shots that you trumped, are marked with "x"'
                board_game(print_table)
                play_again()
                answeruserask = False
            else:
                turns()
boot  = []


# ****************MULTIPLAYER****************

def player_Multi():
    turn = True
    while turn == True:
        clear_list()
        board_gamep1 = generate_board_game_player_one()
        board_gamep2 = generate_board_game_player_two()
        battle_1 = position_player1()
        battle_2 = position_player2()
        turn = turns(battle_1,battle_2)
    clear()
    user_menu()

def turns(battle_1,battle_2):
    puntosp1 = 0
    puntosp2 = 0
    global count_ships_p1
    global count_ships_p2
    count_ships_p1 = count_ships_p1 * 0
    count_ships_p2 = count_ships_p2 * 0
    for x in range(1,5):
        print "Your turn is",x
        a1 = attack_player_one(battle_2)
        if a1 == None:
            pass
        else:
            puntosp1 = puntosp1 + a1
            if puntosp1 == 2:
                print "You derived all ships"
                break
        print "Your turn is",x
        a2 = attacK_player_two(battle_1)
        if a2 == None:
            pass
        else:
            puntosp2 = puntosp2 + a2
            if puntosp2 == 2:
                print "You derived all ships"
                break
    try_play()

def try_play():
    m = raw_input("Do you want to play again y/n?")
    if m == "y":
        return True
    else:
        return False

def position_player1():
    barcosp1 = []
    for cord in range(1,5):
            number_repeatp1 = True
            while number_repeatp1 == True:
                print"PLAYER ONE"
                board_game_player_one(table_gamep1)
                print "Insert the coordinate, where  you want  to conceal your ship."
                verific_position_p1 = True
                while verific_position_p1 == True:
                    coordinate1_player1 = raw_input("--> Insert row: ")
                    coordinate2_player1 = raw_input("--> Insert column: ")
                    if False == coordinate1_player1.isdigit() or False == coordinate2_player1.isdigit():
                        print "Insert numbers."
                        verific_position_p1 = True
                    else:
                        verific_position_p1 = False
                        verific_position_p1 = ver_hor_p1(coordinate1_player1,coordinate2_player1)
                coordinate1_player1 = int(coordinate1_player1)
                coordinate2_player1 = int(coordinate2_player1)
                if len(barcosp1) != 5:
                    table_gamep1[coordinate1_player1][coordinate2_player1] = "H"
                    barcosp1.append({"row":coordinate1_player1,"col":coordinate2_player1})#aboatui se aguarda las corrdenadas ingresadas por el usuario
                    print " "
                    raw_input("  Press Enter...")
                    clear()
                    number_repeatp1 = False
                else:
                    if attack_table_gamep1[coordinate1_player1][coordinate2_player1] == "H":
                        clear()
                        print "That position not found..."
                        number_repeatp1 = True
                    else:
                        table_gamep1[coordinate1_player1][coordinate2_player1] = "H"
                        barcosp1.append({"row":coordinate1_player1,"col":coordinate2_player1})#aboatui se aguarda las corrdenadas ingresadas por el usuario
                        clear()
                        number_repeatp1 = False
    raw_input("Press enter to continue player Two... ")
    return barcosp1


def ver_hor_p1(coordinate1_player1,coordinate2_player1):
    coordinate1_player1 = int(coordinate1_player1)
    coordinate2_player1 = int(coordinate2_player1)
    h_v_userp1 = True
    while h_v_userp1 == True:
        print "Which direction you want to conceal your ship?"
        user_v_hp1 = raw_input("Horizontal or Vertical?: ")
        user_v_hp1 = user_v_hp1.lower()

        if user_v_hp1 == "vertical":
                p1 = coordinate1_player1 + 1
                p2 = p1 + 1
                p3 = p2 + 1
                p4 = p3 +1
                if coordinate1_player1 > 9 or p1 > 9 or p2 > 9 or p3 > 9 or p4 > 9 or coordinate2_player1 > 9:
                    print "You cannot place your ship here because a part of this one out of the ocean. "
                    raw_input("Press enter to continue...")
                    clear()
                    return True
                else:
                    if table_gamep1[p1][coordinate2_player1] == "H":
                        print "This position already exists"
                        raw_input("Press enter to continue...")
                        clear()
                        return True
                    else:
                        table_gamep1[p1][coordinate2_player1] = "H"
                        if table_gamep1[p2][coordinate2_player1] == "H":
                            print "This position already exists"
                            raw_input("Press enter to continue...")
                            clear()
                            return True
                        else:
                            table_gamep1[p2][coordinate2_player1] = "H"
                            if table_gamep1[p3][coordinate2_player1] == "H":
                                print "This position already exists"
                                raw_input("Press enter to continue...")
                                clear()
                                return True
                            else:
                                table_gamep1[p3][coordinate2_player1] = "H"
                                if attack_table_gamep1[p4][coordinate2_player1] == "H":
                                    print "This position already exists"
                                    raw_input("Press enter to continue...")
                                    clear()
                                    return True
                                else:
                                    attack_table_gamep1[p4][coordinate2_player1] = "H"
                        return False
                h_v_userp1 = False
        elif user_v_hp1 == "horizontal":
            p1 = coordinate2_player1 + 1
            p2 = p1 + 1
            p3 = p2 + 1
            p4 = p3 + 1
            if coordinate1_player1 > 9 or p1 > 9 or p2 > 9 or p3 > 9 or p4 > 9 or coordinate2_player1 > 9:
                print "You cannot place your ship here because a part of this one out of the ocean. "
                raw_input("Press enter to continue...")
                clear()
                return True
            else:
                if table_gamep1[coordinate1_player1][p1] == "H":
                    print "This position already exists"
                    raw_input("Press enter to continue...")
                    clear()
                    return True
                else:
                    table_gamep1[coordinate1_player1][p1] = "H"
                    if table_gamep1[coordinate1_player1][p2] == "H":
                        print "This position already exists"
                        raw_input("Press enter to continue...")
                        clear()
                        return True
                    else:
                        table_gamep1[coordinate1_player1][p2] = "H"
                        if table_gamep1[coordinate1_player1][p3] == "H":
                            print "This position already exists"
                            raw_input("Press enter to continue...")
                            clear()
                            return True
                        else:
                            table_gamep1[coordinate1_player1][p3] = "H"
                            if table_gamep1[coordinate1_player1][p4] == "H":
                                print "This position already exists"
                                raw_input("Press enter to continue player two...")
                                clear()
                                return True
                            else:
                                table_gamep1[coordinate1_player1][p4] = "H"
                    return False
            h_v_userp1 = False
        else:
            clear()
            print "IT'S BAD!!! :O-O:"
            print "            : o :"
            print "Only write horizontal or vertical, please!"

def position_player2():
#    clear()
    barcosp2 = []
    for cordp2 in range(1,5):
            number_repeatp2 = True
            while number_repeatp2 == True:
                print "PLAYER TWO"
                board_game_player_two(table_gamep2)
                print "Insert the coordinate, where  you want  to conceal your ship."
                verific_position_p2 = True
                while verific_position_p2 == True:
                    coordinate1_player2 = raw_input("--> Insert row: ")
                    coordinate2_player2 = raw_input("--> Insert column: ")
                    if False == coordinate1_player2.isdigit() or False == coordinate2_player2.isdigit():
                        print "Insert numbers player TWO."
                        verific_position_p2 = True
                    else:
                        verific_position_p2 = False
                        verific_position_p2 = ver_hor_p2(coordinate1_player2,coordinate2_player2)
                coordinate1_player2 = int(coordinate1_player2)
                coordinate2_player2 = int(coordinate2_player2)
                if len (barcosp2) != 5:
                    table_gamep2[coordinate1_player2][coordinate2_player2] = "B"
                    barcosp2.append({"row":coordinate1_player2,"col":coordinate2_player2})
                    print " "
                    raw_input("Press enter to continue...")
                    clear()
                    number_repeatp2 = False
                else:
                    if attack_table_gamep2[coordinate1_player2][coordinate2_player2] == "B":
                        clear()
                        print "That position not found..."
                        number_repeatp2 = True
                        print("ha!_p2")
                    else:
                        table_gamep2[coordinate1_player2][coordinate2_player2] = "B"
                        barcosp2.append({"row":coordinate1_player2,"col":coordinate2_player2})
                        clear()
                        number_repeatp2 = False
    raw_input("Press enter to continue the battle..")
    return barcosp2


def ver_hor_p2(coordinate1_player2,coordinate2_player2):
    coordinate1_player2 = int(coordinate1_player2)
    coordinate2_player2 = int(coordinate2_player2)
    h_v_userp2 = True
    while h_v_userp2 == True:
        print "Which direction you want to conceal your ship?"
        user_v_hp2 = raw_input("Horizontal or Vertical?: ")
        user_v_hp2 = user_v_hp2.lower()
        if user_v_hp2 == "vertical":
            p1 = coordinate1_player2 + 1
            p2 = p1 + 1
            p3 = p2 + 1
            p4 = p3 +1
            if coordinate1_player2 > 9 or p1 > 9 or p2 > 9 or p3 > 9 or p4 > 9 or coordinate2_player2 > 9:
                print "You cannot place your ship here because a part of this one out of the ocean. "
                raw_input("Press enter to continue...")
                clear()
                return True
            else:
                if table_gamep2[p1][coordinate2_player2] == "B":
                    print "This position already exists"
                    raw_input("Press enter to continue...")
                    clear()
                    return True
                else:
                    table_gamep2[p1][coordinate2_player2] = "B"
                    if table_gamep2[p2][coordinate2_player2] == "B":
                        print "This position already exists"
                        raw_input("Press enter to continue...")
                        clear()
                        return True
                    else:
                        table_gamep2[p2][coordinate2_player2] = "B"
                        if table_gamep2[p3][coordinate2_player2] == "B":
                            print "This position already exists"
                            raw_input("Press enter to continue...")
                            clear()
                            return True
                        else:
                            table_gamep2[p3][coordinate2_player2] = "B"
                            if attack_table_gamep2[p4][coordinate2_player2] == "B":
                                print "This position already exists"
                                raw_input("Press enter to continue...")
                                clear()
                                return True
                            else:
                                attack_table_gamep2[p4][coordinate2_player2] = "B"
                        return False
                h_v_userp2 = False
        elif user_v_hp2 == "horizontal":
            p1 = coordinate2_player2 + 1
            p2 = p1 + 1
            p3 = p2 + 1
            p4 = p3 + 1
            if coordinate1_player2 > 9 or p1 > 9 or p2 > 9 or p3 > 9 or p4 > 9 or coordinate2_player2 > 9:
                print "You cannot place your ship here because a part of this one out of the ocean. "
                raw_input("Press enter to continue...")
                clear()
                return True
            else:
                if table_gamep2[coordinate1_player2][p1] == "B":
                    print "This position already exists"
                    raw_input("Press enter to continue...")
                    clear()
                    return True
                else:
                    table_gamep2[coordinate1_player2][p1] = "B"
                    if table_gamep2[coordinate1_player2][p2] == "B":
                        print "This position already exists"
                        raw_input("Press enter to continue...")
                        clear()
                        return True
                    else:
                        table_gamep2[coordinate1_player2][p2] = "B"
                        if table_gamep2[coordinate1_player2][p3] == "B":
                            print "This position already exists"
                            raw_input("Press enter to continue...")
                            clear()
                            return True
                        else:
                            table_gamep2[coordinate1_player2][p3] = "B"
                            if table_gamep2[coordinate1_player2][p4] == "B":
                                print "This position already exists."
                                raw_input("Press enter to continue whit the battle!...")
                                clear()
                                return True
                            else:
                                table_gamep2[coordinate1_player2][p4] = "B"
                    return False
            h_v_userp2 = False
        else:
            clear()
            print "IT'S BAD!!! :O-O:"
            print "            : o :"
            print "Only write horizontal or vertical, please!"


def attack_player_one(battle_1):
    board_game_player_one(table_gamep1)
    board_game_player_two(attack_table_gamep2)
    verific_attack_p1 = True
    while verific_attack_p1 == True:
        attack1_p1 = raw_input("Player 1, insert the row that you want attack!: ")
        attack2_p1 = raw_input("Player 1, insert the column that you want attack!: ")
        if False == attack1_p1.isdigit() or False == attack2_p1.isdigit():
            print "Insert numbers."
            raw_input("Press enter to continue...")
            clear()
        else:
            a1 = answer_player1(attack1_p1,attack2_p1,battle_1)
            verific_attack_p1 = False
    return a1
def answer_player1(guess_row,guess_column,battle_1):
    guess_column = int(guess_column)
    guess_row = int(guess_row)
    global count_ships_p1
    for co in battle_1:#Every ship is print in battle_1
        if guess_row == co["row"] and guess_column == co["col"]:
            clear()
            print "Great!!" + "\n" + "Congratulations! You sunk my battleship, and you sunk it hard.!"
            count_ships_p1 = count_ships_p1 + 1
            table_gamep2[guess_row][guess_column] = "*"
            attack_table_gamep2[guess_row][guess_column] = "*"
            board_game_player_one(table_gamep1)
            board_game_player_two(attack_table_gamep2)
            print "You sunk ",count_ships_p1, "of ",len(battle_1)
            raw_input("Press enter to continue player two...")
            return 1
    if (guess_row < 0 or guess_row >= 10) or (guess_column < 0 or guess_column >= 10):
        clear()
        print "That is not in the ocean!!"
        raw_input("Press enter to continue: ")
        board_game_player_one(table_gamep1)
        board_game_player_two(attack_table_gamep2)
        print "You sunk ",count_ships_p1, "of ",len(battle_1)
        raw_input("Press enter to continue player two...")
        clear()
    elif table_gamep2[guess_row][guess_column] == "x":
        clear()
        print "You said that!"
        raw_input("Press enter to continue: ")
        board_game_player_one(table_gamep1)
        board_game_player_two(attack_table_gamep2)
        print "You sunk ",count_ships_p1, "of ",len(battle_1)
        raw_input("Press enter to continue player two...")
        clear()
    else:
        clear()
        print "You didn't sunk my battleship!!!. juju"
        print " "
        raw_input("Press enter to continue: ")
        clear()
        table_gamep2[guess_row][guess_column] = "x"
        attack_table_gamep2[guess_row][guess_column] = "x"
        board_game_player_one(table_gamep1)
        board_game_player_two(attack_table_gamep2)
        print "You sunk ",count_ships_p1, "of ",len(battle_1)
        raw_input("Press enter to continue player two...")


def attacK_player_two(battle_2):
#    clear()
    board_game_player_two(table_gamep2)
    board_game_player_one(attack_table_gamep1)
    verific_attack_p2 = True
    while verific_attack_p2 == True:
        attack1_p2 = raw_input("Player 2, insert the row that you want attack!: ")
        attack2_p2 = raw_input("Player 2, insert the column that you want attack!: ")
        if False == attack1_p2.isdigit() or False == attack2_p2.isdigit():
            print "Insert numbers"
            raw_input("Press enter to continue...")
            clear()
        else:
            a2 = answer_player2(attack1_p2,attack2_p2,battle_2)
            verific_attack_p2 = False
    return a2
def answer_player2(guess_rowp2,guess_columnp2,battle_2):
    guess_columnp2 = int(guess_columnp2)
    guess_rowp2 = int(guess_rowp2)
    global count_ships_p2
    for co2 in battle_2:
        if guess_rowp2 == co2["row"] and guess_columnp2 == co2["col"]:
            clear()
            print "Great!!" + "\n" + "Congratulations! You sunk my battleship, and you sunk it hard.!"
            count_ships_p2 = count_ships_p2 + 1
            table_gamep1[guess_rowp2][guess_columnp2] = "*"
            attack_table_gamep1[guess_rowp2][guess_columnp2] = "*"
            board_game_player_two(table_gamep2)
            board_game_player_one(attack_table_gamep1)
            print "You sunk ",count_ships_p2," of", len(battle_2)
            raw_input("Press enter to continue player one...")
            clear()
            return 1
    if (guess_rowp2 < 0 or guess_rowp2 >= 10) or (guess_columnp2 < 0 or guess_columnp2 >= 10):
        clear()
        print "That is not in the ocean!!"
        raw_input("Press enter to continue: ")
        board_game_player_two(table_gamep2)
        board_game_player_one(attack_table_gamep1)
        print "You sunk ",count_ships_p2, " of",len(battle_2)
        raw_input("Press enter to continue player one...")
        clear()
    elif table_gamep1[guess_rowp2][guess_columnp2] == "x":
        clear()
        print "You said that!"
        raw_input("Press enter to continue... ")
        board_game_player_two(table_gamep2)
        board_game_player_one(attack_table_gamep1)
        print "You sunk ",count_ships_p2," of", len(battle_2)
        raw_input("Press enter to continue player one...")
        clear()
    else:
        clear()
        print "You didn't sunk my battleship!!!. juju"
        print " "
        raw_input("Press enter to continue: ")
        clear()
        table_gamep1[guess_rowp2][guess_columnp2] = "x"
        attack_table_gamep2[guess_rowp2][guess_columnp2] = "x"
        board_game_player_two(table_gamep2)
        board_game_player_one(attack_table_gamep2)
        print"You sunk ",count_ships_p2," of", len(battle_2)
        raw_input("Press enter to continue player one...")




def instructions_game():
    print ""
    print "                   Hi !!"
    print "          Welcome to Battleship !!"
    print "1. If you be a single player:"
    print "     All boats are random, if you're lucky,"
    print "     you can leave one position boats"
    print "     and if you will not come much bigger boats."
    print " "
    print "2. If you be someting of players:"
    print "     you can to hide your own ships in anywhere of the ocean."
    print " "
    print "3. You can only insert numbers for 0 to 9."
    print " "
    raw_input("Press enter to continue...")
    clear()
    user_menu()


def player_vs_bot():
    ask_user()

def print_menu():
    print " "
    print "                  1.One player."
    print "                  2.Multiplayer."
    print "                  3.Instrucctions."
    print "                  4.Exit."
    print " "


def menu():
    answerusermenu = True
    while answerusermenu == True:
        answer_usermenu = raw_input("Insert your option >>:  ")
        print " "
        clear()
        if answer_usermenu == "1" or answer_usermenu == "One player":
            player_vs_bot()
        elif answer_usermenu == "2" or answer_usermenu == "Multiplayer":
            player_Multi()
            print "Sharks surrounded us! Insert other option or Please try later"
            answerusermenu = True
        elif answer_usermenu == "3" or answer_usermenu == "Instructions":
            instructions_game()
        elif answer_usermenu == "4" or answer_usermenu == "Exit":
            print "See you soon, bye bye.!!"
            sys.exit()
        else:
            clear()
            print ""
            print "     Insert the number or name to option."
            print_menu()

def user_menu():
    print ""
    print "===================================================="
    print "=               Welcome to Battle Ship             ="
    print "===================================================="
    print_menu()
    menu()

user_menu()