# 14. Дано список з п'яти чисел. Переставити цифри в числах задом наперед і вивести нове найбільше. Список заповнити випадковими числами.
import random
n = 10
b = random.randint(5,n)
a = [i for i in range(b)]

print(a)
d = a[::-1] # переворачиваем список вобратном порядке
print(d)