"""
目录：
1.初识对象
2.成员方法
3.类和对象
4.构造方法
5.其他内置方法 (魔术方法)
6.封装
7.继承
8.类型解释
9.多态
10.综合案例
"""











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






### 8.类型解释
### 9.多态
### 10.综合案例








