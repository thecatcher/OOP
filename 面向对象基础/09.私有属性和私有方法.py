class Woman:
    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s的年龄是%d"%(self.name,self.__age))


xiaofang = Woman("xiaofang")



# 千万别这么干

print(xiaofang._Woman__age)

xiaofang._Woman__secret()

