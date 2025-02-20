"""Author: Angela Venable
    Number converter program
"""

import random
from binarynumber import BinaryNumber

hexDigits = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100", 
             "5":"0101","6":"0110","7":"0111","8":"1000","9":"1001",
             "A":"1010","B":"1011","C":"1100","D":"1101",
             "E":"1110","F":"1111"}

def main():
    
    choice = get_menu_choice()
    res = process_choice(choice)
    print(f"{res['inputNumber']} is {res['resultNum']} in {res['result']}")
    """ length = random.randint(1,64)
    binaryNumberStr = ""
    for i in range(length):
        digit = random.randint(0,1)
        binaryNumberStr += str(digit) """
    #decimalNum = binaryToDecimal(binaryNumberStr)
    #print(f"{binaryNumberStr} is {decimalNum} in decimal")
    #hexNum = binaryToHex(binaryNumberStr)
    #print(f"{binaryNumberStr} is {hexNum} in hexadecimal")




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
    result = {}
    if choice == 1:
        binaryNum = getBinary()
        #hex = binaryToHex("101")
        result = {"inputNumber":"101", "resultNum":5, "result":"hexadecimal"}

    elif choice == 2:
        binaryNum = getBinary()
        dec = binaryNum.binaryToDecimal()
        result = {"inputNumber":binaryNum.binaryNum, "resultNum":dec, "result":"decimal"}
    elif choice == 3:
        number = getFloat()
        binaryNum = decimalToBinary(number)
        result = {"inputNumber":number, "resultNum":binaryNum, "result":"binary"}
        
    else:
        print("Invalid menu choice!")
    return result
    
def getFloat():
    try:
        num = float(input("Enter a floating point number: "))
        return num
    except ValueError as e:
        print(e)
        print("You entered something that is not a number.")
    return getFloat()

def getBinary():
    try:
        num = BinaryNumber(input("Enter a binary number: "))
        return num
    except ValueError as e:
        print(e)
        print("You entered something that is not a number.")
    return getBinary()
    



if __name__ == "__main__": #if the file is being run directly instead of imported
    main()

