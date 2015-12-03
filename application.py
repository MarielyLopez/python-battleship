#coding:utf-8
import random
import sys

table_game = []

for i in range(1,11):
    table_game.append(["0"]*10)

def board_game(table_game):
    for row in table_game:
        print " ".join(row)

def random_row(table_game):
    return random.randint(0, len(table_game)-1)

def random_column(table_game):
    return random.randint(0, len(table_game[0])-1)

battle_row = random_row(table_game)
battle_column = random_column(table_game)
#print battle_row
#print battle_column

def ask_user():
    def turnos():
        print "su turno es el ", turno
        board_game(table_game)
        guess_row = raw_input("Guess row: ")
        guess_column = raw_input("Guess column: ")
        if False == guess_row.isdigit():
            print "insert numbers"
        else:
            #print "is a nube
            answer_user(guess_row,guess_column)
    answeruserask = True
    while answeruserask == True:
        turno = 0
        for turno in range(1,5):
            
            if turno == 4:
               
                turnos()
                print "Termino el juego"
                answeruserask = False
            else:
                turnos()
 
    #print random_row(table_game)
    #print random_column(table_game)

def answer_user(guess_row,guess_column):
    guess_column = int(guess_column)
    guess_row = int(guess_row)
    if guess_row == battle_row and guess_column == battle_column:
        print "¡Felicitaciones! ¡Hundiste mi barco!"
        table_game[guess_column][guess_row] = "x"
        board_game(table_game)
    else:
        if (guess_row< 0 or guess_row >= 11) or (guess_column < 0 or guess_column  >= 11):
            print "Eso no esta en el oceano!!"
            board_game(table_game)

        elif table_game[guess_row][guess_column] == "x":
            print "Ya dijiste eso!"
        else:
            print "No impactaste mi barco! juju"
            table_game[guess_row][guess_column] = "x"
           # board_game(table_game)
#board_game(table_game)

#{[],[]} lista de lista



def print_menu():
    print"Welcome !! we play Battle Ship!"
    print "1.ONE PLAYER"
    print "2.EXIT"
    menu()

def menu():
    answer_usermenu = raw_input("Insert your option >> ")
    if answer_usermenu == "1" or answer_usermenu == "ONE PLAYER":
            ask_user()
    elif answer_usermenu == "2" or answer_usermenu == "EXIT":
        sys.exit()
    else:
        print "Insert a number to option"

print_menu()