f = (x for x in range(20, 30))


def gen1():
    for k in range(10):
        yield k


def gen2():
    for j in range(10, 20):
        yield j


def generator():
    yield from gen1()
    yield from gen2()
    yield from f


if __name__ == '__main__':
    for i in generator():
        print(i)
