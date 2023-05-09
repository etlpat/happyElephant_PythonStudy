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

# 设计模式使一种编程套路，可以极大的方便程序的开发
# 最常见、最经典的设计模式，就是我们所学习的面向对象了

# 除了面向对象外，在编程中也有很多既定的套路可以方便开发，我们称之为设计模式
# ·单例、工厂模式
# ·建造者、责任链、状态、备忘录、解释器、访问者、观察者、中介、模板、代理模式
# ·等等模式



## ① 单例模式

# 基础介绍：
# 正常情况下，创建类的实例后，当我们获取多个对象，每个对象都拥有不同的地址。
# 某些时候，我们需要一个类无论获取多少次类对象，都仅仅提供一个具体的实例（地址相同），就叫做【单例模式】
# 单例模式：用以节省创建类对象的开销和内存开销，如某些工具类，仅需要一个实例，即可在各处使用

# 单例模式(Singleton Pattern)，是一种常用的软件设计模式，该模式的主要目的是确保一个类只有一个实例存在
# 定义：单例模式的基本思想是在一个应用程序中只创建一个唯一的对象实例，并提供全局访问该实例的方法。这个实例通常被称为“单例”（Singleton）。
# 使用场景：当一个类只能有一个实例，而客户可以从一个众所周知的访问典访问它时

# # 单例模式的实现：
#
# # ①在一个文件中定义如下代码：
# class Tool:
#     pass
# my_tool = Tool()
#
# # ②在另一个文件中导入对象
# for test import my_tool
# t1 = my_tool()
# t2 = my_tool()
#
# # 由于我们在下面文件中直接导入了创建好的对象，使用肯定是同一个地址





## ② 工厂模式

# 工厂模式概念：
# 当需要大量创建一个类的实例的时候，可以使用工厂模式。
# 工厂模式（Factory Pattern）是一种创建型设计模式，它定义了一个工厂接口，使得客户端可以通过调用工厂方法创建对象，而无需知道对象的具体实现细节。
# 优点：大批量创建对象是有统一的入口，便于代码的维护，当发生修改，仅修改工厂类的创建方法即可
#      符合现实世界的模式，即工厂生产产品

# # 工厂模式的实现：
# class Person:
#     pass
# class Worker(Person):
#     pass
# class Student(Person):
#     pass
# class Teacher(Person):
#     pass
#
# class PersonFactory:
#     def get_person(self, p_type):
#         if p_type == 's':
#             return Student()
#         elif p_type == 't':
#             return Teacher()
#         else:
#             return Worker()
#
# factory = PersonFactory()
# s1 = factory.get_person('s')
# t1 = factory.get_person('t')
# w1 = factory.get_person('w')















### (4)多线程

# # 进程和线程：
# 现代操作系统，如MacOS、UNIX、Linux、Windows等，都是支持“多任务”的操作系统
# 进程：就是一个程序，运行在系统之上，那么便称这个程序为一个运行进程，并分配进程ID方便系统管理
# 线程：线程是归属于进程的，一个进程可以开启多个线程，执行不同的工作。进程是进程的实际工作最小单位
#
# 注意：进程之间是内存隔离的，不同进程拥有各自的内存空间
#      线程之间是内存共享的。线程属于进程，一个进程内的多个线程之间是共享这个进程所拥有的内存空间

# 并行执行：
# 进程之间就是并行执行的，操作系统库同时运行好多程序，这些程序都是在并行执行。
# 除了进程外，线程也可以并行执行。
# 比如一个python程序，其实完全可以做到：
# 一个线程在输出：hello
# 一个线程在输出：hi
# 像这样一个程序在统一时间做两件乃至多件不同是事情，我们就称之为：多线程并行执行



# threading模块
# thread  英文： n.线、线程、多线程
# python的多线程可以通过threading模块来实现
# 步骤：①导入threading模块 ②创建Thread线程对象 ③用对象方法start线程

# # 语法如下：
# import threading
#
# # 创建线程对象
# thread_obj = threading.Thread()
# # Thread的参数列表如下：
# # -group：暂时无用，未来功能的预留参数
# # -target：执行目标的任务名【传递函数名即可】
# # -args：以元组的方式给执行任务传参【元组相当于位置参数】
# # -kwargs：以字典的方式给执行任务传参【字典相当于关键字参数】
# # -name：线程名，一般不用设置
#
# # 启动线程，让线程开始工作
# thread_obj.start()





# # 【案例1】：多线程运行无参数的函数
#
# import time, threading
#
# def sing():
#     while True:
#         print('我在唱歌~~')
#         time.sleep(1)
#
# def dance():
#     while True:
#         print('我在跳舞~~')
#         time.sleep(1)
#
# if __name__ == '__main__':
#     # 构建线程对象
#     sing_thread = threading.Thread(target=sing)    # target = 目标任务名
#     dance_thread = threading.Thread(target=dance)  # 当所执行函数无参数，线程对象的参数仅(target=参数名)即可
#     # 让线程去执行（实现多线程）
#     sing_thread.start()
#     dance_thread.start()
#  # 由于sing和dance函数为死循环，若不用多线程，将无法同时执行两个函数


# # 【案例2】：多线程运行有参数的函数
#
# import time, threading
#
# def pri1(str):
#     while True:
#         print(str)
#         time.sleep(1)
#
# def pri2(str):
#     while True:
#         print(str)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     pri1_thread = threading.Thread(target=pri1, args=('123',))  # 当目标函数有参数，用args传递元组，填充函数的(位置)参数列表
#     pri2_thread = threading.Thread(target=pri2, kwargs={'str':'456'})  # 用kwargs传递字典，键值对来进行关键字传参
#     pri1_thread.start()
#     pri2_thread.start()















### (5)网络编程

# socket(套接字)，是程序之间通信的一个工具，好比现实生活中的插座，所有家用电器想要工作都是基于插座进行
# 进程之间想要进行网络通信，需要socket
# socket负责进程之间的网络传输，好比数据的搬运工

# 两个客户端进程之间通过Socket进行相互通通讯，必须有服务端作为中转
# socket服务端：等待其他进程的连接、可接受发来的消息、可以回复消息
# socket客户端：主动连接服务器、可以大宋消息、可以接受消息




## ① socket服务端编程
# 步骤如下：

# # 1.创建socket对象
# import socket
# socket_server = socket.socket()  # 此时对象并未区分是服务端/客户端
#
# # 2.绑定IP地址和端口【bind方法将socket对象确定为服务端】
# socket_server.bind(('localhost',8888))  # 将socket_server对象绑定到了本机的8888端口上
# # bind - 英文：绑定；直接与ip、端口绑定，所以为服务端
#
# # 3.服务端开始监听端口
# socket_server.listen(1)
# # 参数中的整数，表示接受的连接数量
#
# # 4.接受客户端连接，获得连接对象
# coon, address = socket_server.accept()
# # accept返回的是一个二元元组(客户端和服务端的对象, 客户端的地址信息)，可以使用上述形式，用两个变量依次接收二元元组的2个元素
# # accept方法为【阻塞】方法，如果没有连接，会卡在当前这一步，不向下执行
# print(f'接收到客户端的连接，客户端的信息是：{address}')
#
#
# # 5.客户端连接后，通过recv接收客户端消息，send给客户端发送消息
# # 注意：收发信息使用客户端和服务端的连接对象coon进行
# while True:
#     data = coon.recv(1024).decode('UTF-8')
#     # recv方法的返回值是字节数组(Bytes)，可以通过decode使用UTF-8解码为字符串
#     # recv方法的传参是buffsize，缓冲区大小，一般设置为1024
#     if data == 'exit':
#         break
#     print('客户端发来的消息是：',data)
#
#     coon.send(input('请输入你要回复的信息').encode('UTF-8'))
#     # 发送的数据需要用encode将字符串编码为字节数组
#
# # 6.关闭连接
# coon.close()
# socket_server.close()





## ② socked客户端编程
# 创建客户端的方法与上面服务端类似；客户端先发送再接收，服务端先接收再回复
# 步骤如下：

# # 1.创建socket对象
# import socket
# socket_client = socket.socket()
#
# # 2.连接到服务端【connect方法将socket对象确定为客户端】
# socket_client.connect(('localhost', 8888))
#
# # 3.send发送消息、recv接收消息
# while True:
#     send_data = input('请输入要发送的信息：')
#     if send_data == 'exit':
#         break
#     socket_client.send(send_data.encode('UTF-8')) # 发送之前记得将UTF-8编码解码为字节数组
#
#     recv_data = socket_client.recv(1024)  # recv方法是阻塞式的，接收到东西才继续向下执行；1024是缓冲区的大小
#     print('接收到的消息为：',recv_data.decode('UTF-8'))
#
# # 4.关闭链接
# socket_client.close()















### (6)正则表达式





### (7)递归








