try:
    #提示用户输入一个整数 
    num = int(input("输入一个整数"))
    
    result = 8 / num
    1.
    print(result)
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s" %result)