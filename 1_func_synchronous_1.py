import time


def fun1(x):
    print(x**2)
    time.sleep(3)
    print('fun1 завершена')


def fun2(x):
    print(x**0.5)
    time.sleep(3)
    print('fun2 завершена')


def main():
    print(time.strftime('%X'))
    fun1(4)
    fun2(4)
    print(time.strftime('%X'))


main()
print(type(fun2))
print(type(fun2(3)))
