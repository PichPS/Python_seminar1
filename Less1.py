# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input: n = 700 m = 750
# Output: 2

# n = int(input("Введите кол-во км пройденное за день: "))
# m = int(input("Введите длину маршрута: "))
# print((m + n - 1) // n)

import math

n = int(input("Введите кол-во км пройденное за день: "))
m = int(input("Введите длину маршрута: "))
print(math.ceil(m / n))