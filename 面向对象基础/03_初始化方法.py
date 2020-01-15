class Cat:
    def __init__(self):
        self.name = "Tom"
        print("this is a init function")

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name)

# tom = Cat()
# tom.eat()

lazy_cat = Cat("lazy")
lazy_cat.eat()