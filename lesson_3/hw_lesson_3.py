print("Задача 1")
print(
    "Уявимо що до нас прийшов наш друг або подруга і попросили написати додаток для покупок в магазині\n"
    "що б можна було скласти список продуктів та коли купуєш викреслювати для викреслення питайте номер елемента\n"
    "що б видалити по індексу треба його передати в pop list_a.pop(0) - видалить нульовий індекс, памятайте що\n"
    "користувач не знає що в нас індекси починаються з нуля. Також нам відомо що цей список має пять або більше елементів.\n"
    "Після кожного видалення елементу виводьте наш оновлений список. Після 5 видалень перевірте чи список пустий якщо\n"
    "не пустий напишіть що ось ще є продукти, якщо пусти то напишіть про це.\n"
    "Також після цього кроку запропонуйте користувачу написати ще продуктів та додати його в кошик.\n"
    "і виведіть їх на екран. Але цього разу вже без видалень.\n")
print("Кроки:\n"
      "1. Спочатку пропонуємо користувачу ввести продукти.\n"
      "2. Робимо 5 запитів на видалення\n"
      "3. Перевіряємо корзину\n"
      "4. Пропонуємо додати продукти\n"
      "5. Виводмо список і прощаємось\n")
print()
var_1 = input(
    "Введіть будь ласка через пробіл товари, що Ви плануєте купити\n"
    "(не менше 5 товарів, тільки літери):")
list_1 = var_1.split()
if len(list_1) < 5:
    print("Вибачте! Товарів менше п'яти.")
    finish = input("Натисніть ENTER для завершення роботи.")
    print(finish)
else:
    print(list_1)
    var_2 = int(input("Введіть порядковий номер товару , який ви вже купили: "))
    list_1.pop(var_2 - 1)
    print(list_1)
    var_2 = int(input("Введіть порядковий номер товару , який ви вже купили: "))
    list_1.pop(var_2 - 1)
    print(list_1)
    var_2 = int(input("Введіть порядковий номер товару , який ви вже купили: "))
    list_1.pop(var_2 - 1)
    print(list_1)
    var_2 = int(input("Введіть порядковий номер товару , який ви вже купили: "))
    list_1.pop(var_2 - 1)
    print(list_1)
    var_2 = int(input("Введіть порядковий номер товару , який ви вже купили: "))
    list_1.pop(var_2 - 1)
    print()
    if len(list_1) < 1:
        print("Вітаю Ви купили все, що планували!\n")
    else:
        print("В кошику ще лишились товари", list_1)
    print()
    var_3 = input("Бажаєте додати ще товар (наберіть так чи ні)?")
    if var_3 == "так":
        var_4 = input("Введіть будь ласка товар, що Ви плануєте купити: ")
        list_1.append(var_4)
        print("Наразі в кошику:", list_1)
        finish = input("Натисніть ENTER для завершення роботи.")
        print(finish)
    else:
        finish = input("Натисніть ENTER для завершення роботи.")
        print(finish)
