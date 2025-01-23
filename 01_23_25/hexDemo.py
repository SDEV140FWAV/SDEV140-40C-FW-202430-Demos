binaryNum = list(input("Enter a binary number: "))
binaryNumcpy = binaryNum[:]
binaryNumcpy.insert(0,'0')
binaryNumcpy.insert(0,'0')
binaryNumcpy.insert(0,'0')
print(binaryNum)
# 0001 1011
#binaryNum.reverse()
""" hexDigits = binaryNum[::3]
print(hexDigits)
rangeList = list(range(-4, -1 * len(binaryNum) - 1,-4))
print(rangeList)
for group in range(-1, -1 * len(binaryNum) - 1,-4):
    hexDigits.append(binaryNum[group:4])
    print(binaryNum[group:4]) """
""" for group in hexDigits:
    group.reverse()
 """
"""
The conversion to decimal starts below
The code loops through the digits starting at the right
The loop keeps track of the current power of 2 for the conversion
The sum is kept in decimalNum
"""
decimalNum = 0
for exponent in range(0, len(binaryNum)):
    decimalNum += int(binaryNum[-1 - exponent]) * 2**exponent
print(decimalNum)

dimensions = (200, 50)
print(f"{dimensions[0]} x {dimensions[1]}")
#dimensions[0] = 400
dimensions = (400, 600)
print(f"{dimensions[0]} x {dimensions[1]}")

