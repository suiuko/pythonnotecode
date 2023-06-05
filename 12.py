# 字典的遍历 
xiaoming_dict = {"name": "xiaoming",
                 "qq":"1234",
                 "phone":"1000"}

# 变量K是 每次循环中，获取到的键值对的key

for k in xiaoming_dict:
    print("%s : %s" %(k,xiaoming_dict[k]))
    