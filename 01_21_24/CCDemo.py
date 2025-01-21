creditCard = input("Enter your credit card number: ")
creditCard = creditCard.replace(" ", "")
digitList = []
digitList.append(int(creditCard[0]))
digitList.append(int(creditCard[1]))
digitList.append(int(creditCard[2]))
digitList.append(int(creditCard[3]))
digitList.append(int(creditCard[4]))
digitList.append(int(creditCard[5]))
digitList.append(int(creditCard[6]))
digitList.append(int(creditCard[7]))
digitList.append(int(creditCard[8]))
digitList.append(int(creditCard[9]))
digitList.append(int(creditCard[10]))
digitList.append(int(creditCard[11]))
digitList.append(int(creditCard[12]))
digitList.append(int(creditCard[13]))
digitList.append(int(creditCard[14]))
digitList.append(int(creditCard[15]))
print(digitList)
digitList[0] = digitList[0] * 2
digitList[2] = digitList[2] * 2
digitList[4] = digitList[4] * 2
digitList[6] = digitList[6] * 2
digitList[8] = digitList[8] * 2
digitList[10] = digitList[10] * 2
digitList[12] = digitList[12] * 2
digitList[14] = digitList[14] * 2

print(digitList)
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
print(ccSum)
