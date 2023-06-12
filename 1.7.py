# 列表的数据统计

name_list = ["zhangsan","lisi","wangwu","wangxiaoer"]

# len(length 长度) 函数 可以统计列表中元素的总数

list_len = len(name_list)
print("列表中包含 %d 个元素" % list_len)

# count 方法可以统计列表中某一个元素出现的次数
count = name_list.count("zhangsan")
print("zhangsan 出现了 %d 次" %count)

# remove 删除元素，多个的话删除左边第一个
name_list.remove("wangwu")