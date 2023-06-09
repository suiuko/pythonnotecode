def demo(num):
    print("函数内部代码")
    
    # 函数内部，不会修改到外部的实参变量
    num =100
    print(num)
    print("函数执行完成")
    
gl_num = 99

demo(gl_num)
print(gl_num)