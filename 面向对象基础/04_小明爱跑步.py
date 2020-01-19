class Man:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def run(self):
        print("%s 是个爱跑步的好孩子"% self.name)
        self.weight = self.weight - 0.5

    def eat(self):
        print("%s 今天很懒 天气好冷，多吃点吧"% self.name)
        self.weight = self.weight + 1

    def __str__(self):
        return "我是%s 我的体重是 %.2f 公斤"%(self.name,self.weight)

    def __del__(self):
        print("啊 小明胖死了！")


xiaoming = Man("xiaoming", 75)

print(xiaoming)
xiaoming.run()
xiaoming.eat()


print(xiaoming)

del xiaoming

print("-"*50)
