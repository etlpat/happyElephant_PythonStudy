"""
目录：
(1)闭包
(2)装饰器
(3)设计模式
(4)多线程
(5)网络编程
(6)正则表达式
(7)递归
"""




### (1)闭包

# # 闭包基础介绍：
# Python闭包指的是一个函数中包含了另外一个函数，并且内部函数可以引用外部函数中的变量或参数。
# 【在Python中，函数是一等公民，可以作为参数传递，也可以作为返回值返回，因此函数嵌套是很常见的】
# 闭包的作用是可以在函数外部访问函数内部的变量，但是这些变量是隐藏在闭包内部的，不会对外部造成影响。这种特性在函数式编程中非常有用，可以实现封装和信息隐藏。


# # 闭包如下：
# def outer(a):
#     def inner(b):  # inner是内部函数，又称【闭包】
#         return a + b
#     return inner
#
# f = outer(10)
# print(f(5))  # 输出15
#
# # 在上面的代码中，【outer函数返回了一个内部函数inner】，【并且内部函数引用了外部函数的参数a】。
# # 我们可以通过调用outer函数来得到一个闭包，然后使用闭包来计算a与另一个参数b的和。
# # 这样闭包，可以做到【变量a对于inner来说持续存在，但是对于outer外的代码是临时的】，达成无法从外部修改的目的
# # 需要注意的是，在使用闭包时要小心变量的作用域和生命周期，避免出现意外的结果。



# # nonlocal关键字
# # 语法：nonlocal 变量名
# # 若想在闭包内修改外部函数的变量，需要使用nonlocal关键字声明想要修改的外部变量，否则报错
#
# def outer(num1):
#     def inner(num2):
#         nonlocal num1  # nonlocal关键字，使闭包内可以修改外部函数变量
#         num1 += 5
#         return num1 + num2
#     return inner
#
# inner = outer(3)
# num = inner(5)
# print(num)  # 13



# # 案例：闭包实现ATM机
# 通过闭包实现ATM存取钱案例，使账户金额无法从外部修改（不把用户金额直接设置为全局变量）

# def account_money(money=0):
#     def atm(num, deposit = True):
#         nonlocal money
#         if deposit:
#             money += num
#             print(f'存款：+{num}，账户余额{money}')
#         else:
#             money -= num
#             print(f'取款：-{num}，账户余额{money}')
#     return atm
#
# atm = account_money(0)
# atm(1000)  # 存款：+1000，账户余额1000
# atm(500,deposit=False)  # 取款：-500，账户余额500



# 闭包优缺点：
# 优点：无需定义全局变量即可实现通过函数，执行的访问、修改某个值
#      闭包使用的变量的所用于在函数内，难以被错误的调用修改
# 缺点：由于内部函数持续引用外部函数的值，所以会导致这一部分内部空间不被释放，一直占用内存















### (2)装饰器

# 装饰器也是一种闭包，其功能就是在【不破坏目标函数原有的代码和功能的前提下，为目标函数添加新功能】


# # (1)装饰器的原理写法（不使用）：
# # 如下，我们要在sleep函数前后加上睡觉起床提示，这里使用装饰器封装为新函数
#
# def outer(func):
#     def inner():
#         print('我睡觉了')
#         func()
#         print('我起床了')
#     return inner
#
# def sleep():
#     import random, time
#     print('睡觉中...')
#     time.sleep(random.randint(1,5))  # 注意，这个randint(num1,num2)的区间是[num1,num2]，和其他的左闭右开不一样
#
# inner = outer(sleep)
# inner()



# # # 装饰器的真正写法【语法糖写法】
#
# def outer(func):
#     def inner():
#         print('我睡觉了')
#         func()
#         print('我起床了')
#     return inner
#
# @outer
# def sleep():
#     import random, time
#     print('睡觉中...')
#     time.sleep(random.randint(1,5))
#
# sleep()
#
# # 【@outer】的作用是：把sleep函数作为参数传递给outer，然后执行inner
# # 语法糖写法，本质上还是调用inner，但给人主观上的感受是sleep的功能增加了















### (3)设计模式
### (4)多线程
### (5)网络编程
### (6)正则表达式
### (7)递归








