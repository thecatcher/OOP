class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地%.2f"%(self.name,self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f [剩余%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_items(self):
        print("添加家具：%s" % self.name)


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bed)
print(chest)
print(table)

my_house = House("两室一厅",60)
print(my_house)
