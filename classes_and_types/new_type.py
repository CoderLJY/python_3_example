class Robot:
    counter = 0

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        return "Hi, I am " + self.name


def Rob_init(self, name):
    self.name = name


Robot2 = type(
    "Robot2", (), {
        "counter": 0,
        "__init__": Rob_init,
        "sayHello": lambda self: "Hi, I am " + self.name
    })

x = Robot2("Marvin")
print(x.name)
print(x.sayHello())
y = Robot("Marvin")
print(y.name)
print(y.sayHello())
print(x.__dict__)
print(y.__dict__)