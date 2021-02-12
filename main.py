import re

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




throws_and_dices()