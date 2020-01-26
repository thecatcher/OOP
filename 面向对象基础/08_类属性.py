class Tool:
    count = 0
    def __init__(self,name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")
tool2 = Tool("锤子")

tool2.count = 99
print(tool2.count)
print(Tool.count)
