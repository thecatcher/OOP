class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地%.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f [剩余%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_items(self, item):
        print("添加家具：%s" % item)
        # 判断剩余空间是否足够
        if self.free_area < item.area:
            print("%s 的面积太大了，放不下啊" % item.name)
        # 添加家具
        self.item_list.append(item.name)
        # 重新计算剩余面积
        self.free_area = self.free_area - item.area


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

my_house = House("两室一厅", 60)

my_house.add_items(bed)

print(my_house)
