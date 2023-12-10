import pytest
from hw_lesson_9 import add_three_numbers


# solution 1
def test_1():
    assert add_three_numbers(3, 4, 5) == 12


# solution 2
@pytest.mark.parametrize("numb_1, numb_2, numb_3, result", [
    pytest.param(3, 4, 5, 12, id="standard"),
    pytest.param(-3, 3, 0, 0, id="negative and positive"),
    pytest.param(-3, -4, -5, -12, id="three negative")])
def test_set_1(numb_1, numb_2, numb_3, result):
    assert add_three_numbers(numb_1, numb_2, numb_3) == result


# solution 3
list_test = [(3, 4, 5, 12), (-3, 3, 0, 0), (-3, -4, -5, -12)]


@pytest.mark.parametrize("numb_1, numb_2, numb_3, result", list_test)
def test_set_2(numb_1, numb_2, numb_3, result):
    assert add_three_numbers(numb_1, numb_2, numb_3) == result
