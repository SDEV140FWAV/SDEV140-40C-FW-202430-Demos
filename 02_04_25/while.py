"""Author: Angela Venable"""

theSum = 0.0
data = input("Enter a number or just enter to quit: ")
dataCpy = data.replace(".", "").replace("-","")

while data != "" and dataCpy.isnumeric(): # and data.isdigit()
    number = float(data)
    theSum += number # theSum = theSum + number
    data = input("Enter a number or just enter to quit: ")
    dataCpy = data.replace(".", "").replace("-","")
print(f"The sum is {theSum:.3f}")