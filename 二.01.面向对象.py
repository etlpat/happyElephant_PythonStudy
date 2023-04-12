"""
目录：
1.初识对象
2.成员方法
3.类和对象
4.构造方法
5.其他内置方法 (魔术方法)
6.封装
7.继承
8.类型注解
9.多态
10.综合案例
"""
import json
import random

### 1.初识对象
# object 英文： n. 对象、物体
# Py中object指对象

# 【面向对象编程】是一种编程范式，它将复杂问题视为对象，【对象是数据和行为的集合】。
# 在 Python 中一切都是对象，包括函数，类，变量，字符串，列表和元组。
# 对象可以用类来抽象，【类是对象的模具】，对象是类的实例。
# 在面向对象编程中，对象是程序的基本单元，它们可以与其他对象交互以完成任务


# 在使用对象来组织数据时，一般有如下步骤：
# 设计类 -> 创建对象 -> 对象属性赋值
# 例子如下：


# # (1)设计类(class)
# class Student:
#     name = None  # 记录学生姓名
#
# # (2)创建对象
# stu_1 = Student()
# stu_2 = Student()
#
# # (3)对象属性赋值
# stu_1.name = '张三'
# stu_2.name = '李四'















### 2.成员方法

# 创建一个类时，我们一般会在类中添加属性和行为：
#   类的属性 - 数据 (成员变量)
#   类的行为 - 函数 (成员方法)
# 也就是说，我们之前见过的所有【方法】，都是【定义在类内部的函数】



# # 【方法详解】
# 方法的创建和我们之前学过的函数的创建格式基本一致，但仍有细微的差别：
#
# # 语法：
# def 方法名(self, 形参1, 形参2,...):
#     方法体
#     ...
#
# 可以看到，在方法的参数列表中，有一个【self关键字】
# self关键字：用于在方法内部访问成员变量   (注意：无论用不用，self都必须存在于方法的参数列表中)
#    ① self用来表示类对象自身的意思
#    ② 当我们使用类对象调用方法时，self会自动被python传入
#    ③ 【在方法内部，想要访问类的成员变量，必须使用self】
#
# 注意：尽管在类中创建方法时，必须设定self形参；但在实际调用时，实参可以不传它，会自动传入




# # 下面是例子：
#
# class Student:
#     name = None  # 学生的姓名
#     age = None  # 学生的年龄
#
#     def say_hi1(self):
#         print(f'Hi大家好，我是{self.name}')  # 注意：想要在成员方法中访问成员变量，必须self.变量名（因为参数只有self）
#
#     def say_hi2(self, str):
#         print(f'Hi大家好，我是{self.name},{str}')
#
# stu_1 = Student()
# stu_1.name = '张三'
# stu_1.say_hi1()  # Hi大家好，我是张三
# stu_1.say_hi2('哎呦！')  # Hi大家好，我是张三,哎呦！
#
#
# # 可以看出，类中：
# #    ①既可以定义属性类记录数据
# #    ②也可以定义函数来记录行为
# # 其中：
# #    ①定义的属性（变量），我们称之为：成员变量
# #    ②定义的行为（函数），我们称之为：成员方法















### 3.类和对象

# class: 类别 ，把..分类
# 定义类时，Py用的是Pascal命名法，用大写字母来分隔单词（除了Pascal命名法，还有下划线命名法，即用下划线分隔单词）


# # 类的定义：
# class 类名称:
#     # 类的属性 - 即定义在类中的变量  （成员变量）
#     # ...
#
#     # 类的行为 - 即定义在类中的函数  （成员方法）
#     # ...
#
#
# # 创建对象：
# 对象 = 类名称()



# ## 实例如下：
#
# # 设计一个闹钟类
# class Clock:
#     id = None
#     price = None
#
#     def ring(self):
#         import winsound
#         winsound.Beep(2000,3000)  # 铃声频率、响铃持续实际(ms)
#
# # 构建两个闹钟对象
# clock_1 = Clock()
# clock_1.id = '114514'
# clock_1.price = 99
# print(f'闹钟ID:{clock_1.id}，价格{clock_1.price}')
# clock_1.ring()
#
# clock_2 = Clock()
# clock_2.id = '191981'
# clock_2.price = 19.9
# print(f'闹钟ID:{clock_2.id}，价格{clock_2.price}')
# clock_2.ring()















### 4.构造方法

# 上面的代码中，我们用多个单独的变量描述对象的属性，为对象的属性赋值需要依次进行，略显繁琐。
# 下面我们使用构造方法来避免上述的问题。


### 构造方法:__init__()
#
# # Python类可以使用： __init__() 方法，称之为【构造方法】
# # __init__，顾名思义，在创建对象时会自动执行，并将参数传入__init__方法中。
# # 构造方法的【功能】：对成员变量进行【声明】并【赋值】
# # 实例如下：
#
#
# class Student():
#
#     def __init__(self, name, age, tel):
#         self.name = name   # 定义变量self.name，并用参数name对其赋值
#         self.age = age
#         self.tel = tel
#
# stu_1 = Student('张三', 18, '7654321')  # 可以在创建对象时直接传参
#
#
# # 上面__init__方法的作用是：声明了name,age,tel三个变量，并用创建对象时传入的参数对其进行赋值。
# # 注意：① 由于构造方法会自动声明其中的成员变量，所以不用再前面另外声明变量
# #      ② 构造方法也是方法，不要省略self参数
# #      ③ 构造方法会把创建对象语句本身变为一个方法，必须传参，否则报错 (除非__init__设定缺省型参数)




# # 案例练习：键入十位学生对象信息并打印：
#
# class Student():
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#
# for i in range(10):
#     name = input(f'请输入第{i+1}个姓名：')
#     age = input(f'请输入第{i+1}个年龄：')
#     address = input(f'请输入第{i+1}个地址：')
#     stu = Student(name,age,address)
#     print(f'第{i+1}个学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}')















### 5.其他内置方法 (魔术方法)

# 上面学习的__init__构造方法，是Python类内置的方法之一
# 这些内置的类方法，各有各的特殊功能，这些内置方法我们也称之为：魔术方法


# 魔术方法：
#   ① __init__ 构造方法
#   ② __str__ 字符串方法
#   ③ __lt__ 小于(<)、大于(>)符号比较
#   ④ __le__ 小于等于(<=)、大于等于(>=)符号比较
#   ⑤ __eq__ 判断是否相等(==)符号比较
#   ......



# (1)__str__ 字符串方法

# 在Python中，__str__()方法用于编辑【直接操作对象时返回的字符串的内容】。当对对象直接调用print()或str()函数时，将调用__ste__中返回的字符串内容。
# 如果我们没有为类实现__str__()方法，则使用内置对象实现，该实现实际上调用__repr__()函数。
#   即：【若不写__str__，就返回地址，若写了，就返回__str__中定义的返回内容】


# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# stu_1 = Student('张三',18)
# print(stu_1)        # <__main__.Student object at 0x000001CD5A84C2D0>
# print(type(stu_1))  # <class '__main__.Student'>
# print(str(stu_1))   # <__main__.Student object at 0x000001CA53C7C2D0>
#
#
# # 如上，当直接打印类对象时，数输出如上结果(内存地址)
# # 内存地址我们一般不会用到，我们可以通过__str__方法，控制直接输出类时的结果。


# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'Student类对象,name={self.name},age={self.age}'
#
# stu_1 = Student('张三',18)
# print(stu_1)        # Student类对象,name=张三,age=18
# print(str(stu_1))   # Student类对象,name=张三,age=18
#
# # 如上：__str__ 可以编辑输出类对象名时返回的字符串内容





# (2)__lt__ 小于、大于符号比较

# 两个类不能用大于号(>)小于号(<)比较大小，会报错
# 我们在类中定义__lt__方法，可以规定比较依据，并返回比较的值
#
# 严格意义上来讲，__lt__是用于小于符号的比较，但是由于小于可比，大于的值也是确定的
#   由于__lt__本身是进行小于比较，所以返回时一定要以小于的形式返回 xxx < xxx 的形式
#   __lt__的两个参数是self和other：self表示自身的类对象，other表示另外一个类对象


# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __lt__(self, other):  # other表示另外一个类对象
#         return self.age < other.age  # 以age为比较依据
#
# stu_1 = Student('张三',18)
# stu_2 = Student('李四',25)
# print(stu_1<stu_2)  # True
# print(stu_1>stu_2)  # False





# (3)__le__ 小于等于、大于等于符号比较
# __le__逻辑与__lt__相同，只是多一个等于的判断

# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __le__(self, other):
#         return self.age <= other.age
#
# stu_1 = Student('张三',18)
# stu_2 = Student('李四',25)
# print(stu_1<=stu_2)  # True
# print(stu_1>=stu_2)  # False





# (4)__eq__ ==符号比较
# __eq__逻辑与__lt__、__le__相同，可以进行==的判断
# 与lt、le不同的是：当没有__eq__时，也可以用==比较两个类，比较的是内存地址。

# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
# stu_1 = Student('张三',18)
# stu_2 = Student('李四',18)
# print(stu_1==stu_2)  # True




# 魔术方法总结：
# ———————————————————————————————————————————————————————————————
# 序号 |   方法       |          功能
#  1  | __init__    |  构造方法，可以用于创建类对象，同时对其赋值
#  2  | __str__     |  用于编辑直接操作类对象时返回的字符串的内容
#  3  | __lt__      |  用于2给类对象进行小于或大于比较
#  4  | __le__      |  用于2给类对象进行小于等于或大于等于比较
#  5  | __eq__      |  用于2给类对象进行相等比较
# ———————————————————————————————————————————————————————————————


# # 魔术方法使用案例
#
# class Student():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f'Student类对象,name={self.name},age={self.age}'
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __le__(self, other):
#         return self.age <= other.age
#
#     def __eq__(self, other):
#         return self.age == other.age
#
# stu_1 = Student('张三',18)
# stu_2 = Student('李四',38)
# print(stu_1)  # Student类对象,name=张三,age=18
# print(stu_1 < stu_2)  # True
# print(stu_1 <= stu_2)  # True
# print(stu_1 == stu_2)  # False















### 6.封装

# 面向对象编程，是许多编程语言都支持的一种编程思想。
# 简单理解是：基于模板(类)去创建实体(对象)，使对象完成功能开发。
# 面向对象包含三大主要特性：
#   ·封装
#   ·继承
#   ·多态


# # 封装是指？
# 【封装】表示的是：将现实世界事物的[属性][行为]，封装到类中描述为[成员变量][成员方法]，从而完成对现实世界事物的描述。
# 现实世界中的属性和行为，不都是对用户开放使用的，同理，类中提供了【私有成员】的形式



# 类中的【私有成员】：私有成员变量 和 私有成员方法
#
# # 如何定义私有成员？
# ·私有成员变量：变量名以__开头（两个下划线）
# ·私有成员方法：方法名以__开头（两个下划线）
# 即可完成私有成员的设置
#
#
# # 私有成员的访问限制？
# 私有变量/方法：只可被类中其他成员使用，不能被用户使用
# 若将变量或方法设为私有型，那么当【用户】使用私有方法或调用私有对象时，报错。（相对于使用了不存在的方法/变量）
# 虽然【用户不能使用私有成员】，但是【类中的其他成员可以访问私有成员】
#
#
# # 私有成员的意义是？
# 意义：在类中提供仅供内部使用的属性和方法，而不对外开放（类对象无法使用）



# class Phone():
#
#     __current_voltage = 0  # (私有成员变量)当前手机运行电压
#
#     def __keep_single_core(self):  # (私有成员方法)
#         print('cpu将以单核模式运行')
#
#     def call_by_5G(self): # 公开成员方法中，可以调用私有成员变量、私有成员方法
#         if self.__current_voltage >= 1:
#             print('5g通话已开启')
#         else:
#             print('电量不足，无法通话',end='，')
#             self.__keep_single_core()
#
#
# p1 = Phone()
#
# # print(p1.__current_voltage) # 报错，用户不能使用私有成员变量
# # p1.__keep_single_core()     # 报错，用户不能使用私有成员方法
#
# p1.call_by_5G()  # 电量不足，无法通话，cpu将以单核模式运行 (可以看出该方法中执行了私有成员方法)




# # 练习：
# # 设计一个手机类，内部包括：
# #  ·私有成员变量：__is_5g_enable，类型bool，True表示开启5g，False表示关闭5g
# #  ·私有成员方法：__check_5g()，会判断私有成员__is_5g_enable的值：
# #       若为True，打印输出5g开启
# #       若为False，打印输出5g关闭，使用4g网络
# #  ·公开成员方法：call_by_5g()，调用它会执行：
# #       调用成员方法：__check_5g()，判断5g网络
# #       打印输出：正在通话中
# # 运行结果：5g关闭，使用4g网络\n正在通话中
#
#
# class Phone():
#     __is_5g_enable = False
#
#     def __check_5g(self):
#         if self.__is_5g_enable:
#             print('5g开启')
#         else:
#             print('5g关闭，使用4g网络')
#
#     def call_by_5g(self):
#         self.__check_5g()
#         print('正在通话中')
#
# phone = Phone()
# phone.call_by_5g()  # 5g关闭，使用4g网络\n正在通话中















### 7.继承
## <1>继承的基本语法
## <2>复写和使用父类成员


#### <1>继承的基本语法
## (1) 继承介绍
## (2) 单继承
## (3) 多继承


# # (1)继承介绍
# 面向对象的编程带来的主要好处之一是代码的重用，实现各种重用的方法之一是通过【继承】。
# 继承就是【子类】继承【父类】的所有变量和方法，如果子类和父类有同名变量或方法，子类会覆盖掉父类。
# 补充：
#    ·通过继承创建的新类称为："子类"或"派生类"
#    ·被继承的类称为："父类"、"基类"或"超类"
#
# # 什么是继承？
# 继承表示：父类将把所有的成员变量和方法继承(复制)给子类 (注意：不含私有)
#         若子类、父类有[同名]的变量或方法，子类会[覆盖]掉父类
#
# # 什么时候使用继承？
# 假如我需要定义几个类，而类与类之间有一些公共的属性和方法。
# 这时我就可以把相同的属性和方法作为父类的成员，而特殊的方法及属性则在子类中定义。
# 通过继承，可以提高代码的可扩展性和重用行。
#
# # 补充：
# Python有单继承与多继承。单继承即子类继承于一个类，多继承即子类继承于多个类。






# # (2)单继承
# 单继承中，一个子类可以继承一个父类
#
# # 语法：
# class 类名(父类名):
#     类内容体
#     ...
#
# 注意：若类不继承时，类名后的括号可有可无
# 继承规则：
#   ① 父类将继承所有变量和方法给子类 (不含私有)
#   ② 若子类、父类有[同名]的变量或方法，子类会[覆盖]掉父类


# class Phone2010:
#     IMEI = 2010  # 序列号
#     producer = 'apple'  # 厂商
#
#     def call_by_4g(self):
#         print('4g通话')
#
# class Phone2023(Phone2010):
#     IMEI = 2023
#     face_id = '1145'  # 面部识别ID
#
#     def call_by_5g(self):
#         print('5g通话')
#
#
# new_phone = Phone2023()
# print(new_phone.IMEI)  # 2023（同名变量，子类覆盖父类）
# print(new_phone.producer)  # apple（子类可以使用父类变量）
# new_phone.call_by_4g()  # 4g通话（子类可以使用父类方法）
# new_phone.call_by_5g()  # 5g通话






# # (3)多继承
# 多继承中，一个子类可以继承多个父类。
# 多继承与单继承语法相似，区别是在括号中写多个父类即可。
#
# # 语法：
# class 类名(父类1, 父类2,......, 父类n):
#     类内容体
#     ...
#
# # 注意：多个父类中，如果有同名成员，则默认以继承顺序(从左到右)为优先级
# 【同名成员的优先级：子类 > 父类；多个父类从左到右，左边 > 右边】
# 和单继承一样，多继承的子类中也无法使用父类的私有成员


# 知识点补充：pass关键字
# pass关键字不做任何操作，仅用来补全语法。
# 比如子类继承了多个父类，不想再定义新成员，语法上 : 后面不能为空，所有写pass补全语法



# # 手机类
# class Phone:
#     IMEI = 11001 # 序列号
#     producer = 'apple'  # 厂商
#
#     def call_by_4g(self):
#         print('4g通话')
#
# # NFC读卡器类
# class NFCreader:
#     nfc_type = '第五代'
#     producer = 'xiaomi'
#
#     def read_card(self):
#         print('读取NFC卡')
#
#     def write_card(self):
#         print('写入NFC卡')
#
# # 红外控制类
# class RemoteControl:
#     rc_type = '红外控制'
#     producer = 'huawei'
#
#     def control(self):
#         print('红外控制开启')
#
# # 新手机类（多继承）
# class NewPhone(Phone, NFCreader, RemoteControl):
#     pass  # 这里不想定义新成员，但是按语法要求不能啥也不写，所有用到pass关键字
#
#
# phone = NewPhone()
# print(phone.IMEI)  # 11001 (可以使用父类的变量)
# print(phone.nfc_type)  # 第五代
# print(phone.rc_type)  # 红外控制
# phone.call_by_4g()  # 4g通话 (可以使用父类的方法)
# phone.read_card()  # 读取NFC卡
# phone.control()  # 红外控制开启
# print(phone.producer)  # apple (当多个父类中有同名变量/方法，按从左到右的优先级顺序继承)






#### <2>复写和使用父类成员
## (1)复写父类成员
## (2)子类中调用同名父类成员



# # (1)复写父类成员
# 子类继承父类的成员属性和方法后，如果对其“不满意”，可以对其进行修改，这种修改就称之为【复写】
# 复写：【即在子类中重新定义与父类同名的属性或方法】
# 原理：子类和父类中存在同名成员变量/方法，子类的成员会覆盖父类 (优先子类)


# class Phone:
#     IMEI = None
#     producer = 'apple'
#
#     def call(self):
#         print('使用4g进行通话')
#
# class NewPhone(Phone):
#     producer = 'pineapple'
#
#     def call(self):
#         print('使用5g进行通话')
#
# my_phone = NewPhone()
# print(my_phone.producer)  # pineapple
# my_phone.call()  # 使用5g进行通话
# # 可以看出：同名成员变量/方法，子类覆盖父类






# # (2)子类中调用同名父类成员
#
# 如果子类继承了父类，那么子类可以访问父类的所有公开属性和方法。
# 当子类中把父类成员复写之后，在类对象调用同名成员时，默认调用子类中的新成员。
# 子类内部，若想在复写后，重新调用父类的同名成员，那么两种方法如下：
#
# # 在子类中，如何调用同名的父类成员？
# 方式 1:
#  ·通过父类名直接调用，
#      父类名.变量
#      父类名.方法(self)  # 类中调用方法必须传self
#   原理：子类可以访问父类的所有公开属性和方法
#
# 方式 2:
#  ·通过super()函数调用
#    ② super().变量
#      super().方法()  # 这里括号中不用加self，因为super()函数会自动将self作为第一个参数传入
#   原理：原理：父类又称超类，super()相当于直接调用超类对象


# class Phone:
#     IMEI = None
#     producer = 'apple'
#
#     def call(self):
#         print('使用5g进行通话（来自于父类）')
#
# class NewPhone(Phone):
#
#     def call(self):# 这里想要调用父类中的同名方法，并输出厂商
#
#         # 法1：父类名.成员
#         print(f'父类的厂商是{Phone.producer}')
#         Phone.call(self)  # 类中调用方法必须传self
#
#         # 法2：super().成员
#         print(f'父类的厂商是{super().producer}')
#         super().call()  # super函数会自动为call传递self参数
#
#
# my_phone = NewPhone()
# my_phone.call()  # 可以看出，子类可以通过调用父类自身来访问其中的同名成员















### 8.类型注解

## (1)类型注解的介绍
## (2)变量的类型注解
## (3)函数(方法)的类型注解
## (4)Union类型



## (1)类型注解的介绍

# # 引入类型注解：
# pycharm具有(自动补全函数、变量名)、(提示参数类型)等功能：
# 【自动补全功能】：当一个内置函数名打了一半时，会自动提示补全后的函数名；【提示参数类型】：在调用方法函数时，ctrl p会对参数的类型进行提示
# 以上功能并非必须是内置函数才能执行，我们自己定义的成员/函数等无法提示，是因为pycharm无法通过代码，确定因传入什么类型，所有无法进行相关提示。
# 若想要pycharm对我们自定义的对象或函数等给出类似内置函数的提示，必须确定变量的类型，这就需要【类型注解】来实现



# # 什么是类型注解？
# Python在3.5版本引入了类型注解，以方便静态类型检查工具，IDE第三方工具。
# 【类型注解】：在代码中涉及数据交互的地方，提供数据类型的注解（显式的说明）
#
# # 主要功能：
# 帮助第三方IDE工具(如pycharm)对代码进行类型推断，协助做代码提示
# 帮助开发者自身对变量进行类型注释
#
# # 支持：
# 变量的类型注释
# 函数(方法)形参列表和返回值的类型注释






## (2)变量的类型注解

# 变量的注解有两种，如下：
# 语法1：变量:类型
# 语法2：# type:类型
#
# 注意： 类型注解只是提示性的，就算标错了，也不报错
# 一般遇到变量复杂到无法轻易看出类型时，我们才会使用类型注解方便使用。


# # 语法： 变量:类型
#
# # 基础变量的类型注解
# var_1 : int = 10
# var_2 : float = 3.14
# var_3 : bool = True
# var_4 : str = 'hihihi'
#
# # 类对象的类型注解
# class Student:
#     pass
# stu : Student = Student()
#
# # 基础容器的(简易)类型注解
# my_list : list = [1, 2, 3]
# my_tuple : tuple = (1, 2, 3)
# my_set : set = {1, 2, 3}
# my_dict :dict = {1:None, 2:None, 3:None}
# my_str : str = '123'
#
# # 基础容器的(详细)类型注解
# my_list : list[int] = [1, 2, 3]
# my_tuple : tuple[str,int,bool] = ('1', 2, True)
# my_set : set[int] = {1, 2, 3}
# my_dict :dict[int, str] = {1:'1', 2:'2', 3:'3'}  # 注意，字典注解时，键和值用逗号隔开



# 除了使用（变量:类型）这种语法以外，也可以【在注释中进行解析】
# 语法： # type:类型
#
# var_1 = random.randint(1,10)    # type : int
# var_2 = json.loads(data)        # type : dict[str, int]
# var_3 = func()                  # type : Student






## (3)函数(方法)的类型注解

# 函数中的类型注解包括（形参）和（返回值）的类型注解
# 同样，形参的类型注解也是提示性的，类型不同也不会报错
# 语法： def 函数名(形参1:类型, 形参2:类型,... ) -> 返回类型:
#           pass



# # ① 函数/方法，【形参】的类型注解
# 即写形参时，（形参:返回值）即可
#
# 语法： def 函数名(形参1:类型, 形参2:类型,... ):
#           pass

# def add(x: float, y: float):
#     return x + y
#
# add(3,5)




# # ② 函数/方法，【返回值】的类型注解
# 即函数括号后面，加上（-> 返回类型）即可
#
# 语法： def 函数名(形参1, 形参2,... ) -> 返回类型:
#           pass

# def add(x, y) -> float:
#     return x + y
#
# add(3,5)






## (4)Union类型












### 9.多态
### 10.综合案例



