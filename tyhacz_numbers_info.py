# python test 1 problem 3 - zachary tyhacz

average = 0.0
added = 0.0
multiplied = 1.0
numbersIn_str = [0.0, 0.0, 0.0, 0.0]
bDone = 0
while bDone == 0:    
    number_str = raw_input("Enter four digits:  ")

    numbersIn_str = number_str.split(" ") # take out white space, split up the digits by the spaces

    #print numbersIn_str
    if len(numbersIn_str) == 1: # user is entering one digit at a tim
        for x in range(1, 4):
            number_str = raw_input("Enter next number: ")
            numbersIn_str.insert(x,number_str)
            bDone = 1 # we got our 4 numbers
    elif len(numbersIn_str) == 4 : #### user entered all their digits
        bDone = 1        
    else:
        print " You did not enter four digits"
#print numbersIn_str[1]
for i in range(0, 3):
    added = added + float(numbersIn_str[i])
    multiplied = multiplied * float(numbersIn_str[i])
    
print "The sum of all the digits: ", added
print "The average of the digits: ", added/4
print "The product of all the digits: ", multiplied
