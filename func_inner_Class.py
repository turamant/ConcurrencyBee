def createClass(name):
    class Car:
        __slots__ = ['name']
        def __init__(self, _name):
            self.name = _name

        def __str__(self):
            return self.name

    return Car(name)


car = createClass("Toyota")
garage = []
for i in range(1, 10):
    garage.append(car)

print(garage[1])
