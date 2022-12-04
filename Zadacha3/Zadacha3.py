# 3'. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def func_separate(num: float) -> float:
    list_num = str(num).split('.')
    return float('0.'+list_num[1])

def min_max(num_list: list[float]) ->float:
    new_list = [func_separate(i) for i in num_list if int(i) != float(i)]
    print (new_list)
    return max(new_list) - min(new_list)
example=[1.1, 1.2, 3.1, 5, 10.01]

print(min_max(example))


