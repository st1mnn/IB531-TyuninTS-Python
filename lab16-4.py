from random import randint


def print_list(list, elem_in_line, symbols_in_elem):
#    elem_in_line = 8
#    symbols_in_elem = 8
    if len(list) < elem_in_line:
        format_txt = '{:%d}' % symbols_in_elem * len(list)
        print(format_txt.format(*list))
    else:
        format_txt = '{:%d}' % symbols_in_elem * len(list[0:elem_in_line - 1])
        print(format_txt.format(*list[0:elem_in_line - 1]))
        print_list(list[elem_in_line:], elem_in_line, symbols_in_elem)


print('Введите длину массива произвольных целых чисел')
n = int(input())
m = 100000  # min-max integer number
random_list = [randint(-m, m) for i in range(0, n)]
print('Массив произвольных целых числе из', n, 'элементов:')
print_list(random_list, 8, 8)

summ = 0
summ_count = 0
for i in range(len(random_list)):
    if random_list[i] > 0 and random_list[i] % 2 == 0:
        # print("Элемент", i, "равный", random_list[i], "положительный четный")
        summ += random_list[i]
        summ_count += 1

# print("Количество положительных четных элементов массива:", summ_count)
# print("Сумма положительных четных элементов массива:", summ)
if summ_count != 0:
    print("Целая часть среднего арифметического положительных четных элементов массива:", summ // summ_count)
else:
    print("Нет положительных четных элементов массива")
