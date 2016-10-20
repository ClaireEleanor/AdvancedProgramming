# using recursion, gets the factorial (n!) of a number
def factorial(num):
    if (num > 1):
        return num * factorial(num - 1)
    else:
        return 1

# given a string
def add_digits(str_num):
    try:
        return eval(str_num[0]) + add_digits(str_num[1::1])
    except IndexError:
        return eval(str_num[0])

print add_digits(str(factorial(215)))
