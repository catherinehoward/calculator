num1=int(input("Please enter a number "))
num2=int(input("And another "))
print("Choose from the following options:")
print("Enter 'a' to add the numbers")
print("'b' to subtract the first number from the second")
print("'c' to divide the first number by the second")
print("'d' to multiply them")
chosen = 'false'
while chosen == 'false':
    myOperator=input()
    if myOperator =="a":
        answer = num1+num2
        print("The answer is " + str(answer))
        chosen = 'true'
    elif myOperator =="b":
        answer = num2-num1
        print("The answer is " + str(answer))
        chosen = 'true'
    elif myOperator =="c":
        answer = num1/num2
        print("The answer is " + str(answer))
        chosen = 'true'
    elif myOperator =="d":
        answer = num1*num2
        print("The answer is " + str(answer))
        chosen = 'true'
    else:
        print("I don't recognise that option, try again")




