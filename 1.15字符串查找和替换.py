
hello_str = "hello,world"

# 1. 判断是否以特定字符串开始

print(hello_str.startswith("hello"))

# 2. 判断是否以特定字符串结束

print(hello_str.endswith("world"))

# 3. 查找指定字符串
# index同样可以查找指定的字符串在打字符串中的索引
print(hello_str.find("llo"))   #输出2，字符串不存在会报错
print(hello_str.index("llo"))  # 字符串不存在会输出-1

# 4. 替换字符串
# replace 执行完成后 会返回一个新的字符串
# 注意： 不会修改原有字符串的内容
print(hello_str.replace("world","python"))
print(hello_str)

