def sum_number(num):
    if num ==1:
        return 1
    
    # 假设 sum_number 能够完成 num -1 的累加
    temp = sum_number(num - 1)
    
    # 函数内部的核心算法就是 两个数字的相加
    
    return num + temp

print(sum_number(5))