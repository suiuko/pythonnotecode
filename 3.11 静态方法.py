class Dog(object):
    
    @staticmethod
    def run():
        
        # 不访问实例属性/类属性
        print("小狗要跑")
        
Dog.run()