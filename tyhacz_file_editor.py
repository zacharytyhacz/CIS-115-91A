from datetime import date
import pickle
import string

options = ["","Create New","Edit Existing","Read Existing","Pickle","Unpickle","Exit"]
user_in = ""
bDone = 0


print " ########  ####  ##        ########  ########   ####  ########   #######   ########   "
print " ##         ##   ##        ##        ##     ##   ##      ##     ##     ##  ##     ##  "
print " ##         ##   ##        ##        ##     ##   ##      ##     ##     ##  ##     ##  "
print " ######     ##   ##        ######    ##     ##   ##      ##     ##     ##  ########   "
print " ##         ##   ##        ##        ##     ##   ##      ##     ##     ##  ##   ##    "
print " ##         ##   ##        ##        ##     ##   ##      ##     ##     ##  ##    ##   "
print " ##        ####  ########  ########  ########   ####     ##      #######   ##     ##  "
print


def SearchForFile(Name):
    global user_in
    record_file = open("records.txt","r")
    for line in record_file.readlines():
        if( string.find(line, Name) != -1):
            user_in = raw_input("Overwriting file....Continue? y or n: ")
            if( user_in == "n" or user_in == "N"):
                print "Returning...."
                break

def AddFileName(Name):
    record_file = open("records.txt","a")
    record_field = "\n " +Name + "   -   " + str(date.today()) 
    record_file.write(record_field)
    record_file.close()

def ReadExist():
    global user_in
    
    record_file = open("records.txt","r")
    for line in record_file.readlines():
        print line
    record_file.close()
    
    user_in = raw_input("Enter a file to open: ")
    
    if( string.find(user_in, ".txt") != -1 ):
        reading_file = open(user_in,"r")    
    else:
        reading_file = open(user_in+".txt","r")

    for line in reading_file.readlines():
        print line
    print " *** END OF FILE *** "
    
    reading_file.close()

def PickleExist():
    record_file = open("records.txt","r")
    new_pickled_file = ""
    new_pickle_name = ""
    for line in record_file.readlines():
        print line
    record_file.close()
    
    user_in = raw_input("Enter a file to pickle: ")
    
    if( string.find(user_in, ".txt") != -1 ):
        ToPickle_file = open(user_in,"r")
        new_pickle_name = "p_" + user_in
        new_pickled_file = open(new_pickle_name,"w")
        
    else:
        ToPickle_file = open(user_in + ".txt","r")
        new_pickle_name = "p_" + user_in +".txt"
        new_pickled_file = open(new_pickle_name,"w")
        
    for line in ToPickle_file.readlines():
        pickle.dump(line,new_pickled_file)

    AddFileName(new_pickle_name)
    ToPickle_file.close()
    new_pickled_file.close()
def CreateFile():
    global user_in
    
    file_name = ""
    file_name = raw_input("Enter the name of the file you want to create: ")
    file_name = file_name+".txt"
    
    #SearchForFile(file_name)
    AddFileName(file_name)
    
    new_file = open(file_name,"w")
    print "Type to the new file and type QUIT to stop."
    while user_in != "QUIT":
        user_in = raw_input("")
        if(user_in != "QUIT"):
            new_file.write(user_in+"\n")
    
    new_file.close()
    print " ok haha"
    
def CheckInput(i):   
    if( i == 1 ):
        CreateFile()
    elif( i == 2):
        EditExist()
    elif( i == 3):
        ReadExist()
    elif( i == 4):
        PickleExist()
    elif( i == 5):
        UnPickleExist()
    else:
        bDone = 1
    
def Start():
    global options,user_in
    x = 1
    while x < len(options): 
        print x,"-",options[x]
        x += 1
    user_in = raw_input("Enter a selection: ")
    if( int(user_in) > 0 and int(user_in) < 7):
        CheckInput(int(user_in))
    else:
        print " Invalid Selection! "
        Start()

while bDone == 0:
    Start()
print "See ya!"
