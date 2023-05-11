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

# 正则表达式：
# 正则表达式，又称规则表达式(Regular Expression)，是使用单个字符串来描述、匹配某个句法规则的字符串，常被用来检索、替换那些符合某个模式(规则)的文本。
# 简单来说，正则表达式就是使用：字符串定义规则，并通过规则去检验字符串是否匹配。
# 比如，检验一个字符串是否符合条件的电子邮箱地址，只需要配置好正则规则，即可匹配任意邮箱。
# 比如通过正在规则：(^[\w-]+(\.[\w-])*@[\w-]+(\.[\w-]+)+$)即可匹配一个字符串是否是标准邮箱格式


# # (1)基础匹配
# re模块：
# python正则表达式，使用re模块，并基于re模块中三个基础方法来做正则匹配。
# 分别是：①match、②search、③findall三个基础方法
# 如下：
# match：从头匹配，匹配第一个命中项，返回匹配对象
# search：全局匹配。匹配第一个命中项，返回匹配对象
# findall：全局匹配。匹配全部命中项，返回字符串列表



## ① match（头部匹配）：
# 语法：re.match(匹配规则, 被匹配的字符串)
# 功能：从被匹配的字符串的开头进行匹配，匹配成功返回第一个匹配对象,匹配不成功返回None
# 匹配对象：匹配成功返回的对象包含span（匹配字段的下标范围，左闭右开）和 match（匹配的内容）等
# 注意：【match从头匹配，若开头不匹配，则直接停止】

# import re
# s1 = '114514 1919810'
# s2 = '1919810 114514'
#
# result1 = re.match('114', s1)
# print(result1)  # <re.Match object; span=(0, 3), match='114'>
# print(result1.span())  # (0, 3)
# print(result1.group())  # 114
#
# result2 = re.match('114', s2)
# print(result2)  # None




## ② search（搜索匹配）
# 语法：re.search(匹配规则, 被匹配字符串)
# 功能：搜索整个字符串，找出第一个匹配的内容，返回匹配对象。之后停止，不会继续向后；找不到返回None

# import re
# s = 'qwer1234asdf1234'
# result = re.search('1234', s)
# print(result)  # <re.Match object; span=(4, 8), match='1234'>




## ② findall（搜索全部匹配）
# 语法：re.findall(匹配规则, 被匹配字符串)
# 功能：匹配整个字符串，找出并返回全部匹配项到列表中，['字符串1', '字符串2',...]；找不到返回空list:[]

# import re
# s = 'qwer66asdf66zxcv66'
# result1 = re.findall('66', s)
# print(result1)  # ['66', '66', '66']
# result2 = re.findall('77', s)
# print(result2)  # None





# # (2)元字符匹配
# 在上面我们只使用了基础的字符串匹配，正在最强大的功能在于元字符匹配规则。


## (Ⅰ) 单字符匹配：
# ————————————————————————————————————————————————————————————————-———————————————————
#  字符 | 功能
#  .   | 匹配任意一个字符(除了\n)，\.匹配点本身
#  []  | 匹配[]中列举的字符； []内可以写：[a-zA-Z0-9]这三种范围组合，或者指定单个字符[acgDF135]
#  \d  | 匹配数字，即0-9
#  \D  | 匹配非数字
#  \s  | 匹配空白，即空格、Tab键
#  \S  | 匹配非空白
#  \w  | 匹配单词字符，即a-z、A-Z、0-9、_   注意：不光字母数字，还包含下划线
#  \W  | 匹配非单词字符
# —————————————————————————————————————————————————————————————————————————————————————
# 注意：上面的字符不是转义字符，所以在编写正则规则时，记得r"xxx"去除转义


# # 单字符匹配的应用
# import re
# s = '1qas2 @xw3!#d45sw  sa6--+s7??'
# # 找出s中全部数字
# result1 = re.findall(r'\d', s)  # 注意：字符串前面带上【r】标记，表示字符串中转义字符无效，就是普通的字符
# print(result1)  # ['1', '2', '3', '4', '5', '6', '7']
# # 找出s中特殊字符
# result2 = re.findall(r'\W', s)
# print(result2)  # [' ', '@', '!', '#', ' ', ' ', '-', '-', '+', '?', '?']
# # 找出全部英文字母
# result3 = re.findall(r'[a-zA-Z]', s)
# print(result3)  # ['q', 'a', 's', 'x', 'w', 'd', 's', 'w', 's', 'a', 's']




## (Ⅱ)数量匹配
# —————————————————————————————————————————————————————————————————————————————————————————————
#  字符   | 功能
#  *     | 匹配前一个规则的字符出现0至无穷次    \d* 表示数字可以有0个到∞个
#  +     | 匹配前一个规则的字符出现1至无穷次    \d+ 表示[1,∞)
#  ?     | 匹配前一个规则的字符出现0次至1次     \d? 表示1个数字，或者没有数字
#  {m}   | 匹配前一个规则的字符出现m次         \d{m} 表示数字出现m次
#  {m,}  | 匹配前一个规则的字符出现至少m次      \d{m,} 表示数字出现[m,∞)次
#  {m,n} | 匹配前一个规则的字符出现m到n次      \d{m,n} 表示数字出现[m,n]次 【注意：m,n 逗号后不要写空格】
# —————————————————————————————————————————————————————————————————————————————————————————————

## (Ⅲ)边界匹配
# ——————————————————————————————
#  字符 | 功能
#  ^   | 从被匹配字符串的开头 进行匹配
#  $   | 一直匹配到 被匹配字符串的结尾
#  \b  | 匹配一个单词的边界
#  \B  | 匹配非单词边界
# ——————————————————————————————

## (Ⅳ)分组匹配
# ———————————————————————————————
#  字符 | 功能
#  |   | 匹配左右任意一个表达式    如：(abc|bcd|def)，表示在abc\bcd\def中任选一个
#  ()  | 将括号中字符作为一个分组   如：(_\w+)* 表示将括号内的一组内容，写[0,∞]次
# ———————————————————————————————


# # # 案例演示：
# import re
# # ①匹配账号，只能由字母和数字组成，长度限制6-10为
# r1 = r'^[0-9a-zA-Z]{6,10}$'  # 前面[]限制单个字符的范围，后面{}限制字符的个数，^$表示从头匹配，到尾结束
# s1 = 'wsdf234'
# s2 = 'as_12dq_'
# print(re.findall(r1, s1))  # ['wsdf234']，匹配
# print(re.findall(r1, s2))  # []，不匹配
#
# # ②匹配QQ号，要求纯数字，长度5-11，第一位不为0
# r2 = r'^[1-9]\d{4,10}$'  # 注意：可以把各种拼起来表示一句规则；[1-9]表示第一位数字，\d{4,10}表示后面的数字，^$表示从头到尾匹配
# s3 = '1234567'
# s4 = '01234567'
# print(re.findall(r2, s3))  # ['1234567']
# print(re.findall(r2, s4))  # []
#
# r3 = '[1-9]\d{4,10}'
# print(re.findall(r3, s4))  # ['1234567']，注意，这里findall跳过前面的0，返回了部分字符串，不是我们想要的结果。这是因为定义规则时没有 ^、$ 规定从开头到结尾
# # 所以要明确是匹配子串还是匹配整体，以此考虑是否添加^$
#
# # ③匹配邮箱地址，只允许qq\163\gmail这三种邮箱地址
# # 邮箱格式可以为 123.qwe.1_2.a-b.…@qq.com.cn.eu.qq.…
# r4 = r'^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$'
# r5 = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
# s5 = '123.qwe.1_2.a-b@qq.com.cn.eu.qq'
# print(re.findall(r4, s5))  # [('.a-b', 'qq', '.qq')] # findall的特殊之处在于：若规则中有括号()进行的分组，会将每一个组返回，而不再返回原本的内容
# print(re.findall(r5, s5))  # [('123.qwe.1_2.a-b@qq.com.cn.eu.qq', '.a-b', 'qq', '.qq')] # 所以对规则整体加括号，即可得到想要的结果
# print(re.match(r4, s5))    # <re.Match object; span=(0, 31), match='123.qwe.1_2.a-b@qq.com.cn.eu.qq'> ，不想显示每个()分组内容，可以直接不要findall
# #
# # 将上面逐步拆分 ^  [\w-]+  (\.[\w-]+)*  @  (qq|163|gmail)  (\.[\w-]+)+  $ 解释如下：
# # ①[\w-]+  :将[]内的\w或-重复[1,∞次)
# # ②(\.[\w-]+)*  :将\.和[\w-]+用()变为一个整体，重复[0,∞)次
# # ③(qq|163|gmail)  :qq、163、gmail三选一
# # ④(\.[\w-]+)+  :将(\.[\w-]+)重复[1,∞)次
# # ⑤将上述依次拼起来，并^$从头到尾















### (7)递归

# python的递归，思路和其他语言相同

# 递归:程序调用自身的编程技巧
# 通常把大规模复杂为题层层转化为同类型规模较小的为题来解决，思想是把大事化小
# 递归的三大要素
# ①明确该函数想要干什么
#   即明确函数返回什么，或每次递归中要做什么
# ②寻找递归结束条件
#   递归，即在函数中，调用这个函数本身。每次函数执行必须有的结束条件，否则函数会无线调用自己。
# ③寻找函数的等价关系式(重点)
#   每次递归中，要不断缩小参数的范围。缩小之后，可通过一些辅助的变量或者操作，使原函数的结果不变。



# # 案例①：计算斐波那契数量的第n项
# # 斐波那契数列：[1,1,2,3,5,8,13,21,34,55……]，下标从0开始
# def f(num):
#     if num <= 1:
#         return 1
#     else:
#         return f(num - 1) + f(num - 2)
#
# print(f(9))  # 55



# # 案例②：用递归遍历文件夹中的全部文件,并将其存入列表返回
# # 知识点补充：os模块
# # os.listdir(文件夹名) - 返回存有子文件的列表
# # os.path.isdir(文件名) - 判断指定路径是否为文件夹
# # os.path.exists(文件名) - 判断指定路径是否存在
#
# import os
# def get_files(filename):
#     """
#     从指定文件夹中使用递归方式，获得全部的文件列表
#     :param filename: 被遍历的文件名
#     :return: 包含全部(非文件夹)文件的列表
#     """
#     if os.path.exists(filename):
#         file_list = []
#         for f in os.listdir(filename):
#             f = filename + "\\" + f  # 将文件名变为完整路径
#             if os.path.isdir(f):
#                 file_list += get_files(f)  # 若子文件为文件夹，递归； get_files(f)代表子文件夹的文件列表，所以要加到file_list中
#             else:
#                 file_list.append(f)
#         return file_list  # 每次递归，返回当此的文件列表
#     else:
#         print('输入的路径不存在')
#         return []
#
#
# file_list = get_files('D:\Python\python项目\python_learn')
# print(file_list)

