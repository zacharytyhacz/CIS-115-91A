#zachary tyhacz encryption program
import string
in_string = ""
en_string = ""
or_string = ""
in_choice = 0

def Encrypt(to_en_string):
	global en_string
	en_string = ""
	en_char = 0.0
	i = 0
	
	en_string += to_en_string[0]
	
	# en_string = first_letter + the NUMBER ord of first letter * pi + SPACE + the character of (the letter ORD number + 1) +.... + last letter 
	while i < len(to_en_string):
		en_char = ord(to_en_string[i])
		en_char = en_char*3
		
		en_string += str( en_char )+" "
		en_string += chr( ord(to_en_string[i]) + 1) 
		
		i += 1
		
	en_string += to_en_string[i-1]
	print
	print en_string
	print
	ShowMenu()

# original string =
# first letter 
# space[1] until the next 
# t364.414 u317.2915 f361.2725 t364.414 ut
def Decipher(dec_string):
	global or_string
	
	or_string = "" # reset the translated string
	h = 0
	temp_list = []
	dec_string.strip(dec_string[0]) 
	temp_list = dec_string.split() # remove white space

	while h < len(temp_list)-1: # not last
		s = temp_list[h] # save the string item in the TEMP_LIST
		temp_list[h] = temp_list[h].lstrip(s[0]) #remove first letter, we can use the number to get it
		temp_int = int(float(temp_list[h]) / 3 ) # turn the string into a float, divide by pi, turn to int 
		#temp_int += 1 # division is dodgey, need to add one for correct chr() 
		#print chr(temp_int)
		or_string += chr(temp_int) 
		h += 1
	else:
		print "Secret Code Deciphered: ", or_string
		ShowMenu()
	
def ShowMenu():
	try:
		print "1 - Encrypt a code"
		print "2 - Un-Encrypt a code"
		in_choice = input("Selection: ")
		if(in_choice != 1 and in_choice != 2):
			print"Invalid Selection!\n"
			ShowMenu()
		elif in_choice == 1:
			in_string = raw_input("Enter the string you want to encrypt: ")
			Encrypt(in_string)
		else:
			in_string = raw_input("Enter the string you want to decipher: ")
			Decipher(in_string)
	except:
		print
		ShowMenu()

ShowMenu()	
