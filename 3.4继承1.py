class Animal:
    def eat(self):
        print("吃")
        
    def drnk(self):
        print("喝")
        
    def run(self):
        print("跑")
        
    def sleep(self):
        print("睡觉")
        
class Dog(Animal):
    
    def bark(self):
        print("汪汪叫")

class XTQ(Dog):
    
    def fly(self):
        print("我会飞")


# # 创建一个对象 --- 狗对象

# wangcai = Animal()
# wangcai.eat()
# wangcai.drnk()
# wangcai.run()
# wangcai.sleep()

# 创建一个啸天犬的对象
xtq = XTQ()
xtq.fly()
xtq.bark()
xtq.eat()