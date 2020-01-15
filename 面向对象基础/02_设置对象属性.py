class Cat:
    def eat(self):
        print("%s 爱吃鱼"%self.name)

    def drink(self):
        print("小猫爱喝水")


tom = Cat()

tom.name = "Tom"
tom.eat()


lazy_cat = Cat()

lazy_cat.name = "lazy cat"
lazy_cat.eat()




