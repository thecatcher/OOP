class Man:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def run(self):
        print("%s like running" % self.name)
        self.weight = self.weight - 0.5

    def eat(self):
        print("%s like eating" % self.name)
        self.weight = self.weight + 1

    def __str__(self):
        return "I am %s and the weight is %.2f" % (self.name, self.weight)


xiaomei = Man("xiaomei", 45)

print(xiaomei)
xiaomei.run()

xiaomei.eat()

print(xiaomei)
