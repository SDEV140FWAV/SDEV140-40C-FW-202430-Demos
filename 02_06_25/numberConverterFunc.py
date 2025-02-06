"""Author: Angela Venable
    Number converter program
"""

import random

hexDigits = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100", 
             "5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
             "A":"1010","B":"1011","C":"1100","D":"1101",
             "E":"1110","F":"1111"}
#hexDigits.pop("F")
x = 5
x + 4
""" def f():
    hexDigits["a"] = "1010"
f() # Does the top-level x change?
print(hexDigits) # No, this displays 5 """
def main():
    
    #choice = get_menu_choice()
    #process_choice(choice)
    length = random.randint(1,64)
    binaryNumberStr = ""
    for i in range(length):
        digit = random.randint(0,1)
        binaryNumberStr += str(digit)
    #decimalNum = binaryToDecimal(binaryNumberStr)
    #print(f"{binaryNumberStr} is {decimalNum} in decimal")
    hexNum = binaryToHex(binaryNumberStr)
    print(f"{binaryNumberStr} is {hexNum} in hexadecimal")


def binaryToDecimal(binaryNum:str):
    """Converts a binary number given as a string to a decimal number stored as an int"""
    decimalNum = 0
    if validateBinaryNumber(binaryNum):
        for exponent in range(0, len(binaryNum)):
            decimalNum += int(binaryNum[-1 - exponent]) * 2**exponent
        #print(decimalNum)
    else:
        print("There are non-binary digits in the string.")
    return decimalNum


def validateBinaryNumber(binaryNum:str):
    """Validates a string is a binary number consisting of all 1s and 0s"""
    for digit in binaryNum:
        if digit != '0' and digit != '1':
            return False
    return True
def binaryToHex(binaryNum:str):
    """  """
    binaryDigits = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', 
                    '0100': '4', '0101': '5', '0110': '6', '0111': '7', 
                    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', 
                    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

    segements = []
    hexNum = ""
    if validateBinaryNumber(binaryNum):
        for i in range(4 - len(binaryNum)%4):
            binaryNum = "0" + binaryNum
        for group in range(0, len(binaryNum), 4):
            segements.append(binaryNum[group:group+4])
        for seg in segements:
            hexNum += binaryDigits[seg]
    return hexNum


def get_menu_choice():
    choice = input(menu())
    
    if choice.isnumeric():
        choice = int(choice)
        if choice >= 1 and choice <=2:
            return choice
    else:
        print("Error: the data entered is not a positive number")
    print("The choice is invalid please choose again.")
    return get_menu_choice()


def menu():
   
    return "Please Choose a Conversion:\n1. Convert Binary to Hexadecimal\n2. Convert Binary to Decimal\n"


def process_choice(choice):
    binaryToHex("101")
    



if __name__ == "__main__": #if the file is being run directly instead of imported
    main()

