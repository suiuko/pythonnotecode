class Animal:
    def eat(self):
        print("吃")
        
    def drnk(self):
        print("喝")
        
    def run(self):
        print("跑")
        
    def sleep(self):
        print("睡觉")
        
class Dog:
    pass

# 创建一个对象 --- 狗对象

wangcai = Animal()
wangcai.eat()
wangcai.drnk()
wangcai.run()
wangcai.sleep()
