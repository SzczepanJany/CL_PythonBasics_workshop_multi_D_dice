import re
from random import randint

def throws_and_dices():
    '''
    Function is asking user for a throw and checking if it's valid one
    '''
    while True:
        type_of_throw = input("Enter type of throw: ")
        x = re.compile("[0-9]*(D10(0)?|D3|D4|D6|D8|D12|D20)([+-][1-9]*)?")
        if x.fullmatch(type_of_throw):
            break
        else:
            print("Enter correct form!")
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
    '''
    Function is computing the score
    '''
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
    elif operations == '+':
        result = result + int(operants[2])

    return result


operant, operation = throws_and_dices()
print(do_the_math(operant, operation))
