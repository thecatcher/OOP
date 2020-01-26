class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count = self.bullet_count + count

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <= 0:
            print("%s 木有子弹了..." % self.model)
            return
        self.bullet_count = self.bullet_count - 1
        print("%s biu~biu~biu [%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("还木有枪")
            return
        if self.gun.bullet_count <=0:
            self.gun.add_bullet("50")
        self.gun.shoot()


ak47 = Gun("ak47")

ak47.add_bullet(50)

ak47.shoot()

xusanduo = Soldier("xusanduo")

# xusanduo.gun = ak47

xusanduo.fire()
