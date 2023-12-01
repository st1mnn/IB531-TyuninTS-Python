def pos_add(a,b):
    return a+b

def foo(a):
    return a//11, a%11

def num_sum(a):
    try:
        a = abs(int(a))
        sum = 0
        for b in a:
            sum += int(b)
        return sum
    except ValueError:
        return "Это не целое число"


input_string = "15"
print(num_sum(input_string))

input_string = "asd"
print(num_sum(input_string))