class Dog(object):
    def __init__(self,name) -> None:
        
        self.name = name
    
    def game(self):
        print("%s playing" %self.name)
        
class XiaoTianDog(Dog):
    def game(self):
        print("%s playing on the sky" %self.name)
        
class Person(object):
    def __init__(self,name) -> None:
        self.name = name
    
    def game_with_dog(self,dog):
        print("%s and %s are playing very happy"%(self.name, dog.name))
        
        # 让狗玩耍
        dog.game()
        
# 1. 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")

# 2. 创建一个小明对象
xiaoming = Person("小明")

# 3. 让小明调用和狗玩的方法
xiaoming.game_with_dog(wangcai)
    