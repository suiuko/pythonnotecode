name_list = ["zhangsan","lisi","wangwu"]

# 1. 取值和索引
print(name_list[2])

#知道数据内容，想知道数据在列表中的位置
print(name_list.index("lisi"))

# 2. 修改

name_list[1] = "李四"
print(name_list)

# 3. 增加

# append 在列表末尾添加数据
name_list.append("王小二")

# insert 方法在列表的置顶索引位置插入数据
name_list.insert(1,"小明")

# extend 插入整个列表
temp_list = ["孙悟空","猪八戒"]
name_list.extend(temp_list)

print(name_list)
# 4. 删除

# remove 删除指定数据
name_list.remove("wangwu")

# pop 默认把列表最后一个元素删了
name_list.pop()
# pop 可以删指定索引
name_list.pop(4)

# clear 清空列表
name_list.clear()

# delete 本质上是用来将一个变量从内存中删除的

del name_list[1]

name = "小明"
del name # 如果使用del 关键词将变量从内存中删除，后续就不能使用此变量
print(name_list)