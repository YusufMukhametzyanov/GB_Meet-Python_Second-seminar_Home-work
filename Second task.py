# Задайте список из n чисел последовательности (1 + 1/n)^n, выведите его на экран,
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input('Enter number n: '))
summ = [round((1+1/i)**i, 3) for i in range(1, number+1)]
print(f'Для n = {number} -> {summ} \n Сумма {round(sum(summ), 3)}')