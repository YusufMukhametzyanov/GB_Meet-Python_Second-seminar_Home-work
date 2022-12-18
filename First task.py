# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = input('Enter number: ')
sum = 0
for a in number:
    if a.isdigit():
        sum += int(a)

print(f"{number} -> ", sum)