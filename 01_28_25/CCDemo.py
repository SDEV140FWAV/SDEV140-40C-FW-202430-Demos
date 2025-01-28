creditCard = input("Enter your credit card number: ")
creditCard = creditCard.replace(" ", "")
if len(creditCard) != 16:
    print("Credit card numbers must be 16 digits.")
else:
    if creditCard.isdigit():
        digitList = [int(digit) for digit in creditCard]
        """ for digit in creditCard:
            digitList.append(int(digit)) """
            
        print(digitList)
        digitListcpy = []
        """ for index in range(0,15,2):
            digitList[index] = digitList[index] * 2
            digitList[index] = digitList[index] % 10 + int(digitList[index]/10) """
        for digit in digitList[::2]:
            digit = digit * 2
            digit = digit % 10 + int(digit/10)
            digitListcpy.append( digit)
        for digit in digitList[1::2]:
            digitListcpy.append(digit)

        print(digitListcpy)
        ccSum = sum(digitListcpy)
        print(ccSum)
        if ccSum % 10 == 0:
            print(f"{creditCard} is a valid credit card number.")
        else:
            print(f"{creditCard} is not valid!")
    else:
        print("The credit card number can't contain non-digts.")
print("Thank you for checking your credit card number with us!")
"""

digitList[0] = digitList[0] % 10 + int(digitList[0]/10)
digitList[2] = digitList[2] % 10 + int(digitList[2]/10)
digitList[4] = digitList[4] % 10 + int(digitList[4]/10)
digitList[6] = digitList[6] % 10 + int(digitList[6]/10)
digitList[8] = digitList[8] % 10 + int(digitList[8]/10)
digitList[10]= digitList[10] % 10 + int(digitList[10]/10)
digitList[12]= digitList[12] % 10 + int(digitList[12]/10)
digitList[14]= digitList[14] % 10 + int(digitList[14]/10)

print(digitList)
ccSum = digitList[0] + digitList[1] + digitList[2] + digitList[3] 
ccSum += digitList[4] + digitList[5] + digitList[6] + digitList[7] \
    + digitList[8] + digitList[9] + digitList[10] + digitList[11] \
    + digitList[12] + digitList[13] + digitList[14] + digitList[15]
print(ccSum) """
#end of program for now
