from random import randint

m = 5  # min-max integer number
#asdhasjkdhasjkdhasjkdasjkdhkashkdashkjdas

# Алгоритм пересчета
def sort_pereschet(arr):
    sort_list = [-m-1] * len(arr)
    for i in range(len(arr)):
        qt_smaller = 0
        for j in range(len(arr)):
            if arr[j] < arr[i]:
                qt_smaller += 1
        while sort_list[qt_smaller] != -m - 1:
            qt_smaller += 1
        sort_list[qt_smaller] = arr[i]
    return sort_list


input_list = []
print("Введите к-во строк и столбов (<10), разделенные пробелом. (Введите 0 для выхода)")
brk = 1
while brk != 0:
    input_list = input().split()
    if len(input_list) == 2:
        try:
            input_list = [int(i) for i in input_list]
            if 0 < input_list[0] <= 10 and 0 < input_list[1] <= 10:
                brk = 0
            else:
                print("Недопустимые значения (ожидается от 1 до 10)")
        except ValueError:
            print("Недопустимые значения (ожидаются целые числа от 1 до 10)")
    elif len(input_list) == 1:
        if input_list[0] == "0":
            print("Обнаружен код выхода")
            exit()
        else:
            print("Неверное к-во элементов ввода (ожидается 2)")
    else:
        print("Неверное к-во элементов ввода (ожидается 2)")

n = int(input_list[0])  # Raws
k = int(input_list[1])  # Columns
random_list = [[randint(-m, m) for i in range(0, k)] for j in range(0, n)]
print("Элементы в массиве в", n, "строки на", k, "столбца:", random_list)

min_el = m + 1
min_el_raw = -1
min_el_col = -1

for i in range(n):
    for j in range(k):
        if random_list[i][j] <= min_el:
            min_el = random_list[i][j]
            min_el_raw = i
            min_el_col = j

print("Минимальный элемент", min_el, "находится на строке", min_el_raw, "в столбце", min_el_col)
print("Строка с минимальным элементом:", random_list[min_el_raw])
print("Отсортированная методом пересчета строка:", sort_pereschet(random_list[min_el_raw]))
