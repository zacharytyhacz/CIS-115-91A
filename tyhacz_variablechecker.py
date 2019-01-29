import random

x = 0

def CheckAnswer(answer):
    if (x == 0 ) and isinstance(answer, str):
        print "Awesome job!",answer,"is a string! Any data type can become a string!"
    elif (x == 1) and isinstance(answer, int):
        print "Awesome job!",answer,"is an integer! Any whole number is an integer!"
    elif (x == 2) and isinstance(answer, float):
        print "Awesome job!",answer,"is a float point integer! Any decimal is a float!"
    else:
        print "Sorry, incorrect data type! :("

while x >= 0:
    x = random.randint(0,3)
    if( x == 0):
        answer = raw_input("Enter a string: ")
        CheckAnswer(answer)
    elif( x == 1):
        answer = input("Enter an integer: ")
        CheckAnswer(answer)
    else:
        answer = input("Enter a float: ")
        CheckAnswer(float(answer))
