mpg = 0.0
gallons = 0
miles = 0
gasprice = 2.50
gloc = id(gasprice)

miles = input("Please Enter miles driven: ")

gallons = input("Please now enter the # of gallons used: ")
if gloc == id(gasprice):
    gallonsUsed = gallons*gasprice
else:
    print " Gas price changed, cost of trip inaccurate."
mpg = (miles / gallons)

print " Your MPG for this trip was: ", mpg
print " The cost of your trip was $",gallonsUsed
