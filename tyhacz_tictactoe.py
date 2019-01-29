import random


bPlayerTurn = 0 # player goes first

top_row = ["1","2","3"]
mid_row = ["4","5","6"]
bott_row = ["7","8","9"]

def YouWin(who):
	global top_row,mid_row,bott_row,bPlayerTurn
	if(who == 0):
		print "__  __ ____   __  __   _       __ ____ _   __  __"
		print "\ \/ // __ \// / / /  | |     / //  _// | / / / /"
		print " \  // / / // / / /   | | /| / / / / /  |/ / / / "
		print " / // /_/ // /_/ /    | |/ |/ / / / / /|  / /_/  "
		print "/_/ \____/ \____/     |__/|__//___//_/ |_/ /_/   "
	else:
		print "Sorry, HAL won."
	
	# reset all values to start new game
	top_row = ["1","2","3"]
	mid_row = ["4","5","6"]
	bott_row = ["7","8","9"]
	bPlayerTurn = 0	
	PrintBoard()
	
def CheckWin():
	i = 0
	# straight across
	if(top_row[0] == top_row[1]) and (top_row[0] == top_row[2]):
		if(top_row[0] == "X"):
			YouWin(0)
		else:
			YouWin(1)
	elif(mid_row[0] == mid_row[1]) and (mid_row[0] == mid_row[2]):
		if(mid_row[0] == "X"):
			YouWin(0)
		else:
			YouWin(1)
	elif(bott_row[0] == bott_row[1]) and (bott_row[0] == bott_row[2]):
		if(bott_row[0] == "X"):
			YouWin(0)
		else:
			YouWin(1)
	# diagnols
	elif(top_row[0] == mid_row[1]) and (bott_row[2] == top_row[0]):
		if(top_row[0] == "X"):
			YouWin(0)
		else:
			YouWin(1)		
	elif(top_row[2] == mid_row[1]) and (bott_row[0] == top_row[2]):
		if(bott_row[0] == "X"):
			YouWin(0)
		else:
			YouWin(1)
	# columns		
	elif(top_row[0] == mid_row[0]) and (bott_row[0] == top_row[0]):
		if(top_row[0] == "X"):
			YouWin(0)
		else:
			YouWin(1)		
	elif(top_row[1] == mid_row[1]) and (bott_row[1] == top_row[1]):
		if(top_row[1] == "X"):
			YouWin(0)
		else:
			YouWin(1)			
	elif(top_row[2] == mid_row[2]) and (bott_row[2] == top_row[2]):
		if(top_row[2] == "X"):
			YouWin(0)
		else:
			YouWin(1)
def Turn():
	global bPlayerTurn, top_row, bott_row, mid_row
	if (bPlayerTurn == 0):
		try:
			num = int(raw_input("Select a number to place an X: "))
			if(num < 4):
				num -= 1 # because top_row array starts at 0, so 1 would be 0.
				if(top_row[num] != "X") and (top_row[num] != "O"):
					top_row[num] = "X"
					#end turn
					bPlayerTurn = 1
					PrintBoard()
					#CheckWin()
				else:
					print "Position already taken, please select another."
					Turn()
			if(num >= 4) and (num < 7):
				num -= 4 #offset
				if(mid_row[num] != "X") and (mid_row[num] != "O"):
					mid_row[num] = "X"
					#end turn
					bPlayerTurn = 1
					PrintBoard()
					#CheckWin()
				else:
					print "Position already taken, please select another."
					Turn()
			else:
				num -= 7 #offset
				if(bott_row[num] != "X") and (bott_row[num] != "O"):
					bott_row[num] = "X"
					#end turn
					bPlayerTurn = 1
					PrintBoard()
					#CheckWin()
				else:
					print "Position already taken, please select another."
					Turn()
		except ValueError:
			print "Enter a valid integer."
			Turn()
	
	else: # bot!
		bot_choice = random.randint(1,9)
		if(bot_choice < 4):
			bot_choice -= 1 # because top_row array starts at 0, so 1 would be 0.
			if(top_row[bot_choice] != "X") and (top_row[bot_choice] != "O"):
				top_row[bot_choice] = "O"
				
				bPlayerTurn = 0	
				PrintBoard()	
				#CheckWin()
			else:
				Turn()
		elif(bot_choice >= 4) and (bot_choice < 7):
			bot_choice -= 4 #array offset
			if(mid_row[bot_choice] != "X") and (mid_row[bot_choice] != "O"):
				mid_row[bot_choice] = "O"	
				bPlayerTurn = 0	
				PrintBoard()	
				#CheckWin()
			else:
				Turn()
		else:
			bot_choice -= 7 #array offset
			if(bott_row[bot_choice] != "X") and (bott_row[bot_choice] != "O"):
				bott_row[bot_choice] = "O"	
				bPlayerTurn = 0	
				PrintBoard()	
				#CheckWin()
			else:
				Turn()
	
def PrintBoard():
	global top_row
	print
	print top_row[0],"|",top_row[1],"|",top_row[2]
	print "---------"
	print mid_row[0],"|",mid_row[1],"|",mid_row[2]	
	print "---------"
	print bott_row[0],"|",bott_row[1],"|",bott_row[2]
	print
	CheckWin()
	Turn()
	
PrintBoard()