print("Задача 1\n"
      "1) Напишіть 10 тестів(можна що б просто повертали Тру(щоб проходили)) імена тестів повині йти підряд\n"
      "test_1, test_2 ... Повішайти на них три декоратора old, main, new. кожен декоратор повинен бути на 3 функціях\n"
      "на одній з функцій повино бути повішано два декоратора old i main.\n"
      "додайти їх в python.ini що б були правильні виводи\n"
      "\n"
      "Зробіть такі прогони\n"
      "1) всі тексти де немає лейби old\n"
      "2) тест де пересікаються old i main.\n"
      "3) тести з маркерами main, new\n"
      "З домашкою здайте скріншоти з прогонами, на скріншотах повино бути\n"
      "видно який саме тест прогнався(використовуйте прапор verbose).\n")

print("Файл '.ini' під тести з маркером - https://github.com/YUROGOR/Hillel_october_23/python.ini\n"
      "Тести з маркуванням - test_mark_lesson_10.py\n"
      "Результати прогонів додано скрінами.\n")

print("Задача 2\n"
      "Візьміть задачу з минулого уроку(3- зробіть функцію як ми робили з додаванням тільки замість двох чисел "
      "зробіть три числа і протестуйте її всіма трьома методами)\n"
      "модернізуйте її так що кожний раз коли ми її запускаємо те що ми туди передаєм та результат повинно\n"
      "записуватись в файл log.txt\n"
      "Зверніть увагу на те що в файл повинно дозаписуватись, а не затератись.\n"
      "Уявіть що ця функція являється легасі кодом і ви її не можете змінювати,\n"
      "тому потрібно використовувати декоратор. Я хотів би бачити таку реалізацію в домашці три функції:\n"
      "функція з минулого уроку\n"
      "функція що записую текст\n"
      "і декоратор\n")

NUMBER_1 = 10
NUMBER_2 = 20
NUMBER_3 = 30
print(f'На вході функції є три числа: {NUMBER_1}, {NUMBER_2}, {NUMBER_3}\n')


def add_three_numbers(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result


print(f'Сума чисел = ', add_three_numbers(NUMBER_1, NUMBER_2, NUMBER_3))


def add_three_numbers2(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    with open("log.txt", "a") as log:
        log.write(f'На вході функції є три числа: {number_1}, {number_2}, {number_3}\n'
                  f'Сума всіх чисел = {result}\n')
        log.write("\n")
    return result


print(f'Сума чисел = ', add_three_numbers2(NUMBER_1, NUMBER_2, NUMBER_3))


def func_wrapper(func):
    def wrapper(*arg, **kwarg):
        result = func(*arg, **kwarg)
        print('Сума чисел = ', result)
        return result

    return wrapper


@func_wrapper
def add_three_numbers3(number_1: int | float, number_2: int | float, number_3: int | float) -> int | float:
    result = number_1 + number_2 + number_3
    return result


add_three_numbers3(NUMBER_1, NUMBER_2, NUMBER_3)
