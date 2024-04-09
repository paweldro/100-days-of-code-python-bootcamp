def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def test(**kwargs):
    print(kwargs)

def test_2(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)

def multiply(n, **kwargs):
    n *= kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

class Car_2:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model") #None

print(add(5, 6, 7))

test(add=3, multiply=5)
test_2(add=3, multiply=5)
multiply(2, add=3, multiply=5)

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
my_car_2 = Car_2(make="Fiat")
print(my_car_2.model)