from funcy import *


lis1 = [1,2,3,4,5,6,7]
lis2 = ["a", "d", "e"]

all = merge(lis1, lis2)
print(all)

def double(x):
    return x*2

z = take(4, iterate(double, 2))
print(z)

@decorator
def log(call):
    print(call._func.__name__, call._args)
    return call()


