print("Задача 1\n"
      "додайте requirements.txt на ваш гіт\n")

print("Результати - https://github.com/YUROGOR/Hillel_october_23/tree/main\n")

print("Задача 2\n"
      "Виберіть будь-яку помилку яка вам подобається і зробіть функцію яка перевіряє на цю помилку"
      "(в функції try except)\n")

print("Перевіряємо в функції try except команду import testtime")
try:
    import testtime
except ImportError:
    print("Такого модулю не знайдено, помилка ImportError\n")

print("Задача 3\n"
      "Зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма "
      "трьома методами\n")


def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result


print("Запускаємо та дивимось результати "
      "в https://github.com/YUROGOR/Hillel_october_23/tree/main/lesson_9/test_lesson_9.py\n")

print("Задача 4\n"
      "перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює\n")

from datetime import datetime


def func_wrapper_time(func):
    def wrapper(*arg, **kwarg):
        start = datetime.now()
        result = func(*arg, **kwarg)
        delta_time = datetime.now() - start
        print("Час виконання функції ось такий: ", delta_time)
        return result

    return wrapper


import time


@func_wrapper_time
def foo_1(*arg, **kwarg):
    print("foo_1")
    time.sleep(3)


@func_wrapper_time
def foo_2(*arg, **kwarg):
    print("foo_2")
    time.sleep(5)


foo_1()
foo_2()

