# 打印多行

def print_line(char,times):
    print(char * times)
    
def print_lines(char,times,row1):
    """
    
    :param char: 分割线使用的分隔字符
    :param times: 分割线重复的次数
    """
    row = 0
    while row < row1:
        print_line(char,times)
        row +=1

print_lines("-",20,5)