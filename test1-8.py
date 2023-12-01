from random import randint

def magic(arr,numb):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i] ** 2
    if sum % numb == 0:
        return "Волшебство случается"
    else:
        return "Никакого волшебства"

n = 500  # Requested number of elements
m = 50  # min-max integer number
random_list = [randint(0, m) for i in range(0, n)]
print(magic(random_list,2))
