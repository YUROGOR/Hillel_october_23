print("Задача 1")
print("Зробіть словник де буде табличка множення додавання ділення і віднімання чисел від 2 до 9(включно).\n"
      "(так як робили на уроці). Ці значення запишіть в словник з відповідними ключами '+', '-', '/', '*'\n"
      "Коли ви підготуєте це, запитайте в користувача яку табличку він хоче побачити (додавання, віднімання,\n"
      "множення, ділення). і виведіть йому цю табличку.")
print()
list_multi = []
list_div = []
list_add = []
list_sub = []
for i in range(2, 10):
    for j in range(2, 10):
        list_multi.append(f"{i} * {j} = {i * j}")
        list_add.append(f"{i} + {j} = {i + j}")
        list_sub.append(f"{i} - {j} = {i - j}")
        division = float(i / j)
        division = round(division, 3)
        list_div.append(f"{i} : {j} = {division}")
dict_table = {"*": list_multi, "/": list_div, "+": list_add, "-": list_sub}
choice = input("Виберіть яку табличку Ви хочете побачити: додавання, віднімання,множення,ділення ? "
               "Введіть відповідно '+', '-', '/', '*' : ")
print(dict_table.get(choice))
finish = input("Натисніть ENTER для завершення роботи.")
print(finish)
