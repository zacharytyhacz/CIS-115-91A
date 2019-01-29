grades = [0,0,0,0,0,0,0,0,0,0]
x = 0
average = 0


def CalcAverage():
    global average
    average = average / len(grades)
    print "The average grade is",average

def GetGrade(g):
    global grades,average
    print g
    grades[g] = input("Enter a grade: ")
    if(grades[g] <= 100 and grades[g] >= 0):
        average += grades[g]
    else:
        print "Invalid grade,please reenter a grade."
        GetGrade(g)
    
while x < len(grades):
    print x
    GetGrade(x)
    x += 1
        
CalcAverage()
