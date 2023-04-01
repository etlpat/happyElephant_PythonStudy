"""
目录：
1.了解异常
2.异常的捕获方法
3.异常的传递
4.Python模块
5.Python包
6.安装第三方软件
"""










### 1.了解异常

# 异常:当检测到一个错误时，Python解释器就无法继续执行了，反而出现了一些错误提示，这就是所谓的“异常”，也就是我们常说的BUG

# 当用只读形式打开一个不存在的文档
# f = open('没有这个文件.txt', 'r')
# 下面是报错
# FileNotFoundError: [Errno 2] No such file or directory: '没有这个文件.txt'












### 2.异常的捕获方法


# 当我们遇到BUG,那么接下来有两种情况：
#   ① 整个程序因为一个BUG停止运行
#   ② 对BUG进行提醒，整个程序继续运行

# 显然再之前的学习中，我们的程序遇到BUG就会出现①这种情况，也就是整个程序直接崩溃。
# 但再真是工作中，我们肯定不能因为一个小的BUG就让整个程序全部崩溃，也就是我们希望的是达到②这日子情况。
# 那我们就需要使用到“捕获异常”

# 捕获异常的作用在于：提前假设某处会出现异常，提前做好准备，当真的出现异常时，有后续手段。



### 本节目录：
## (1)捕获异常  # try exception
## (2)捕获指定的异常  # except 异常的类型 as 变量名:
## (3)捕获多个异常  # except (异常类型1, 异常类型2, 异常类型3,...):
## (4)捕获所有异常并记录异常类型  # except Exception as 变量名:
## (5) else 没有异常时执行的代码
## (6) finally 无论如何都要执行的代码





## (1)捕获异常

# 语法如下：
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码

## except：英文：除...外


# try:
#     f = open("D:\Python\python项目\python_learn\测试文档\不存在的文件.txt", 'r', encoding='UTF-8')
# except:
#     print('文件不存在，我将以只写的模式打开该文件')
#     f = open("D:\Python\python项目\python_learn\测试文档\不存在的文件.txt", 'w', encoding='UTF-8')





## (2)捕获指定的异常

# 语法如下；
# try:
#     可能发生错误的代码
# except 异常的类型 as 变量名:      # 这里通过as对错误类型设定别名
#     如果出现异常执行的代码


# 异常分不同类型，下面列举一些错误的种类
# 1 / 0  # ZeroDivisionError 除零错误
# print(变量)  # NameError 变量名错误（未定义）
# open('某文件', 'r')  # FileNotFoundError 文件未找到


# try:
#     print(name)
# except NameError as e:
#     print(f'发生了错误：{e}')  # 发生了错误：name 'name' is not defined
#
# # 若try中代码错误类型不是NameError，则不可捕获异常，程序停止运行





## (3)捕获多个异常
# 当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写

# 语法如下：
# try:
#     可能发生错误的代码
# except (异常类型1, 异常类型2, 异常类型3,...):
#     如果出现异常执行的代码


# try:
#     print(name)
#     1 / 0
# except (NameError, ZeroDivisionError):
#     print(f'代码发生错误')





## (4)【常用】 捕获所有异常 并 记录异常类型

# 注意：仅写try,except本身就是捕获所有异常，但是不能记录异常类型
# 我们可以借助【Exception】来接收所有异常并记录异常类型

# 语法如下：
# try:
#     可能发生错误的代码
# except Exception as 变量名:
#     如果出现异常执行的代码

## Exception：英文  n.例外



# try:
#     1 / 0
# except Exception as e:
#     print(f'发生错误：{e}')  # 发生错误：division by zero


# try:
#     print(name)
# except Exception as e:
#     print(f'发生错误：{e}')  # 发生错误：name 'name' is not defined





## (5) else 没有异常时执行的代码
# else 与 try exception 搭配，表示如果没有异常要要执行的代码

# 语法如下：
# try:
#     ...
# except ... :
#     ...
# else:
#    如果未异常，执行的语句


# name = '张三'
# try:
#     print(name)
# except Exception as e:
#     print(f'发生错误：{e}')
# else:
#     print('未发生错误')





## (6) finally 无论如何都要执行的代码
# finally一般写在捕获异常的最后，时无论如何最后都要执行的代码

# 语法如下：
# try:
#     ...
# except ... :
#     ...
# else:
#     ...
# finally:
#    有没有异常，最后都会执行该代码


# try:
#     f = open('D:\Python\python项目\python_learn\测试文档\草稿.txt', 'r')
# except Exception as e:
#     print(f"发生错误:{e},将以只写的形式打开")
#     f = open('D:\Python\python项目\python_learn\测试文档\草稿.txt', 'w')
# else:
#     print('打开文件成功')
# finally:
#     f.close()













### 3.异常的传递

# 异常是具有传递性的
# 请看如下例子：

# def func01():
#     print("func01开始")
#     num = 1 / 0 # 这是一个异常
#     print("func01结束")
#
# def func02():
#     print("func02开始")
#     func01()
#     print("func02结束")
#
# def main():
#     try:
#         func02()
#     except Exception as e:
#         print(e)
#
# main()
#  # main函数的打印结果如下所示：
#  # func02开始
#  # func01开始
#  # division by zero


# 当函数func01中发生异常，并且没有捕获处理这个异常是，异常会传递到函数func02，
# 当func02也没有捕获处理这个异常是，main函数会捕获
# 以上就是异常的传递性

# 启示：由于异常具有传递性，如果我们想要捕获异常，并不需要深入到真正出现异常的那句话，只要函数之间有层级关系，我们就可以再高的层级对异常进行捕获即可













### 4.Python模块

## (0)模块的介绍
## (1)模块的导入
## (2)自定义模块



## (0)模块的介绍

# 什么是模块？
# Python模块(Module)，是一个Python文件，以.py结尾。模块能定义函数、类和变量，模块里也能包含可执行的代码。

# 模块作用：
# Python中有很多不同的模块，每一个模块都可以帮助我们快速实现一些功能，比如实现和时间相关的功能就可以使用time模块。
# 我们可以视为一个模块就是一个工具包，每一个工具包中都有各种不同的工具供我们使用，进而实现各种不同的功能。

# 简单来讲：
# 模块就是一个Python文件，里面有类、函数、变量等，我们可以导入模块去使用





## (1)模块的导入

# 模块导入语法：
# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
# 提示：（上面的中括号[]表示可选）（* 代表全部）
#   import 英文：进口、导入

# 常用组合形式如下：
# import 模块名
# from 模块名 import 类、变量、方法等
# from 模块名 import *
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名





### ① 直接导入模块
# # 语法如下
# import 模块名
# import 模块名1, 模块名2
#
# 模块名.功能名()   # 功能 -- 即模块中的全部类、函数、变量


# # 通过import导入py内置的time模块 （time.py这个代码文件）
# # 【注意】导入后ctrl点击模块名，可以进入模块的.py文件内部
# import time
# time.sleep(5)     # . 表示层级关系，说明sleep函数属于time模块





### ② 从模块中引入单个功能
# # 语法如下
# from 模块名 import 功能名
# 功能名()

# 注意：从这里可以看出，【import后面跟什么，引入的就是什么】。
#   ① 中import模块，即引入模块整体，所以使用功能需要【模块.功能()】
#   ② 中import功能，即直接引入功能，所以使用功能时【功能()】即可


# from time import sleep
# sleep(5)





### ③ 用*从模块中导入全部功能
# # 语法如下
# from 模块名 import *
# 功能名()


# from time import *
# sleep(5)





### ④ 用 as 对模块/功能定义别名

# # 语法如下
#
# # 定义模块别名
# import 模块名 as 别名
# 别名.功能名()
#
# # 定义功能别名
# from 模块名 import 功能 as 别名
# 别名()


# import time as t1
# t1.sleep(5)

# from time import sleep as s1
# s1(5)






## (2)自定义模块














### 5.Python包
### 6.安装第三方软件





























