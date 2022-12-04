# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])
import random
def func(lst: list[int]) -> list:
    lst2 = []
    iterations = round((len(lst)+1)/2)
    for i in range(round(len(lst)/2)):
        lst2.append(lst[i]*lst[-1-i])
    return lst2


lst_rnd = [random.randint(1, 10) for i in range(0, 7)]
print(lst_rnd)
print(func(lst_rnd))
