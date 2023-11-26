print(
    "1. Cортування списка по зростанню числа, від меншого до більшого. Функція приймає список з чисел і повертає "
    "відсортований список.\n"
    "2. Сортування списка на спад, від  більшого до меншого. Функція приймає список з чисел і повертає "
    "відсортований список\n"
    "3. Сортування за кількістю букв у слові.Функція приймає список з слів і повертає відсортований список.\n")


def sort_list_asc(list_1=tuple([])):
    list_1 = list(list_1)
    list_2 = sorted(list_1)
    return list_2


def sort_list_desc(list_1=tuple([])):
    list_1 = list(list_1)
    list_2 = sorted(list_1, reverse=True)
    return list_2


def sort_list_alpha(list_1=tuple([])):
    list_1 = list(list_1)
    list_2 = sorted(list_1, key=len)
    return list_2


list_number = [34, 456, 11, -100, 77, 888, -35, 1031]
list_word = ['груша', 'яблуко', 'диня', 'слива', 'апельсин']
print(f"Список чисел: ", list_number)
print(f"Список слів: ", list_word)
print()
print("Cортування списка по зростанню числа, від меншого до більшого: ", sort_list_asc(list_number))
print("Сортування списка на спад, від  більшого до меншого: ", sort_list_desc(list_number))
print("Сортування за кількістю букв у слові: ", sort_list_alpha(list_word))
