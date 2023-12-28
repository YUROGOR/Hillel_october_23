print("Задача:\n"
      "Виберіть який з наступних магічних методів і реалізуйте його в простому класі:\n"
      "__ne__: To check if two objects are not equal.\n"
      "__lt__: To check if one object is less than another.\n"
      "__le__: To check if one object is less than or equal to another.\n"
      "__gt__: To check if one object is greater than another.\n"
      "__ge__: To check if one object is greater than or equal to another.\n"
      "Жодного з цих методів ми не розглядали на уроці, але вони працюють ідентично до метода ___eq__ ,\n"
      "який ми розглянули на уроці.Тобто вам треба буде змінити всього дві букви."
      "І написати свою логіку яку ви хочте.\n"
      "Створіть два обьєта класа в якому ви це реалізували і зробіть перевірку що все працює\n"
      "\n"
      "Рішення:\n")


class A:
    def __init__(self, text):
        self.text = text

    def __bool__(self):
        if len(self.text) < 20:
            return False
        return True

    def __ne__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError
        elif abs(int(self.text) - int(other.text)) < abs(int(self.text) + int(other.text)):
            return True
        else:
            return False


a = A("1000")
a_2 = A("3000")

print(a != a_2)
