
class BinaryNumber:
    def __init__(self, binaryNumber:str):
        self.binaryNum = binaryNumber
        self.validateBinaryNumber()

    def validateBinaryNumber(self):
        """Validates a string is a binary number consisting of all 1s and 0s"""
        self.negative = False
        self.floatingPoint = False
        if self.binaryNum[0] == '-' and self.binaryNum.count('-') == 1:
            self.binaryNum = self.binaryNum.replace('-','')
            self.negative = True
        elif self.binaryNum.count('-') > 1:
            raise ValueError("Numbers cannot have more than 1 -")
        
        if self.binaryNum.count('.') > 1:
            raise ValueError("Numbers cannot have more than 1 .")
        
        for digit in self.binaryNum:
            if digit != '0' and digit != '1' and digit != '.':
                raise ValueError("Binary numbers contain only 1s and 0s")
            
            
    

    def binaryToDecimal(self):
        """Converts a binary number given as a string to a decimal number stored as an int"""
        decimalNum = 0.0
        parts = self.binaryNum.split('.')
        
    
        for exponent in range(0, len(parts[0])):
            decimalNum += int(parts[0][-1 - exponent]) * 2**exponent
            #print(decimalNum)
        try:
            i = 0
            for exponent in range (-1, -1 * len(parts[1]), -1):
                decimalNum += float(parts[1][i]) * 2 ** exponent
                i+=1
        except IndexError:
            pass
        if self.negative:
            decimalNum *= -1
        return decimalNum



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
