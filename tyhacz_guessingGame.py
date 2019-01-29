import random

the_number = 0
bWon = 1
player_number = ""
player_choice = 0
player_guesses = 0
custom_min = 0
custom_max = 0

def Title():
    print "==============================================================================================================================="
    print "  _______  __    __   _______     _______.     _______. __  .__   __.   _______      _______      ___      .___  ___.  _______ "
    print " /  _____||  |  |  | |   ____|   /       |    /       ||  | |  \ |  |  /  _____|    /  _____|    /   \     |   \/   | |   ____|"
    print "|  |  __  |  |  |  | |  |__     |   (----`   |   (----`|  | |   \|  | |  |  __     |  |  __     /  ^  \    |  \  /  | |  |__   "
    print "|  | |_ | |  |  |  | |   __|     \   \        \   \    |  | |  . `  | |  | |_ |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|  "
    print "|  |__| | |  `--'  | |  |____.----)   |   .----)   |   |  | |  |\   | |  |__| |    |  |__| |  /  _____  \  |  |  |  | |  |____ "
    print " \______|  \______/  |_______|_______/    |_______/    |__| |__| \__|  \______|     \______| /__/     \__\ |__|  |__| |_______|"
    print "==============================================================================================================================="

def YouWin():
    print "###########################################################################"
    print "____    ____  ______    __    __     ____    __    ____  __  .__   __.  __ "
    print "\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | |  |"
    print " \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | |  |"
    print "  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | |  |"
    print "    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | |__|"
    print "    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| (__)"
    print
    if(player_guesses == 1):
        print "YOU WON WITH",player_guesses,"GUESS!!!"
    else:
        print "YOU WON WITH",player_guesses,"GUESSES!!!"
    print "###########################################################################"
    Start()

def CheckGuess(num):
    global player_guesses
    player_guesses = player_guesses + 1
    if num == the_number:
        bWon = 0
        YouWin()
    else:
        print "Wrong...try again"
        
def Playing():
    while bWon == 1:
        player_number = raw_input("Guess: ")
        #print type(player_number)
        CheckGuess(int(player_number))

def Easy():
    global the_number
    the_number = random.randrange(1,10)
    print "Guess the number between 1 and 10!"
    Playing()
    
def Inter():
    global the_number
    the_number = random.randrange(1,75)
    print "Guess the number between 1 and 75!"
    Playing()
    
def Expert():
    global the_number
    the_number = random.randrange(1,200)
    print "Guess the number between 1 and 200!"
    Playing()
    
def Custom():
    global the_number, custom_min, custom_max
    custom_min = input("Enter the minimum number for your guessing range: ")
    custom_max = input("Enter the maximum number for your guessing range: ")
    the_number = random.randrange(custom_min, custom_max)
    print "Guess the number between",custom_min,"and",custom_max,"!"
    Playing()
    
def Start():
    print "-===== CHOOSE MODE =====-"
    print "1. Easy Mode"
    print "2. Intermediate Mode "
    print "3. Expert Mode"
    print "4. Custom "
    player_guesses = 0
    bWon = 1
    player_choice = input("")
    if player_choice == 1:
        Easy()
    elif player_choice == 2:
        Inter()
    elif player_choice == 3:
        Expert()
    elif player_choice == 4:
        Custom()
    else:
        Start()

Title()
Start()
