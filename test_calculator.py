import calculator
def test_calc_multipy():

    multiply = calculator.mul(4, 5)
    assert multiply==20
def test_calc_add():
    addition = calculator.add(40, 4)
    assert addition == 44
test_calc_add()
test_calc_multipy()