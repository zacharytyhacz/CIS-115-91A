



password = "1999"
pass_key = raw_input("Enter the code: ")
try:
    test_it = int(pass_key)
    print" Smart guy, you know it's all digits!"
    if pass_key == password:
        print" You shall pass "
    else:
        print" Incorrect code. "
except:
    print" Ha! Incorrect code. The code is made of digits you fool!"
        

