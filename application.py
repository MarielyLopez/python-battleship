#coding:utf-8
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
def createTable():
    for column in range(0, 10):
        table_game.append(["-"] * 10)
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
    createTable()
    #board_game(table_game[0])


def play_again():
    clear_list()
    answer_userplay = True
    while answer_userplay == True:
        time.sleep(2)
        choose_user = raw_input("Do you want to play again y/n: ")
        choose_user = choose_user.lower()
        if choose_user == "y":
            user_menu()
        elif choose_user == "n":
            print "Good bye"
            sys.exit()
        else:
            print "Only can write -y- or -n- \n"


def answer_user(guess_row,guess_column,battle_row,battle_column):
    guess_column = int(guess_column)
    guess_row = int(guess_row)
    if guess_row == battle_row and guess_column == battle_column:
        print "Great!!" + "\n" + "Congratulations! You sunk my battleship, and you sunk it hard.!"
        table_game[guess_column][guess_row] = "x"
        board_game(table_game)
        play_again()
    else:
        if (guess_row < 0 or guess_row >= 11) or (guess_column < 0 or guess_column >= 11):
            print "That is not in the ocean!!"
#            print " "
            board_game(table_game)
        elif table_game[guess_row][guess_column] == "x":
            print "You said that!"
            board_game(table_game)
        else:
            print "You didn't sunk my battleship, You didn't sunk my battleship!!!. juju"
            print " "
            table_game[guess_row][guess_column] = "x"

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

def random_play():
    battle_row = random_row(table_game)
    battle_column = random_column(table_game)
    return battle_row,battle_column

def ask_user():
    battle_row,battle_column = random_play()
    print battle_row
    print battle_column

    def turnos():
        #clear_list()
        #clear()
        board_game(table_game)
        print ""
        print "Your turn is ", turno
        print ""
        guess_row = raw_input("Guess row: ")
        guess_column = raw_input("Guess column: ")
        if False == guess_row.isdigit():
            print "insert numbers"
        else:
            answer_user(guess_row,guess_column,battle_row,battle_column)
    answeruserask = True
    while answeruserask == True:
        turno = 0
        for turno in range(1,5):
            if turno == 4:
                turnos()
                board_game(table_game)
                print "Game over!!!"
                print "My ship it is in the row:",battle_row, "and the column:",battle_column
                play_again()
                answeruserask = False
            else:
                turnos()

def player_Multi():
    #user_menu()
    turn = True
    while turn == True:
        clear_list()
        board_gamep1 = generate_board_game_player_one()
        board_gamep2 = generate_board_game_player_two()
        #print board_game_player_one(table_gamep1)
        #answer_player1(coordenada1_jugador1,coordenada2_jugador1)
        battle_1 = posicion_jugador1()
        battle_2 = posicion_jugador2()
        turn = turnos(battle_1,battle_2)
    clear()
    user_menu()

def turnos(battle_1,battle_2):
    puntosp1 = 0
    puntosp2 = 0
    for x in range(1,5):
        print "su turno es",x       
        a1 = attack_player_one(battle_2)#aqui uso los barcos como parametros para luego poder utilizarlos en la funcion de abajo.
        if a1 == None:
            #print "derivaste todos los barcos"
            pass
        else:
            puntosp1 = puntosp1 + a1
            if puntosp1 == 2:
                print "Derivaste todos los barcos"
                break

        print "su turno es",x  
        a2 = attacK_player_two(battle_1)
        if a2 == None:
            #print "derivaste todos los barcos"
            pass
        else:
            puntosp2 = puntosp2 + a2
            if puntosp2 == 2:
                print "Derivaste todos los barcos"
                break

    m = raw_input("quieres jugar de nuevo y/n?: ")
    if m == "y":
        return True
    else:
        return False


def posicion_jugador1():
    clear()
    barcos = []
    for cord in range(1,3):

        print"PLAYER ONE"
        print "Ingrese la Coordenada donde quiere ocultar su barco."
        coordenada1_jugador1 = input("--> Inserta fila: ")
        coordenada2_jugador1 = input("--> Inserta columna: ")
    #    coordenada_jugador = coordenadas_barco()
        table_gamep1[coordenada1_jugador1][coordenada2_jugador1] = "H"
        board_game_player_one(table_gamep1)
        barcos.append({"fila":coordenada1_jugador1,"col":coordenada2_jugador1})#aqui se aguarda las corrdenadas ingresadas por el usuario
    return barcos



def posicion_jugador2():
    raw_input("Enter para continuar...")
    clear()
    barcosp2 = []
    for cordp2 in range(1,3):

        print "PLAYER TWO"
        print "Ingrese la Coordenada donde quiere ocultar su barco."
        coordenada1_jugador2 = input("--> Inserta fila: ")
        coordenada2_jugador2 = input("--> Inserta columna: ")
    #    coordenada_jugador = coordenadas_barco()
        table_gamep2[coordenada1_jugador2][coordenada2_jugador2] = "B"
        board_game_player_two(table_gamep2)
        barcosp2.append({"fila":coordenada1_jugador2,"col":coordenada2_jugador2})
    raw_input("Enter para continuar...")
    return barcosp2

def show_tables(coordenada1_jugador2,coordenada2_jugador1):
    table_gamep2[coordenada1_jugador2][coordenada2_jugador2] = "-"
    board_game_player_two(table_gamep2)




def attack_player_one(battle_1):
    clear()
    board_game_player_two(table_gamep1)
    board_game_player_two(attack_table_gamep2)
    attack1_p1 = raw_input("Player 1 ingresa la fila que quieres atacar!: ")
    attack2_p1 = raw_input("Player 1 ingresa la columna que quieres atacar!: ")
    a1 = answer_player1(attack1_p1,attack2_p1,battle_1)
    return a1

def answer_player1(guess_row,guess_column,battle_1):
    guess_column = int(guess_column)
    guess_row = int(guess_row)
#El for verificara si acerto, si no acerto,se pasa al if.
    for co in battle_1:#se imprime cada barco en battle_1
        if guess_row == co["fila"] and guess_column == co["col"]:
            print "Great!!" + "\n" + "Congratulations! You sunk my battleship, and you sunk it hard.!"
            table_gamep2[guess_row][guess_column] = "x"
            attack_table_gamep2[guess_row][guess_column] = "x"
            #board_game_player_one(table_gamep1)
            board_game_player_two(table_gamep1)
            board_game_player_two(attack_table_gamep2)
            raw_input("Enter para continuar...")
            return 1 
    if (guess_row < 0 or guess_row >= 11) or (guess_column < 0 or guess_column >= 11):
        print "That is not in the ocean!!"
#            print " "
        #board_game_player_one(table_gamep1)
        board_game_player_two(table_gamep1)
        board_game_player_two(attack_table_gamep2)


    elif table_gamep2[guess_row][guess_column] == "x":
        print "You said that!"
        #board_game_player_one(table_gamep1)
        board_game_player_two(table_gamep1)
        board_game_player_two(attack_table_gamep2)
    else:
        print "You didn't sunk my battleship!!!. juju"
        print " "
        table_gamep2[guess_row][guess_column] = "x"
        attack_table_gamep2[guess_row][guess_column] = "x"
        board_game_player_two(table_gamep1)
        board_game_player_two(attack_table_gamep2)


def attacK_player_two(battle_2):
    clear()
    board_game_player_one(table_gamep2)
    board_game_player_two(attack_table_gamep1)
    attack1_p2 = raw_input("Player 2 Ingresa la fila que quieres atacar!: ")
    attack2_p2 = raw_input("Player 2 Ingresa la columna que quieres atacar!: ")
    a2 = answer_player2(attack1_p2,attack2_p2,battle_2)
def answer_player2(guess_rowp2,guess_columnp2,battle_2):
    guess_columnp2 = int(guess_columnp2)
    guess_rowp2 = int(guess_rowp2)
    for co2 in battle_2:
        if guess_rowp2 == co2["fila"] and guess_columnp2 == co2["col"]:
            print "Great!!" + "\n" + "Congratulations! You sunk my battleship, and you sunk it hard.!"
            table_gamep1[guess_rowp2][guess_columnp2] = "x"
            attack_table_gamep1[guess_rowp2][guess_columnp2] = "x"
            board_game_player_one(table_gamep2)
            board_game_player_two(attack_table_gamep1)
            raw_input("Enter para continuar...")

            return 1
    if (guess_rowp2 < 0 or guess_rowp2 >= 11) or (guess_columnp2 < 0 or guess_columnp2 >= 11):
        print "That is not in the ocean!!"
#            print " "
        board_game_player_one(table_gamep2)
        board_game_player_one(attack_table_gamep1)

    elif table_gamep1[guess_rowp2][guess_columnp2] == "x":
        print "You said that!"
        board_game_player_one(table_gamep2)
        board_game_player_one(attack_table_gamep1)
    else:
        print "You didn't sunk my battleship!!!. juju"
        print " "
        table_gamep1[guess_rowp2][guess_columnp2] = "x"
        attack_table_gamep2[guess_rowp2][guess_columnp2] = "x"
        board_game_player_one(table_gamep2)
        board_game_player_one(attack_table_gamep2)






def instructions_game():
    print ""
    print "You can only insert numbers for 0 to 9 "
    print ""


def player_vs_bot():
    #clear_list()
    print "Single player"
    ask_user()

def print_menu():
#    clear()
#    clear_list()
    print ""
    print "===================================================="
    print "==              Welcome to Battle Ship            =="
    print "===================================================="
    print " "
    print "                  1.One player."
    print "                  2.Multiplayer."
    print "                  3.Instrucctions."
    print "                  4.Exit."


def menu():
    answerusermenu = True
    while answerusermenu == True:
        answer_usermenu = raw_input("Insert your option >>:  ")
        print " "
        if answer_usermenu == "1" or answer_usermenu == "One player":
            print "ONE PLAYER..!! XD"
            player_vs_bot()
        elif answer_usermenu == "2" or answer_usermenu == "Multiplayer":
            player_Multi()
            print "Sharks surrounded us! Insert other option or Please try later"
            answerusermenu = True
        elif answer_usermenu == "3" or answer_usermenu == "Instructions":
            instructions_game()
        elif answer_usermenu == "4" or answer_usermenu == "Exit":
            print "See you later, bye bye!!"
            sys.exit()
        else:
            clear()
            print ""
            print "     Insert the number or name to option."
            print_menu()

def user_menu():
    print_menu()
    menu()

user_menu()