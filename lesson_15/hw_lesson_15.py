print("Задачв 1.\n"
      "Напишіть ліст компрехеншин який формує список всіх чисел від 34 до 121 які діляться націло на 3 та на 2\n"
      "\n"
      "Рішення:\n")
list_comp = [i for i in range(34, 121) if i % 2 == 0 or i % 3 == 0]
print(list_comp)
print()
print("Задачв 2.\n"
      "Напишіть клас калькулятора де будуть 4 арифметичні дії плюс, мінус, додавання, множення - звичайні методи.\n"
      "і зробіть статік метод який буде виводити повідомлення, привіт я калькулятор.\n"
      "\n"
      "Рішення:\n")


class Calculator:

    # def __init__(self, number1, number2):
    #     self.number1 = number1
    #     self.number2 = number2

    def division(self, number1, number2):
        div = round(number1 / number2, 3)
        return div

    def multiplication(self, number1, number2):
        multi = number1 * number2
        return multi

    def addition(self, number1, number2):
        add = number1 + number2
        return add

    def subtraction(self, number1, number2):
        sub = number1 - number2
        return sub

    @staticmethod
    def hello_calculator():
        print("Привіт! Я калькулятор")


operation = Calculator()
print(operation.division(11, 12))
print(operation.multiplication(13, 14))
print(operation.addition(15, 16))
print(operation.subtraction(17, 18))
Calculator.hello_calculator()
print()
print("Задачв 3.\n"
      "Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.\n"
      " до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого)\n"
      "Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення в файл коли ми\n"
      "запустили тест та текстове повідомлення що ми стартанули. Тердаун буде писати повідомлення що ми закінчили і\n"
      "також час коли закінчили  використайте вже відому вам бібліотеку дататайм\n"
      "\n"
      "Рішення:\n")
print(f"Запустити кейси з test_lesson_15")

