import random

from tabulate import tabulate

one = two = three = four = five = six = 0
rand = float(0)
total_number_of_rolls = 1000
x = 0
while x < total_number_of_rolls:
    x = x + 1
    rand = random.random()
    if rand < 1/6:
        one = one + 1
    elif rand < 2/6:
        two = two + 1
    elif rand < 3/6:
        three = three + 1
    elif rand < 4/6:
        four = four + 1
    elif rand < 5/6:
        five = five + 1
    else:
        six = six + 1

total = one + two + three + four + five + six
f1 = round(100 * one / total, 1)
f2 = round(100 * two / total, 1)
f3 = round(100 * three / total, 1)
f4 = round(100 * four / total, 1)
f5 = round(100 * five / total, 1)
f6 = round(100 * six / total, 1)
Total = round(f1 + f2 + f3 + f4 + f5 + f6,1)
table = {'FACE NUMBER': [1, 2, 3, 4, 5, 6, 'Total'], 'FREQUENCY': [one, two, three, four, five, six, total],
         'PERCENTAGE(%)': [f1, f2, f3, f4, f5, f6, Total]}
print(tabulate(table, headers='keys'))
