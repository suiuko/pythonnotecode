# 创建元组
info_tuple = ("zhangsan",18,1.75)

# 1. 取值和取索引
print(info_tuple[0])
print(info_tuple.index("zhangsan")) # 已经知道数据的内容，需要知道索引

# 2. 统计计数
print(info_tuple.count("zhangsan"))

# 统计元组中包含元素的个数
print(len(info_tuple))


