# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a,b):
    if a < b:
        k1, k2 = a, b
    else: k1, k2 = b, a
    if k1 == 0:
        return k2
    return sum(k2+1,k1-1)

a = int(input('Num a = '))
b = int(input('Num b = '))
print(sum(a,b))