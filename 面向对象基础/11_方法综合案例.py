class Game:
    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息:自己慢慢玩~")

    @classmethod
    def show_top_score(cls):
        print("the top score is %d"% cls.top_score)

    def start_game(self):
        print("%s game started!" % self.player_name)


#1. 查看游戏的帮助信息

Game.show_help()

#2. 查看历史最高分

Game.show_top_score()

#3.创建游戏对象

xiaoming = Game("xiaoming")
xiaoming.start_game()
