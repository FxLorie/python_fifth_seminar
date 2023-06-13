# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии

def degree(a,b):
    if b < 1:
        return 1
    return a*degree(a,b-1)

a = int(input('Num a = '))
b = int(input('Num b = '))
print(degree(a,b))

