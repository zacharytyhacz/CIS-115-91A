# curly headed creations
print ".______     _______   ______ .___________.    ___      .__   __.   _______  __       _______ "
print "|   _  \   |   ____| /      ||           |   /   \     |  \ |  |  /  _____||  |     |   ____|"
print "|  |_)  |  |  |__   |  ,----'`---|  |----`  /  ^  \    |   \|  | |  |  __  |  |     |  |__   "
print "|      /   |   __|  |  |         |  |      /  /_\  \   |  . `  | |  | |_ | |  |     |   __|  "
print "|  |\  \-. |  |____ |  `----.    |  |     /  _____  \  |  |\   | |  |__| | |  `----.|  |____ "
print "| _| `.__| |_______| \______|    |__|    /__/     \__\ |__| \__|  \______| |_______||_______|"
print
print "                .___  ___.      ___       __  ___  _______ .______     ########               "
print "                |   \/   |     /   \     |  |/  / |   ____||   _  \          ##               "
print "                |  \  /  |    /  ^  \    |  '  /  |  |__   |  |_)  |     ######               "
print "                |  |\/|  |   /  /_\  \   |    <   |   __|  |      /      ##                   "
print "                |  |  |  |  /  _____  \  |  .  \  |  |____ |  |\  \-.    ##                   "
print "                |__|  |__| /__/     \__\ |__|\__\ |_______|| _| `.__|    #######              "

bDone = 1
while bDone == 1:
	try:
		height = input("Enter height: ")
		width = input("Enter width: ")

		print
		row = 1
		column = 1
		while row <= height:
			while column <= width:
				if(row == 1 or row == height): # top and bottom
					while column <= width:
						print "#",
						column += 1

				elif(row > 1):
					if(column == 1 or column == width):
						print "#",
						column += 1

					else:
						if((column ==(width/2)) and ((row == (height/2)))):
							print "ZAC",
							column += 1
						else:
							print " ",
						column += 1
			row += 1
			print
			column = 1
	except:
		print "Value is not acceptable!"