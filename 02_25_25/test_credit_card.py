import CCDemo
from pytest import raises

def test_valid_credit_card():
    """testing the credit card checksum functions"""
    #4578 4230 1376 9219
    digitList = CCDemo.credit_card_valid_step_1_and_2("4578 4230 1376 9219")
    testDigitList = [8, 5, 14, 8, 8, 2, 6, 0, 2, 3, 14, 6, 18, 2, 2, 9]
    assert digitList == testDigitList
    digitList = CCDemo.credit_card_valid_step_3(digitList)
    testDigitList = [8, 5, 5, 8, 8, 2, 6, 0, 2, 3, 5, 6, 9, 2, 2, 9]
    assert digitList == testDigitList
    testSum = 80
    sum = CCDemo.credit_card_valid_step_4(digitList)
    assert sum == testSum
    valid = CCDemo.credit_card_valid_step_5(sum)
    assert valid == True

def test_invalid_credit_card():
    #4578 4230 1376 9219
    digitList = CCDemo.credit_card_valid_step_1_and_2("4578 4235 1376 9219")
    testDigitList = [8, 5, 14, 8, 8, 2, 6, 5, 2, 3, 14, 6, 18, 2, 2, 9]
    assert digitList == testDigitList
    digitList = CCDemo.credit_card_valid_step_3(digitList)
    testDigitList = [8, 5, 5, 8, 8, 2, 6, 5, 2, 3, 5, 6, 9, 2, 2, 9]
    assert digitList == testDigitList
    testSum = 8 + 5 + 5 + 8 + 8 + 2 + 6 + 5 + 2 + 3 + 5 + 6 + 9 + 2 + 2 + 9
    sum = CCDemo.credit_card_valid_step_4(digitList)
    assert sum == testSum
    valid = CCDemo.credit_card_valid_step_5(sum)
    assert valid == False

def test_invalid_number():
    with raises(ValueError):
        CCDemo.credit_card_valid_step_1_and_2("1234abcd")
        CCDemo.credit_card_valid_step_1_and_2("4578 4235 13A6 9219")