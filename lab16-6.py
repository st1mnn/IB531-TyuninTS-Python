# pip install tabulate
from tabulate import tabulate


def funct(x, eps):
    fx = 0
    fx2 = 1
    k = 1
    while k <= 100 and abs(fx2 - fx) > eps:
        fx = fx2
        fx2 += (((-1) ** k) * (x ** k) * (k + 1) * (k + 2)) / 2
        k += 1
    return fx2


# def print_list(list):
#    for i in list:
#        print('{:5f}\t{:5f}'.format(i[0], i[1]))

#A = -0.1
print('Введите A (-0.1)')
A = float(input())
#B = -0.2
print('Введите B (-0.2)')
B = float(input())
#Nx = 13
print('Введите Nx (13)')
Nx = int(input())
#EPS = 10 ** -5
print('Введите EPS 1e-Y (Y=-5)')
EPS = 10 ** (int(input()))

Dx = (B - A) / Nx

X = A
final_list = []
print("A: {}\tB: {}\tDx: {:.5f}\tEPS: {:.5f}".format(A, B, Dx, EPS))
# print("X\t\t\tFx")
for j in range(Nx + 1):
    Fx = (1 + X) ** -3
    S = funct(X, EPS)
    # print('{:5f}\t{:5f}'.format(X, Fx))
    final_list.append([X, Fx, S])
    X += Dx

# print_list(final_list)
print(tabulate(final_list, headers=['x', 'Fx', 'S'], tablefmt="grid", floatfmt=".5f"))

with open('lab16-6.txt', 'w') as file_print:
    file_print.write("A: {}\tB: {}\tDx: {:.5f}\tEPS: {:.5f}\n".format(A, B, Dx, EPS))
    file_print.write(tabulate(final_list, headers=['x', 'Fx', 'S'], tablefmt="grid", floatfmt=".5f"))

with open('lab16-6v2.txt', 'w') as file_print:
    file_print.write("A: {}\tB: {}\tDx: {:.5f}\tEPS: {:.5f}\n".format(A, B, Dx, EPS))
    file_print.write("x\t\tFx\tS\n")
    for i in final_list:
        file_print.write('{:.5f}\t{:.5f}\t{:.5f}\n'.format(i[0], i[1], i[2]))
