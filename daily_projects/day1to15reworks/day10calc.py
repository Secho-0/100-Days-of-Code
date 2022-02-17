from os import system
from math import floor
import art

def add(a,b):
    sum = a + b
    return sum

def sub(a,b):
    dif = a - b
    return dif

def mult(a,b):
    prod = a * b
    return prod

def div(a,b,type):

    #decimal (float) division
    if type.lower().startswith('d'):
        quo = a / b
        return quo
    
    #remainder division, returns integers of both 
    if type.lower().startswith('r'):
        quo = floor(a / b)
        rem = a % b
        retquo = f"{quo} R{rem}"
        return retquo

def printMenu(menu):
    for i, op in enumerate(menu):
        if i < (len(menu) -1):
            print(op, end = ' | ')
        else: 
            print(op)  

def checkInput(userInput,userop):
    if userInput.startswith('y') or userInput.startswith('n'):
        return True
    if userop == "/" and (userInput.startswith('d') or userInput.startswith('r')):
        return True
    else:
        return False


opnum = 1
newcalc = 'y'

menu = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}
print(art.CALCULATOR)

while newcalc.startswith('y'):

    # Gather the two numbers the user would like to operate on if first operation in a series
    if opnum == 1:
        firstNum = int(input("What is your first number? "))
        secondNum = int(input("What is your second number? "))

    # if continuation, print first result and ask for second number 
    if opnum > 1:
        print("Your result from the last operation is: ", firstNum)
        secondNum = int(input("What is your second number? "))

    print("")
    printMenu(menu)      

    # Ask for menu choice 
    user_op = input(" What operation would you like to preform from the list above?\n> ")
    calc = menu[user_op]

    # If division is chosen, what kind? Remainder or Decimal - Otherwise execute chosen function 
    if user_op == "/":
        type = input("What type of division would you like to do? (D)ecimal or (R)emainder\n> ").lower()
        if not checkInput(type,user_op):
            print("Invalid input")
            type = input("What type of division would you like to do? (D)ecimal or (R)emainder\n> ").lower()
        else:
            answer = calc(firstNum,secondNum,type)
    else:
        answer = calc(firstNum,secondNum)

    #print the answer 
    print(f"""   The result of your caclulation is:
    \t{firstNum} {user_op} {secondNum} = {answer}\n""")

    # Ask if they want to continue with the result
    contmaths = input("Would you like to continue using the previous result (no remainder div)? Y or N \n> ").lower()
    if not checkInput(contmaths,user_op):
        print("Invalid choice")
        contmaths = input("Would you like to continue using the previous result (no remainder div)? Y or N \n> ").lower()
    elif contmaths.startswith('y'):
        firstNum = answer
        opnum +=1
        continue
    elif contmaths.startswith('n'):
        # Ask for next operation 
        newcalc = input("Would you like to preform new operations? Y or N\n> ").lower()
        if not checkInput(newcalc,user_op):
            print("Invalid choice")
            newcalc = input("Would you like to preform new operations? Y or N\n> ").lower()
        elif newcalc.startswith('y'):
            # Ask if they want to clear the screen 
            clr_screen = input("Would you like to clear the screen?> ").lower()
            if not checkInput(clr_screen,user_op):
                clr_screen = input("Would you like to clear the screen?> ").lower()
            elif clr_screen.startswith('y'):
                opnum = 1
                system("cls")
                continue
            elif clr_screen.startswith('n'):
                continue       
        elif newcalc.startswith('n'):
            break

print("Hope we could help!")

