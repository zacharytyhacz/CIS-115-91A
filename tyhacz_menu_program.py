bDone = 0 # if user is done buying
bDrink = 0
bFries = 0
quantity = 0
total_cost = 0.0

user_choice = 0
user_decision = ""
menu =['',"McDoubleWubble","McChikenThang","McSuperBurger","McSpicyHam","McFillySteak","McFourOunce","McNuggetBoxe","McChikenBiscuit","McSpecial"]

drink_cost = 1.25
item_cost = 0.0
order = [0,0,0,0] # [item number, quantity, bFries, bDrink]


print "#### Welcome to McPython, how may I help you? ####"
print " Press the corresponding number to what you want to get..... "

while bDone == 0:   ## until user says theyre done, itll return back to menu
    for x in range(1,10):
        print x,".",menu[x], "         $",(x*0.25+1.07) ## number each item in the menu with its cost
        x = x + 1

    user_choice = input("")
    item_cost = user_choice * 0.25 + 1.07 ## save item cost to total up on bil

    print "How many",menu[user_choice],"'s","would you like?"
    quantity = input("")
    total_cost = total_cost + (item_cost*quantity) # the more the merrier

    print"Each item gets a side of fries, do you want fries? yes or no"
    user_decision = raw_input("")
    if(user_decision == "yes"):
        bFries = 1 # saved to keep record if there is second order
        total_cost = total_cost + 1.00
    
    print "Alright",quantity,menu[user_choice],"'s. Would you like a drink with that? yes or no"
    user_decision = raw_input("")
    if(user_decision == "yes"):
        total_cost = total_cost + drink_cost
        bDrink = 1 # saved to keep record if there is second order
   
    print "Ok, will that be all?"
    user_decision = raw_input("")
    if(user_decision == "yes"):
        bDone = 1
    elif(user_decision == "no"):
        if(order[0] == 0): ## checks if second order's first number is 0, this means there isnt a second order so its ok to store info there
            ##SAVe
            order[0] = user_choice ## stored in this array because all these variables will be overwritten next go round
            order[1] = quantity
            order[2] = bFries
            order[3] = bDrink
        else:
            print" You're done ordering, you're gonna get way too fat" ## 
            bDone = 1
print "Ok my dude here is your bill..."
print "___________________________________"
for z in range(0,order[1]):
    print menu[order[0]],"  $",(order[0]*0.25 + 1.07)
if(order[2] == 1):
    print "Fries","   $1.00"
if(order[3] == 1):
    print "Large Bepsi","  $",drink_cost

for y in range(0,quantity):
    print menu[user_choice],"  $",item_cost


if(bFries == 1):
        print "Fries","   $1.00"
    
if(bDrink == 1):
    print "Large Bepsi","  $",drink_cost
    print "___________________________________"
    if(total_cost > 20.0):
        total_cost = total_cost - (total_cost*0.1)
        print "10% OFF DISCOUNT"
    print "      Total:  $",total_cost
