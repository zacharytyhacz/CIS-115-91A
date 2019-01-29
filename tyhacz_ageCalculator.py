from datetime import date

day = 0
year = 0
month = 0

now = date.today()

#print age.days

def CalcDays(y,m,d):
    global now, birthday
    birthday = date(y,m,d)
    age = now - birthday
    
    print "You are",age.days,"days old!"

def getDay():
    global day, month, year
    day = input("Enter the day of that month you were born: ")
    if (day == 29) and (month == 2):
        #print " LEAP !!!! "
        CalcDays(year,month,day)
    else:
        CalcDays(year,month,day)

def getMonth():
    global month
    print " Choose the month you were born..."
    print " 1 - Jan. "
    print " 2 - Feb. "
    print " 3 - March "
    print " 4 - April "
    print " 5 - May "
    print " 6 - June "
    print " 7 - July "
    print " 8 - August "
    print " 9 - Sept. "
    print " 10 - Oct. "
    print " 11 - Nov. "
    print " 12 - Dec. "
    month = input("")
    getDay()

def getYear():
    global year
    year = input("Enter the four digit year you were born:  ")
    getMonth()

getYear()
