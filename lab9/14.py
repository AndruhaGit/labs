# 14. Даний рядковий файл, який містить дати в форматі «день / місяць / рік», причому під день і місяць відводиться по дві позиції,
# а під рік - чотири (наприклад, «16/04/2001»).
# Створити два файли цілих чисел, перший з яких містить значення днів, а другий - значення місяців для дат з вихідного рядкового файлу (в тому ж порядку).
import random
lines = [random.randint(0, 31), random.randint(0, 12), random.randint(2000, 2020)]
with open('date.txt', 'w+') as file:
    file.writelines("%s /" % line for line in lines)
    file.close()
