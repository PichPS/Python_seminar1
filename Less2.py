# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input("Введите кол-во учеников в 1-ом кабинете: "))
# b = int(input("Введите кол-во учеников в 2-ом кабинете: "))
# c = int(input("Введите кол-во учеников в 3-ом кабинете: "))
# result = a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2
# print(result)


# import math

# a = int(input("Введите кол-во учеников в 1-ом кабинете: "))
# b = int(input("Введите кол-во учеников в 2-ом кабинете: "))
# c = int(input("Введите кол-во учеников в 3-ом кабинете: "))
# result = math.ceil(a / 2) + math.ceil(b / 2) + math.ceil(c / 2)
# print(result)


import math


a = int(input("Введите кол-во учеников в 1-ом кабинете: "))
b = int(input("Введите кол-во учеников в 2-ом кабинете: "))
c = int(input("Введите кол-во учеников в 3-ом кабинете: "))
s1 = (a + 1) // 2
s2 = (b + 1) // 2
s3 = (c + 1) // 2
print(s1 + s2 + s3)