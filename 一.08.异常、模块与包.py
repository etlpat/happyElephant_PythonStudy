"""
目录：
1.了解异常
2.异常的捕获方法
3.异常的传递
4.Python模块
5.Python包
"""
import my_module_test1
import my_package_test1.my_module1
from my_package_test1 import my_module1

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

### ① 自定义模块的使用
### ② __name__ 变量以及 "__main__" 的作用
### ③ __all__ 变量（作用于 * 上）




### ① 自定义模块的使用

# Py中已经帮我们实现了很多模块，不过有时候我们需要一些个性化的模块，这里就可以通过自定义模块实现，也就是自己制作一个模块。
# 注意：每个Py文件都可以作为一个模块，模块的名字就是文件的名字，也就是说自定义模块名必须要符合标识符的命名规则


# # 实例演示：
# # 我们在 my_module_test1 文件中写了一个 add 函数
# import my_module_test1
# x = my_module_test1.add(1, 2)
# print(x)  # 3
# from my_module_test1 import add
# y = add(2, 3)
# print(y)  # 5


# 注意：若不慎调用了位于两个文件中的同名功能，后调用的功能会覆前面的功能








### ② __name__ 变量以及 "__main__" 的作用

# 我们首先要了解一个规则：
#   【当调用模块时，会把模块执行一遍】
#
# 若我们的模块中有输出结果的语句，在调用模块时，就会在主文件输出，这不是我们想要的。
# 若我们不想在导入时输出模块中的函数调用结果，就想要了解下面的内容：



## （1）__name__ 变量
#
# __name__变量相当于一个文件的运行属性，文件运行时被赋值：
# 当我们把某个文件当主文件运行时，文件中的__name__的值为【__main__】
# 当我们在导入模块语句中执行模块文件，模块中的__name__的值为【模块名】
#
## 【官方解释】：__name__是一个特殊变量，在Python中用来表示当前模块的名字。当Python文件被直接执行时，__name__变量会被赋值为"main"，而当Python文件被作为模块导入时，__name__变量会被赋值为该模块的名字。这个变量通常用于判断当前文件是被作为模块导入还是被直接执行，从而区分执行不同的代码逻辑。

# print(__name__)  # main




## （2）语句 if __name__ == '__main__'
# 以上语句是判断当前模块是否为主程序的条件语句，如果是主程序，则执行if下面的代码块，否则不执行。
# 该语句在模块中非常重要


# if __name__ == '__main__':
#     print('直接执行了该文件')
# # 上面这段代码，当在直接执行该模块，if条件为真；若引入模块时执行，if条件为假

# from my_module_test1 import add
# # 我们在模块中加入了【if __name__ == '__main__':】语句，所以引入模块时未执行模块中的函数调用语句








## ③ __all__ 变量（作用于 * 上）
# 如果一个模块文件中有__all__变量，当使用 from xxx import * 导入时，只能导入这个列表中的元素。
# __all__ 变量是一个【列表】，列表内容可以【以字符串的形式存放函数名、变量名】


# # 我们在模块中写入了 __all__ = ['add'] ；模块中有add和mul两个函数
# from my_module_test1 import *
# add(1, 2)  # 3
# mul(2, 3)  # 报错，因为__all__列表未包含'mul'













### 5.Python包

## (1) 自定义包
## (2) 安装第三方包






## (1) 自定义包

### ① 包的概念
### ② 自定义包



### ①包的概念

# 为什么要用包？
# 基于Python模块，我们可以在编写代码的时候，导入许多外部代码来丰富功能，
# 但如果模块太多了，会造成管理混乱，我们就需要用包来管理。

# 什么是包？
# 【从物理上看】：包就是一个文件夹，在该文件夹下包含了一个 __init__.py 文件，该文件夹可用于包含多个模块文件。
# 【从逻辑上看】：包的本质依然时模块
# 补充：__init__.py 是一个特殊的文件，只要这个文件存在于文件夹中，那么这个文件就是Python包

# 包的作用：
# 当我们的模块文件越来越多时，包可以帮助我们管理这些模块，
# 包的作用就是包含多个模块，但包的本质依然时模块。








### ② 自定义包

# 如何在Pycharm中创建 Python包？
#   右键项目名称，新建 Python软件包

# 自定义包中模块的使用，与普通模块的使用方法【完全一致】
#    唯一的不同点在于，需要用 . 表示层级关系
#    以及新增了导入模块的方法： from 包名 import [模块名 | *]




## （1）导入包中的模块
# from 包名 import 模块名
# 模块名.功能名()

# from my_package_test1 import my_module1
# my_module1.info_print1()




## （2）导入包中的模块：(用 . 表示层级关系)
# import 包名.模块名
# 包名.模块名.功能名()

# import my_package_test1.my_module1
# my_package_test1.my_module1.info_print1()  # 我是模块1的功能函数代码




## （3）导入单个功能
# from 包名.模块名 import 功能名
# 功能名()

## 从（2）（3）中可以看出，包中的模块与普通模块的用法区别在于：
##  普通用法中有层级关系，这里就要多加一层【包名.xxx】
##  普通用法中无层级关系，这里也无层级关系


# from my_package_test1.my_module1 import info_print1
# info_print1()  # 这里就如上所说，无层级关系




## （4）用 * 导入 __all__中指定模块
# 包中模块不能用 * 直接全部导入
# 必须在 __init__.py 中用 __all__ 包含指定的模块名，之后才能导入

# 语法：
# 首先在__init__中：__all__ = ['模块名1','模块名2',...]
# from 包名 import *
# 模块名.功能名()


## __all__ 中包含了 模块1、2
# from my_package_test1 import *
# my_module1.info_print1()
# my_module2.info_print2()










## (2) 安装第三方包

# 我们知道，包可以包含众多Python模块，而每个模块又内含许多的功能
# 所以，为我们认为，一个包，就是一堆同类型功能的集合体

# 在Py程序的生态中，又许多的第三方包(非官方)，可以极大的帮助我们提高开发效率，如：
# 科学计算中常用的：numpy包
# 数据分析中常用的：pandas包
# 大数据计算中常用的：pyspark、apache-flink包
# 图形可视化常用的：matplotlib、pyecharts
# 人工智能常用的：tensorflow
# 等



# 第三方安装包的【安装方法】

# # （1）通过 pip 命令安装
#
## 下载方法如下：
# ① 打开cmd
# ② 输入：pip install 包名称
#   下载国内镜像的包：pip install -i 网址 包名称



# # （2）通过pycharm安装
#
## 下载方法如下：
# 设置 -> 项目 -> Python解释器 -> "+"
# 输入包名称即可选择安装
#   下载镜像包的方法：右下角选项，输入【-i 网址】即可











