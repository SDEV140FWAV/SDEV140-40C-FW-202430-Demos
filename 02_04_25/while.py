"""Author: Angela Venable"""

theSum = 0.0
data = " "


while data != "": # and data.isdigit()
    data = input("Enter a number or just enter to quit: ")
    dataCpy = data.replace(".", "").replace("-","")
    
    if not dataCpy.isnumeric() or data.count(".") > 1 or data.count("-") > 1:
        if data != "":
            print("The input is not a floating point number.")
        continue
    number = float(data)
    theSum += number # theSum = theSum + number
    
    
print(f"The sum is {theSum:.3f}")