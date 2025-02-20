"""Author: Angela Venable
    Number converter program
"""

import random

hexDigits = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100", 
             "5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
             "A":"1010","B":"1011","C":"1100","D":"1101",
             "E":"1110","F":"1111"}

def main():
    
    choice = get_menu_choice()
    process_choice(choice)
    """ length = random.randint(1,64)
    binaryNumberStr = ""
    for i in range(length):
        digit = random.randint(0,1)
        binaryNumberStr += str(digit) """
    #decimalNum = binaryToDecimal(binaryNumberStr)
    #print(f"{binaryNumberStr} is {decimalNum} in decimal")
    #hexNum = binaryToHex(binaryNumberStr)
    #print(f"{binaryNumberStr} is {hexNum} in hexadecimal")


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

def decimalToBinary(decimalNum:float):
    binaryNum = ""
    decimalNumStr = str(decimalNum)
    parts = decimalNumStr.split('.')
    decimalNum = int(parts[0])
    negative = False
    if decimalNum < 0:
        negative = True
        decimalNum *= -1
    
    while decimalNum > 0:
        binaryNum = str(decimalNum % 2) + binaryNum
        decimalNum = int(decimalNum / 2)
    try:
        parts[1] = '.' + parts[1]
        binaryNum += '.'
        decimalNum = float(parts[1])
        i = 0
        while decimalNum != 0 and i < 10:
            decimalNum *= 2
            parts = str(decimalNum).split('.')
            binaryNum += parts[0]
            decimalNum = float('.'+parts[1])
            i += 1
    except IndexError:
        pass
    
    if negative:
        binaryNum = "-" + binaryNum
    
    return binaryNum

def get_menu_choice():
    try:
        choice = int(input(menu()))
        
        if choice >= 1 and choice <=3:
            return choice
        else:
            print("Error: the data entered is not a positive number")
    except ValueError as e:
        print(e)
    print("The choice is invalid please choose again.")
    return get_menu_choice()


def menu():
    menuStr = ("Please Choose a Conversion:\n"
    "1. Convert Binary to Hexadecimal\n"
    "2. Convert Binary to Decimal\n"
    "3. Convert Decimal to Binary\n")
    return menuStr


def process_choice(choice):
    if choice == 1:
        binaryToHex("101")
    elif choice == 2:
        binaryToDecimal("101")
    elif choice == 3:
        #number = getFloat()
        decimalToBinary(6)
        
    else:
        print("Invalid menu choice!")
    



if __name__ == "__main__": #if the file is being run directly instead of imported
    main()

