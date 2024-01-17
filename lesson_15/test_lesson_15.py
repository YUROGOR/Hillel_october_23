import pytest
from datetime import datetime
from hw_lesson_15 import Calculator


class TestClass:

    @classmethod
    def setup(cls):
        cls.calc = Calculator()

    @classmethod
    def setup_class(cls):
        with open("logs.txt", "a") as file:
            file.write(f'Start testing:{datetime.now()}\n')

    @classmethod
    def teardown_class(cls):
        with open("logs.txt", "a") as file:
            file.write(f'Stop testing:{datetime.now()}\n')
            file.write("\n")

    @pytest.mark.parametrize("numb_1, numb_2, result", [
        pytest.param(12, 4, 3),
        pytest.param(9, 3, 3),
        pytest.param(21, 7, 3),
        pytest.param(90, 5, 18),
        pytest.param(225, 25, 9)])
    def test_division(self, numb_1, numb_2, result):
        assert self.calc.division(numb_1, numb_2) == result

    @pytest.mark.parametrize("numb_1, numb_2, result", [
        pytest.param(12, 4, 16),
        pytest.param(9, 3, 12),
        pytest.param(21, 7, 28),
        pytest.param(90, 5, 95),
        pytest.param(225, 25, 250)])
    def test_addition(self, numb_1, numb_2, result):
        assert self.calc.addition(numb_1, numb_2) == result
