print("Задача 1")
print("Залишок від ділення: Користувач вводить два числа. Вивести залишок від ділення першого числа на друге.")


def remainder(number_1: int | float, number_2: int | float):
    result = number_1 % number_2
    return result


def out(string):
    out_string = f"Залишок від ділення першого числа на друге: {string}"
    return out_string


user_number_1 = int(input("Введіть перше число: "))
user_number_2 = int(input("Введіть друге число: "))
result_remainder = remainder(number_1=user_number_1, number_2=user_number_2)
new_string = out(string=result_remainder)
print(new_string)
print()
print("Задача 2")
print("Напишіть програму яка запитує в користувача вартість покупок, він їх вводе через пробіл, точна кількість\n"
      "не вказана. Вам потрібно до вартості покупок додати 6,5 відсотки податків.\n"
      "Потім питаєте чи є в користувача купон на знижку, якщо є то питаєте це на суму чи на відсоток і потім\n"
      "віднімаєте суму або відсоток відповідно від ціни яку отримали раніше і пишете користувачу кінцеву суму.")
print()


def list_price_string(string):
    list_1 = string.split()
    return list_1


def print_final_price(string):
    out_string = f"Сума до сплати - : {string}"
    return out_string


def final_price_without_sum(number_1: int | float, number_2: int | float):
    final_price_1 = number_1 - number_2
    return final_price_1


def final_price_without_percent(number_1: int | float, number_2: int | float):
    final_price_2 = number_1 - (number_1 * number_2) / 100
    return final_price_2


price = input("Введіть будь ласка вартість покупок через пробіл(копійки вводимо через крапку):")
list_string = list_price_string(price)
list_2 = []
for element in list_string:
    element = float(element)
    list_2.append((element * 6.5) / 100 + element)
final_price = sum(list_2)
coupon = input("Підкажіть у Вас є купон на знижку?(так - 1, ні - 2) - ")
if coupon == '2':
    print(print_final_price(final_price))
else:
    discount = input("Знижка на суму чи відсоток ?(сума - 1, відсоток - 2) - ")
    if discount == '1':
        discount_sum = float(input("Вкажіть суму знижки ?(копійки вводимо через крапку) - "))
        print(print_final_price(final_price_without_sum(final_price, discount_sum)))
    else:
        discount_percent = float(input("Вкажіть відсоток знижки ?(знак розділення крапка) - "))
        print(print_final_price(final_price_without_percent(final_price, discount_percent)))
print()
finish = input("Натисніть ENTER для завершення роботи.")
print(finish)
