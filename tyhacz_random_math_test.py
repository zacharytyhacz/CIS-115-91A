from random import randint ## random integer class

num1 = randint(0, 9) ## different numbers every run
num2 = randint(0, 9)
answer = 0
in_num = 0          # user input

correct_str = "You are correct, nice job!"
incorrect_str = " Incorrect "
chance_str = "One more shot...."

print " Select the type of operation you want to be tested on...."
print " 1. Addition "
print " 2. Subtraction "
print " 3. Multiplication "
print " 4. Division "
in_num = input("")
if in_num == 1:
    print "What is",num1,"+",num2,"?"
    answer = num1+num2
    in_num = input("Sum: ")
    if in_num == answer:
        print correct_str
    else:
        print incorrect_str
        print chance_str
        print"What is",num1,"+",num2,"?"
        in_num = input("Sum: ")
        if in_num == answer:
            print correct_str
        else:
            print incorrect_str
            print "The sum is ", answer
elif in_num == 2:
    print "What is",num1,"-",num2,"?"
    answer = num1-num2
    in_num = input("Difference: ")
    if in_num == answer:
        print correct_str
    else:
        print incorrect_str
        print chance_str
        print"What is",num1,"-",num2,"?"
        in_num = input("Difference: ")
        if in_num == answer:
            print correct_str
        else:
            print incorrect_str
            print "The difference is ", answer
elif in_num == 3:
    print "What is",num1,"*",num2,"?"
    answer = num1*num2
    in_num = input("Product: ")
    if in_num == answer:
        print correct_str
    else:
        print incorrect_str
        print chance_str
        print"What is",num1,"*",num2,"?"
        in_num = input("Product: ")
        if in_num == answer:
            print correct_str
        else:
            print incorrect_str
            print "The product is ", answer
elif in_num == 4:
    if num1 == 4:
        num1 = 10
        num2 = 2
    else:
        num1 = 9
        num2 = 3
    if num2 == 5:
        num1 = 8
        num2 = 2
    else:
        num1 = 6
        num2 = 2
    print "What is",num1,"/",num2,"?"
    answer = num1/num2
    in_num = input("Quotient: ")
    if in_num == answer:
        print correct_str
    else:
        print incorrect_str
        print chance_str
        print"What is",num1,"/",num2,"?"
        in_num = input("Quotient: ")
        if in_num == answer:
            print correct_str
        else:
            print incorrect_str
            print "The quotient is ", answer
                
