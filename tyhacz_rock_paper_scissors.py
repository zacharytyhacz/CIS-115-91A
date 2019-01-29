import random

warriors = [ "","ROCK","PAPER","SCISSORS"]


player_in = ""
player_choice = 0

bot_choice = 0

bot_score = 0
player_score = 0
def Battle():
    global bot_choice,warriors,player_choice,bot_score,player_score
    
    bot_choice = random.randrange(1,3)
    print
    print "HAL has chosen",warriors[bot_choice]
    print "You have chosen",warriors[player_choice]
    if(bot_choice == player_choice):
        print " TIE!!! Draw again! "
    elif(bot_choice == 1):
        if(player_choice == 2):
            print "YOU WIN!"
            player_score += 1
            
        elif(player_choice == 3):
            print "YOU LOSE!"
            bot_score += 1
            
    elif(bot_choice == 2):
        if(player_choice == 3):
            print "YOU WIN!"
            player_score += 1
            
        elif(player_choice == 1):
            print "YOU LOSE!"
            bot_score += 1
            
    elif(bot_choice == 3):
        if(player_choice == 1):
            print "YOU WIN!"
            player_score += 1
            
        elif(player_choice == 0):
            print "YOU LOSE!"
            bot_score += 1
def CheckChoice(i):
    global player_in,player_choice
    if(i == 1):
        print
        print "Rock: Tough and Solid Earth Mass"
        print "Weaknesses: Thin Shadowing Paper"
        print "Ultimate Victims: Poor Sheets of Colliding Metal"
        print
        player_in = raw_input("Are you sure you want to choose ROCK? y or n:  ")
    elif(i == 2):
        print
        print "Paper: Warping and Kinesthetic Covering Tarp"
        print "Weaknesses: The Sharp and Violent Scissors and water"
        print "Ultimate Victims: Solid Grunts of Stone"
        print
        player_in = raw_input("Are you sure you want to choose PAPER? y or n:  ")
    elif(i == 3):
        print
        print "Scissors: Sleek Sharp Metal of Destruction"
        print "Weaknesses: The Collosal Earth Rock"
        print "Ultimate Victims: Puny and Weak Papyrus"
        print
        player_in = raw_input("Are you sure you want to choose SCISSORS? y or n:  ")
    for char in player_in:
        if(char == "y" or char == "Y"):
            player_choice = i
            Battle()
        elif(char == "n" or char == "N"):
            continue
            

while player_choice >= 0:
    print " Current Score :",player_score,"/",bot_score
    print " 1 -  ROCK"
    print " 2 - PAPER"
    print " 3 - SCISSORS"
    player_in = raw_input("Choose your fate!  ")
    CheckChoice(int(player_in))
