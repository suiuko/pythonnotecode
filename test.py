

# 将数字类型转换成字符串

num_str = str(11) 
print(type(num_str),num_str)

float_str = str(11.333)
print(type(float_str), float_str)

# 将字符串转换为数字

num = int("11")
print(type(num),num)

num2=float("11.333")

print(type(num2),num2)

# 整数转浮点数

float_num = float(11)
print(type(float_num),float_num)

# 浮点数转整数
int_num = int(11.333)
print(type(int_num),int_num)

# 算数（数学）运算符
print(" 1 + 1 =",1 + 1)
print(" 1 - 1 =",1 - 1)
print(" 2 * 1 =",2 * 1)
print(" 4 / 2 =",4 / 2)
print(" 11 // 2 =",11 // 2)
print(" 9 % 2 =",9 % 2)

## 字符串拼接

name = "X"
print("my name is "+ name)

## 字符串格式化

name = "你好"
message= "你到了么？%s" % name
print(message)
class1 =11
message1="hello,我是%s,我的班级是%s" % (name, class1)
print(message1)

# 数字精度控制

num1 = 11
num2 = 11.345
print("数字11宽度为5，结果为 %5d" % num1)

# 快速格式化

name1 = "你好"
set_up_year = 2000
stock_price = 1
print(f"我是{name1}，我成立于{set_up_year},我有{stock_price}元钱")

# 表达式格式化

print("1 * 1的结果是：%d" %(1 * 1))
print(f"1 * 1的结果是：{1 * 1}")
print("字符串在python的类型是： %s" % type('字符串'))



# 练习： 股价计算小程序
"""
定义如下变量：
name2
stock_price 当前股价
stock_code 股票代码
stock_pirce_daily_growth_factor 股票每日正常系数，浮点类型
growth_days 增长天数
计算经过growth_days天的增长后，股价达到了多少钱
"""
# 定义变量

name2 = "小新的股票"
stock_price = 19.99
stock_code = "00001"
stock_price_daily_growth_factor = 1.2
growth_days = 7

finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days

print("公司:{name2}, 股票代码:{stock_code},当前股价:{stock_price}")
print("每日增长系数:%.1f,经过%d天的增长后,股价达到了:%.2f" %(stock_price_daily_growth_factor
,growth_days,finally_stock_price))


# input语句
print("请告诉我你是谁？")
name = input()
print("我知道了，你是%s" % name)

# input 升级版

name3 = input("tell me your name")
print("get! you are %s" % name3)

# bool类型

bool1 = True
bool2 = False
print(f"bool1的变量内容是：{bool1},类型是{type(bool1)}")
print(f"bool2的变量内容是：{bool2},类型是{type(bool2)}")

# if
age1 = 18
print(f"今年我已经{age1}岁")
if age1 >= 18:
    print("我已经成年了")
    print("即将步入大学生活")
print("时间很快啊")

age2 = 30
if age2 >= 18:
    print("我已经成年了")
print("结束")

# if练习，成年人判断
"""
结合之前的input语句 完成以下任务

1. input 获取age值
2. 通过if判断是否是成年人，满足条件则输出提示信息
"""
# 定义变量
age3 = int(input("请输入你的年龄"))

#判断是否是成年人

if age3>= 18:
    print("成年，需要 10元")
print("未成年，祝您游玩愉快")


# if - else条件

age4 = int(input("请输入你的年龄："))
if age4 >=18:
    print("您已经成年，需要买10元")
else:
    print("您未成年，可以免费玩")


# if elif else

height = int(input("请输入你的身高CM:"))
vip_level = int(input("请输入你的VIP等级"))
day = int(input("请输入今天的日期"))

# 以上的变量可以不用通过变量来写 可以直接写入表达式中
# 通过if来进行判断
if height < 120:
    print("身高小于120，可以免费")
elif vip_level > 3:
    print("VIP等级大于3可以免费")
elif day == 1:
    print("今天1号免费")
else:
    print("不好意思，条件都不满足，需要买票10元")


# 练习： 猜猜心里数字
"""
定义一个变量，数字类型，内容随意
基于input语句输入猜想的数字，通过if和多次elif的组合
判断猜想的是否和心理想的一致
"""

# 定义 数字 num 

num_guess = 5
if int(input("猜一个数字")) == num:
    print("恭喜你第一次就猜对了")
elif int(input("猜错了再来一次")) == num:
    print("猜对了")
elif int(input("猜错了再来一次")) == num:
    print("恭喜，最后一次机会，你猜对了")
else:
    print("sorry 你猜错了")


"""
判断语句的嵌套使用

"""

if int(input("你的身高是多少 ")) > 120:
    print("身高超出限制，不可以免费")
    print("但是，如果VIP大于3，可以免费")

    if(int(input("你的VIP等级是多少"))) > 3:
        print("恭喜您VIP达标，可以免费")
    else:
        print("sorry，你需要买票")
else:
    print("欢迎小朋友，免费游玩")


# 练习2
"""
必须是大雨等于18岁小于30岁的成年人
同时入职时间需满足大于两年，或者级别大于3才可以领取
"""
age5 = 20
year1 = 3
level1 =1
if age5 >= 18:
    print("you are adult")
    if age5 < 30:
        print("你的年龄达标了")
        if year1 > 2:
            print("恭喜您，年龄和入职时间都达标，可以领取礼物")
        elif level1 > 3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和等级都不达标")
    else:
        print("不好意思，您的年龄太大")
else:
    print("不好意思，小朋友不可以领取")   


"""
案例要求：
定义一下数字，随机产生，通过第三次判断来猜出这个数字
数字为1-10
三次猜测数字
每次猜不中，会提示大了或者小了

提示： 以下会产生一个随机数字
import random
num = random.randint(1,10)
"""
# 1.构建一个随机的数字
import random
num = random.randint(1,10)

gress_num = int(input("输入你要猜测的数字"))

# 2.通过if判断语句进行数字的猜测
if gress_num == num:
    print("恭喜，猜中了")
else:
    if gress_num > num:
        print("你猜大了")
    else:
        print("你猜小了")
    gress_num = int(input("输入你要猜测的数字"))
    if gress_num == num:
        print("恭喜，猜中了")
    else:
        if gress_num > num:
            print("你猜大了")
        else:
            print("你猜小了")

        gress_num = int(input("输入你要猜测的数字"))
        if gress_num == num:
            print("恭喜，猜中了")
        else:
            if gress_num > num:
                print("你猜大了")
            else:
                print("你猜小了")
    

"""
石头剪刀布
目标：
1. 强化多个条件的逻辑运算
2. 体会 `import` 倒入模版

需求：
1. 从控制台输入要出的拳
2. 电脑随机出圈
3. 出胜负
"""
import random
player = int(input("请输入您要出的拳 石头1/剪刀2/布3"))

# 电脑随机出
computer = random.randint(1,3)
print("玩家选择的拳头是 %d - 电脑出拳是 %d  " % (player,computer))

# 比较胜负
# 规则： 1. 石头V 剪刀  2. 剪刀V 布 3. 布V石头

if (player == 1 and computer ==2) or (player == 2 and computer ==3 ) or (player == 3 and computer ==1):
    print("电脑弱爆了！")
elif player == computer:
    print("平手")
else:
    print("玩家输了")
