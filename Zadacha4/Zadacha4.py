# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def get_input():
    while True:
        try:
            n= int(input('введите число : '))
            return n
        except ValueError:
            print("Ошибочный ввод.")

n = get_input()
print(bin(n)[2::])