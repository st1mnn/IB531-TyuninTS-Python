break_input = "q"
print('Вводите вещестественные числа. Для окончания ввода наберите "q"')

current_number = 0
current_input = 0
min_negative_number = 0
min_negative = 0

while current_input != break_input:
    del current_input
    current_input = input()
    if current_input == break_input:
        break
    else:
        current_input = float(current_input)
        current_number += 1
        if current_input <= min_negative:
            min_negative = current_input
            min_negative_number = current_number

if min_negative == 0:
    print('Среди', current_number, 'введенных чисел нет отрицательных')
else:
    print('Минимальное отрицательной число', min_negative, 'последний раз было введено', min_negative_number, 'среди', current_number, 'введенных чисел')
