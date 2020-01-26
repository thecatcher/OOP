class Animal:
    def eat(self):
        print("eat")

    def run(self):
        print("run")

    def drink(self):
        print("drink")

    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("wangwangwang")


class Xiaotian(Dog):
    def fly(self):
        print("fly...")

    def bark(self):
        Dog.bark(self)
        super(Xiaotian, self).bark()

        print("hahahah wu wu wu wang wang wang")

    def eat(self):
        print("-" * 50)
        super(Xiaotian, self).eat()
        print("老子是神犬")


wangcai = Dog()

wangcai.bark()
wangcai.eat()

xiaotianquan = Xiaotian()

xiaotianquan.eat()
xiaotianquan.bark()
xiaotianquan.fly()
