"""
Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
"""

number = int(input("Введите число: "))
degree = 2
print("Целые степени двойки: ")
while degree < number:
    print(degree, end=' ')
    degree *= 2
