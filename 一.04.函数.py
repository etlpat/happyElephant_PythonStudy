"""
目录：
1.函数介绍
2.函数的定义
3.函数的参数
4.函数的返回值
    知识拓展：None
5.函数说明文档
6.函数的嵌套调用
7.变量的作用域
    global关键字
8.综合案例
"""




## 1.函数介绍

# 函数：是组织好的，可重复使用的，用来实现特定功能的代码块。
# 如库函数 len()，可以随时随地直接使用来求长度
# 函数特点： 1.已组织好的 2.可重复使用 3.针对特定功能


# # 如下面用函数实现len()
# def my_len(data):
#     count = 0
#     for i in data:
#         count += 1
#     return count
#
# str = "114515"
# print(my_len(str)) # 6


# 我们写函数，是为了得到一个针对特定需求，可供重复利用的代码段
# 提高程序的复用性，减少重复的代码，提高开发效率








## 2.函数的定义

## 定义一个函数：
#
# def 函数名(传入参数):
#     函数体
#     return 返回值

# 注：不写return语句，则默认返回None


## 调用函数：
# 函数名(参数)



# def say_hi():
#     print("hi")
#
# say_hi() # hi








## 3.函数的参数

# 传入参数的功能是：在函数进行计算时，接受外部(调用时)提供的数据

# def 函数名(形式参数):
#     函数体
#     return 返回值
#
# 函数名(实际参数)

# 参数可以有任意的



# def add(a, b):
#     return a + b
#
# print(add(3,2), add(9,8)) # 5 17








## 4.函数的返回值

# 注意点：
# 1.return 语句是函数的结束标志，不会执行return后的代码
# 2.函数的返回值可将函数的结果返回给函数的调用者
# 3.不写return语句，则默认返回None(空类型，<class 'NoneType'>)



# def add(a, b):
#     return a + b
#
# x = add(5, 6)
# print(x) # 11


# def say_hi():
#     print("hi")
#
# x = say_hi()
# print(x)  # None
# print(type(x)) # <class 'NoneType'>



### 知识拓展：None
# None,是类型为NoneType的字面量
# 用于表示空的、无意义的


## None的应用场景：
#
# 1.用在函数无返回值上
#
# 2.用在if判断上：None等同于False
#   一般用于函数中主动返回None，配合if做相关处理
#
# 3.用于声明无内容的变量上
#   定义变量，但暂时不需要变量有具体值，可以用None代替



# # 代码实现提示未成年
# def check_age(age):
#     if age >= 18:
#         return "SUCCESS" # 注意，if语句中字符串算非0
#     else:
#         return None
#
# if not check_age(int(input("请输入年龄："))):
#     print("您未成年，不可进入")








## 5.函数说明文档

# # 语法如下：(下面的注释框架，在函数内打印三引号，编译器就会自动给出)
#
# def func(x, y):
#     """
#     #函数说明
#     :param x: 形参x的说明
#     :param y: 形参y的说明
#     :return: 返回值的说明
#     """
#     函数体
#     return 返回值
#
# 之后调用函数时，把鼠标悬停在函数名上，就会弹出你编写的函数说明



# def add(a, b):
#     """
#     两数相加函数
#     :param a: 一个形参数字
#     :param b: 另一个形参数字
#     :return: a+b的结果
#     """
#     return a+b
#
# add(5,6)








## 6.函数的嵌套调用

# 格式如下(b中嵌套a)
#
# def func_a():
#     #函数体
#     #return 返回值
#
# def func_b():
#     #函数体
#     func_a()
#     #return 返回值



# def pri1():
#     print("114514")
#
# def pri2():
#     pri1()
#     print("1919810")
#
# pri2()








## 7.变量的作用域

# 变量按作用域可分为两类：局部变量和全局变量
# 如函数内定义的变量，就是局部变量，在函数内被创建，出函数被销毁



# def f():
#     num = 100
#
# print(num)
# # 报错：NameError: name 'num' is not defined. Did you mean: 'sum'?
#
# 上面num就是局部变量


# 在函数外定义的变量即全局变量，在全局可以使用



### 补充：global关键字

# num = 100
#
# def f():
#     num = 200
#     print(num)
#
# f()  # 200
# print(num)  # 100
#
# 如上我们可以发现函数内num被赋为200，并不影响全局变量num的值
# 函数内的变量都是局部变量



## 若想在函数内使用全局变量，须使用【global关键字】
# global关键字 可以在函数内部声明变量为全局变量
# 如有全局变量a，在函数内 global a，即把全局变量a引入函数中

# num = 100
#
# def f():
#     # global 关键字声明num为全局变量
#     global num
#     num = 200
#     print(num)
#
# f()  # 200
# print(num)  # 200








## 8.综合案例



# # 案例(1)
#ATM程序
# 定义一个全局变量:money,用来记录银行卡余额(默认5000000)
# 定义一个全局变量:name,用来记录客户姓名(启动程序时输入)
# 定义如下函数
#    查询余额函数
#    存款函数
#    取款函数
#    主菜单函数
# 要求：
# 程序启动后要求输入客户姓名
# 查询余额、存款、取款后都会返回主菜单
# 存款、取款后，都应显示一些当前余额
# 客户只有选择退出或输入错误，程序会退掉，否则程序会一直运行



# # 定义全局变量
# name = input("请输入您的姓名：")
# money = 5000000
#
# # 打印菜单函数
# def menu():
#     print("--------------主菜单--------------")
#     print(f"{name}，您好，欢迎来到ATM。请选择操作：")
#     print("查询余额\t【输入1】")
#     print("存款\t\t【输入2】")
#     print("取款\t\t【输入3】")
#     print("退出\t\t【输入4】")
#
#
# def query(flag):
#     if flag:
#         print("--------------查询余额--------------")
#     print(f"{name}，您好，您的余额剩余：{money}")
#
#
# def saving(num):
#     print("--------------存款--------------")
#     global money
#     money += num
#     print(f"{name}，您好，{num}元存储成功")
#     query(False)
#
#
# def geting(num):
#     print("--------------取款--------------")
#     global money
#     money -= num
#     print(f"{name}，您好，{num}元取款成功")
#     query(False)
#
#
# while True:
#     menu()
#     num = int(input("请输入您要进行的业务："))
#     if num == 1:
#         query(True)
#     elif num == 2:
#         int(input("请输入存款的金额："))
#         saving(num)
#     elif num == 3:
#         int(input("请输入取款的金额："))
#         geting(num)
#     elif num == 4:
#         break
#     else:
#         print("暂无此业务，请重新输入")
#     input()
# print("程序已退出")



# # 案例(2)
# 用函数计算并输出斐波那契数列中小于参数n的所有值，并调用该函数进行测试
#
# def fbnq(n):
#     a, b = 1, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#
# fbnq(100)  # 1 1 2 3 5 8 13 21 34 55 89



# # 案例(3)
# 使用递归，实现整数的因式分解
# 在每次递归中，找到num最小的因数做商，对商进行递归，返回一个因数列表
#
# def f(num: int):
#     num_list = []
#     for i in range(2, int(num)):
#         if num % i == 0:
#             num_list.append(int(i))
#             return num_list + f(num//i)  # 若能遍历到因数+递归的下一级列表
#     num_list.append(int(num))
#     return num_list  # 若无因数，返回存放自身的列表
#
# n = int(input('请输入一个整数：'))
# n_list= f(n)
# print(n_list)







