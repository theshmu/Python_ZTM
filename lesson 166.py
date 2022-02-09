from time import time


def how_long(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        temp = fn(*args, **kwargs)
        t2 = time()
        print(f'Calculation took {t2 - t1} seconds')
        return temp

    return wrapper


def fib(num):
    a = 0
    b = 1
    for index in range(num + 1):
        yield a
        temp = a
        a = b
        b = temp + b


for num in fib(10):
    print(num)
    