"""
目录：
1.while循环的基础语法
2.while循环的基础案例
3.while循环的嵌套应用
4.while循环的嵌套案例
5.for循环的基础语法
6.for循环的嵌套调用
7.循环终端：break和continue
8.综合案例
"""





# 1.while循环的基础语法

# 格式如下

# while 条件:
#     执行语句
#     ...

# 条件为布尔类型，条件为真，执行循环
# 以四格缩进划分代码块


# # 例子：1~100求和
# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)  # 5050










# 2.while循环的基础案例

# 猜数字，1~100中生成一个随机整数，来猜猜输入数字是否等于随机数


# # 法1
# import random
# num = random.randint(1,100)
# count = 0
# guess = int(input("请输入猜测的数字:"))
# while guess != num:
#     if num > guess:
#         print("小了")
#     else:
#         print("大了")
#     guess = int(input("请输入猜测的数字:"))
#     count += 1
# print(f"猜中了！数字是{num},猜了{count}次")


# # 法2
# import random
# num = random.randint(1,100)
# count = 0
# flag = True
# while flag:
#     guess = int(input("请输入猜测的数字:"))
#     count += 1
#     if guess == num:
#         print("猜中了！")
#         flag = False
#     else:
#         if guess > num:
#             print("猜大了")
#         else:
#             print("猜小了")
# print(f"猜中了！数字是{num},猜了{count}次")










# 3.while循环的嵌套应用


# while 条件1:
#     执行语句1
#     ...
#     while 条件2:
#         执行语句2
#         ...





# 4.while循环的嵌套案例


# # 知识点补充【1】：如何让print()语句输出不换行功能 ?
# # print()语句输出内容会自动换行，若想输出不换行，需要在语句末尾加上end=空字符串 (即 ,end='')
#
# print("你好呀", end='') # 这样不会自动换行
#
# # print()语句原本结尾默认end='\n'，现在我们手动改为end=''，就不会换行


# 知识点补充： '\t'
# 水平制表符能让\t，能让单词、数字对齐到4的整数倍上
# 在单词/数字长度差不多时，可用'\t'实现单词的对齐


# # 打印九九乘法表
#
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i}={i*j}\t", end = "")  # 通过\t制表符进行对齐；通过end=""取消print的自动换行
#         j += 1
#     print('')
#     i += 1










# 5.for循环的基础语法


## (1) 基础语法
# while和for的[区别]
# while循环的循环条件是自定义的，自行控制循环条件
# for循环是一种【"轮询"】机制，是对一批内容进行【"逐个处理"】


# 格式如下：
# for 变量名 in 序列类型
#     执行语句
#     ...

# 将待处理数据集中数据挨个取出，每次循环就当次数据赋予前面的变量
# 序列类型：字符串、列表、元组等


# num = "1145141919810"
# for x in num: # 将num的内容逐个取出并赋予x
#     print(x)
#     print(type(x)) # <class 'str'>
# print(x) # 0
#
# # 上面代码可看出 1.字符串中取出的单个字符也是str类型 2.变量x的值在出循环后保持最后一次的值


# # 统计下面字符串中有多少"1"
# num = "1145141919810"
# count = 0
# for x in num: # 将num的内容逐个取出并赋予x
#    if x == '1':
#        count += 1
# print(count)
#
# # 上面代码可看出 1.字符串中取出的单个字符也是str类型 2.变量x的值在出循环后保持最后一次的值


## (2)range语句

# range语句，可以生成一个简单的数字序列
# 注意：range() 生成数字的范围【左闭右开】
#      num1不写，默认为0 ；步长不写，默认为1


# 语法1
# range(num)
# 获得一个从01开始，到num结束的数字序列 (不含num本身)
# 如 range(5) 取得的数据是:[0,1,2,3,4]

# 语法2
# range(num1, num2)
# 获得一个从num1开始，到num2结束的数字序列 (不含num2本身)
# 如 range(5,10) 得的数据是:[5，6，7，8，9]

# 语法3
# range(num1, num2, step)
# 获得一个从num1开始，到num2结束的数字序列 (不含num2本身)
# 数字之间的步长，以step为准 (不写默认为1)
# 如 range(5,10,2) 取得的数据是:[5,7,9]


# for x in range(10):
#     print(x,end=' ')
# # 打印结果为: 0 1 2 3 4 5 6 7 8 9

# for x in range(5,10):
#     print(x,end=' ')
# # 打印结果为: 5 6 7 8 9

# for x in range(5,10,2):
#     print(x,end=' ')
# # 打印结果为: 5 7 9


## (3)变量作用域

# # 如下例子
# for i in range(5):
#     print(i)
# print(i) # 输出4
#
# # 规范上：不允许
# # 实际上：可以

# 编程规范上来看，变量的作用域只限定在for循环内部
# 如果在for外部，也是可以访问到临时变量的，但不建议这么做
# 若真想在循环外部使用循环变量，可以在for外边在定义一次同名变量








# 6.for循环的嵌套调用

# for 变量名1 in 序列类型1
#     执行语句1
#     ...
#     for 变量名2 in 序列类型2
#         执行语句2
#         ...


# # 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}*{i}={j * i}', end='\t')
#     print()










# 7.循环终端：break和continue

# continue关键字用于：中断本次循环，直接进入下一次循环
# continue可用于：for循环和while循环中


# for i in range(1,11):
#     if i == 6:
#         continue
#     print(i,end = ' ')
#
# # 1 2 3 4 5 7 8 9 10 显然结果把6跳过了



# break关键字用于：直接结束循环
# break可以用于：for循环和while循环中


# for i in range(1,11):
#     if i == 6:
#         break
#     print(i,end = ' ')
#
# # 1 2 3 4 5  当变量等于6时结束循环










# 8.综合案例

# 某1公司，账户余额有10000元，给20名员工发工资
# 员工编号1到20，从编号1开始，一次领取工作，每人1000元
# 领工资时，判断绩效分（1到10随机生成），低于5，不发工资
# 若工资发完，结束发工资

# import random
# money = 10000
# for i in range(1,21):
#     count = random.randint(1,10) # 生成 1~10 的员工绩效分
#
#     if count < 5:
#         print(f"员工{i}绩效分{count},不满足，不发工资")
#         continue
#     if money != 0:
#         print(f"员工{i}绩效分{count},满足，发1000工资，工资账户余额{money}")
#         money -= 1000
#     else:
#         print(f"员工{i}绩效分{count},满足，工资账户余额{money},下月补发")
