import re
from random import randint

def throws_and_dices():
    type_of_throw = input("Enter type of throw: ")
    result = re.split('[-|D|+]',type_of_throw)
    print(result)
    if "-" in type_of_throw:
        sign = "-"
    elif "+" in type_of_throw:
        sign = "+"
    else:
        sign = ""
    return (result,sign)

def do_the_math(operants, operations):
    throws = []
    if operants[0] == '':
        mulitple = 1
    else:
        mulitple = operants[0]

    for _ in range(int(mulitple)):
        throws.append(randint(1,int(operants[1])))
        print(throws)
    result = sum(throws)    
    if operations == '-':
        result = result - int(operants[2])
    elif operations == '-':
        result = result + int(operants[2])

    return result


operant, operation = throws_and_dices()
print(do_the_math(operant, operation))