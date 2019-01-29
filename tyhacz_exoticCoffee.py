ascii_art = [ "                                        ",
              "         #############      (           ",
              "        #############       (  )        ",
              "       ####                )    (       ",
              "      ####              **********_     ",
              "     ##########         ********** |    ",
              "    ##########          **********_|    ",
              "   ####                 **********      ",
              "  ####                  **********      ",
              " #########                              ",
              "######### XOTIC COFFEE                  ",
              "________________________________________"
            ]

menu_items = [ "",
               "Black Ivory Coffee",
               "Monkey Brew",
               "House Blend",
               "Danish",
               "Tasty Balut"
               ]
menu_prices = [ "",
                "5.00",
                "2.50",
                "1.50",
                "2.00",
                "3.75"
                ]
x = 0
bDoneOrdering = 0

user_in = ""
user_total = 0.0


for x in range(0,len(ascii_art)):
    print ascii_art[x]
    x += 1

def show_menu(): # print item number, item price, then name of the item
    global menu_items,menu_prices
    print
    for y in range(1,6):
        print y,"-",("$"+menu_prices[y]),menu_items[y]
        y += 1
        
def CheckInput(in_str): # checks if bDoneOrdering
    global bDoneOrdering
    for char in in_str:
        if(char == "y" or char == "Y"):
            continue
        if(char == "n" or char == "N"):
            bDoneOrdering = 1
        else:
            CheckInput(raw_input("   Would you like to make another purchase? y or n   "))
        

def buy_item(z): # show item and price, add to total, ask if another purchase
    global menu_items,menu_prices,user_total,user_in
    print "   You bought a", menu_items[z],"for","$"+menu_prices[z]
    user_total += float(menu_prices[z])
    print "   Your total is now ","$"+str(user_total)+"0"
    user_in = raw_input("   Would you like to make another purchase? y or n   ")
    CheckInput(user_in)

    
while bDoneOrdering == 0:
    show_menu()
    user_in = raw_input("Please make a selection: ")
    if(int(user_in) > 0 and int(user_in) < 6): # only items on menu
        buy_item(int(user_in))
    else:
        print "Invalid selection, please select again"
## when here, ordering is done
if(user_total > 10.0):
    user_total -= (user_total / 10) # take off a 10th
    print "10% OFF DISCOUNT!"
user_total += (user_total / 7)
print "Your total is ","$"+str(user_total)+"0"

