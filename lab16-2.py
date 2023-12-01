import math


def formula(a, b):
    if a > 0.444:
        return math.log10(a) - math.sin(b) + 0.444
    elif a < -0.444:
        return math.exp(0.444 * a) + math.cos( b)
    else:
        return 0.444 * math.log(abs(b))


print("%.4f" % formula(a=1, b=0.5))
print("%.4f" % formula(a=-1, b=2.3))
print("%.4f" % formula(a=0, b=9.5))
