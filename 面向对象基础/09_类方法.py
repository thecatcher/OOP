class Tool:
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("Tool count is %d" % cls.count)

    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool("斧头")


Tool.show_tool_count()