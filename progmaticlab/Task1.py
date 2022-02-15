import itertools
from itertools import *

operands = ("9", "8", "7", "6", "5", "4", "3", "2", "1", "0")
# получаем все возможные комбинации длиной в 9 символов из представленных операторов
operators = ["+", "-", ""]
comb = [p for p in itertools.product(operators, repeat=9)]


# для каждой комбинации из comb поочередно миксуем элементы с операндами
for el in comb:
    lst = []
    # добавляем поочередно элементы из zip с проверкой на None, т.к. zip комбинирует по самому длинному списку
    for i in list(zip_longest(operands, el)):
        for elem in i:
            if elem is not None:
                lst.extend(elem)
    # склеиваем список в строку, вычисляем выражение в строке и делаем проверку на равенство к цифре "200"
    lst_str = ''.join(lst)
    check = eval(lst_str)
    if check == 200:
        print(f"{lst_str} = 200")
