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

    def bark(self):
        print("叫得跟神一样")
        
        

# 创建一个啸天犬的对象
xtq = XTQ()
# xtq.fly()

# 如果子类中，重写了父类的方法
# 在使用子类对象调用方法，会调用子类中重写的方法

xtq.bark()
# xtq.eat()