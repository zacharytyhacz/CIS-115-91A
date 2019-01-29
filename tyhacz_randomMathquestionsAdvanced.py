from random import randint ## random integer class

num1 = 0
num2 = 0
answer = 0

irand = 0

operations = ["+","-","*"]
op_str = ["sum","difference","product"]
question_str = ""

while answer < 100:
	num1 = randint(1, 10)
	num2 = randint(1, 10)
	
	print "Select an operation..."
	print "1. Addition"
	print "2. Substraction"
	print "3. Multiplication"
	
	irand = input("\n")
	irand -= 1
	
	if( irand == 0):
		question_str = "What is the " + op_str[irand] + " of " + str(num1) + operations[irand] + str(num2) + "?"
		answer = num1+num2
		print question_str
	elif( irand == 1):
		question_str = "What is the " + op_str[irand] + " of " + str(num1) + operations[irand] + str(num2) + "?"
		answer = num1-num2
		print question_str
	elif( irand == 2):
		question_str = "What is the " + op_str[irand] + " of " + str(num1) + operations[irand] + str(num2) + "?"
		answer = num1*num2
		print question_str
		
	user_in = input("Answer: ")
	
	if(user_in == answer):
		print "That is correct!"
	else:
		print "Wrong..."
		print question_str
		user_in = input("Answer: ")
		if(user_in == answer):
			print "That is correct!"
		else:
			print "Wrong, the answer is",answer
	print

