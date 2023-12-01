import math


def formula(a, b):
    if abs(a * b) < 0.3456:
        return math.atan(0.3456 * b) - a * b
    elif abs(a * b) >= 0.3456 and a * b > 0:
        return math.log10(abs(a * b)) + math.sqrt(a * b)
    else:
        return math.sin(b) - math.cos(0.3456 * a * b)


print(formula(a=1, b=-0.2))
print(formula(a=2.5, b=1.5))
print(formula(a=1.5, b=-1.5))
