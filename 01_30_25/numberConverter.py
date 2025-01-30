import random
import sys

binaryNum = input("Enter a binary string: ")
hexDigits = {"0":"0000","1":"0001","A":"1010", "a":"1010","C":"1100"}
hexDigits["B"] = "1011"
hd = input("Enter a hex digit: ")
print(hexDigits.get(hd, f"There is no binary mapping for {hd}"))
print(hexDigits.pop(hd,f"There is no binary mapping for {hd}"))
print(hexDigits)
del hexDigits["F"]

binaryNum = binaryNum.replace(" ", "")
if binaryNum.isdigit():
    """decimal conversion"""
    decimalNum = 0
    for exponent in range(0, len(binaryNum)):
        if binaryNum[-1 - exponent] != "1" and binaryNum[-1 - exponent] != "0":
            print("Error: The string contain non binary digits")
            #break
            sys.exit()
        else:    
            decimalNum += int(binaryNum[-1 - exponent]) * 2**exponent
    print(f"{binaryNum} is {decimalNum} in decimal")

    for i in range(4 - len(binaryNum)%4):
        binaryNum = "0" + binaryNum
    #print(binaryNum)
    segements = []
    hexNum = ""
    for group in range(0, len(binaryNum), 4):
        segements.append(binaryNum[group:group+4])
    for seg in segements:
        match seg:
            case '0000':
                hexNum = hexNum + "0"
            case '0001':
                hexNum = hexNum + "1"
            case '0010':
                hexNum = hexNum + "2"
            case '0011':
                hexNum = hexNum + "3"
            case '0100':
                hexNum = hexNum + "4"
            case '0101':
                hexNum = hexNum + "5"
            case '0110':
                hexNum = hexNum + "6"
            case '0111':
                hexNum = hexNum + "7"
            case '1000':
                hexNum = hexNum + "8"
            case '1001':
                hexNum = hexNum + "9"
            case '1010':
                hexNum = hexNum + "A"
            case '1011':
                hexNum = hexNum + "B"
            case '1100':
                hexNum = hexNum + "C"
            case '1101':
                hexNum = hexNum + "D"
            case '1110':
                hexNum = hexNum + "E"
            case '1111':
                hexNum = hexNum + "F"
    print(f"{binaryNum} is {hexNum} in hexadecimal")
    decimalNum = 0
    numericDigits = ['0','1','2','3','4','5','6','8','9']
    for exponent in range(0, len(hexNum)):
        if hexNum[-1 - exponent] in numericDigits:
            decimalNum += int(hexNum[-1 - exponent]) * 16**exponent
        else:
            match hexNum[-1 - exponent].upper():
                case "A":
                    decimalNum += 10 * 16**exponent
                case "B":
                    decimalNum += 11 * 16**exponent
                case "C":
                    decimalNum += 12 * 16**exponent
                case "D":
                    decimalNum += 13 * 16**exponent
                case "E":
                    decimalNum += 14 * 16**exponent
                case "F":
                    decimalNum += 15 * 16**exponent
    print(f"{hexNum} is {decimalNum} in decimal")
                



