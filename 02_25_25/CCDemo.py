
def credit_card_valid_step_1_and_2(creditCard:str):

    creditCard = creditCard.replace(" ", "")
    if len(creditCard) != 16 or not creditCard.isdigit():
        raise ValueError("Credit card numbers must be 16 numeric digits.")
    else:
        digitList = [int(digit) for digit in creditCard]
    for index in range(0,15,2):
        digitList[index] = digitList[index] * 2
    
    return digitList

def credit_card_valid_step_3(digitList):
    for index in range(0,15,2):
        digitList[index] = digitList[index] % 10 + int(digitList[index]/10)
    return digitList

def credit_card_valid_step_4(digitList):
    return sum(digitList)

def credit_card_valid_step_5(digitTotal):
    if digitTotal % 10 == 0:
        return True
    else:
        return False



    





    
    