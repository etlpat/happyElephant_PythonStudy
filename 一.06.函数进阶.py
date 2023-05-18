"""
目录：
1.函数多返回值
2.函数多种传参方式
  (1)位置参数
  (2)关键字参数
  (3)缺省参数
  (4)不定长参数
3.匿名函数
4.内置函数补充
"""









### 1.函数多返回值

## return：返回变量的值，并且结束函数
## 函数若想返回多个返回值，不能写多个return，而是在一个return中返回多个返回值
#
#
# 语法：def test_return():
#          return 1, 2, 3
#
# 调用：x, y, z = test_return()
#      print(x)  # 结果1
#      print(y)  # 结果2
#      print(z)  # 结果3
#
#
## 按照返回值的顺序，写对应顺序的多个变量接收即可
## 变量之间用逗号隔开
## 支持不同类型的数据return



# def func(f1, f2, f3, f4, num1, num2):
#     n1 = f1(num1, num2)
#     n2 = f2(num1, num2)
#     n3 = f3(num1, num2)
#     n4 = f4(num1, num2)
#     return n1, n2, n3, n4
#
# x1, x2, x3, x4 = func(lambda x,y:x+y, lambda x,y:x-y, lambda x,y:x*y, lambda x,y:x/y, 32, 17)
# print(x1, x2, x3, '%.2f' % x4)  # 49 15 544 1.88

















### 2.函数多种传参方式
## (1)位置参数
## (2)关键字参数
## (3)缺省参数
## (4)不定长参数





#### (1)位置参数

# 位置参数：调用函数是，根据函数定义的位置来传递参数
# 这种方法是咱们之前一直在使用的方法
# 注意：传递的参数和定义的参数的顺序及个数必须一致


# def user_info(name, age, num):
#     print(f"您的名字是{name}，年龄是{age}，电话号是{num}")
#
# user_info('jimmy', '18', '1234567')








#### (2)关键字参数

# 在Python中，关键字参数是指在函数调用时，通过指定参数名来传递参数的一种方式。
# 函数调用时，通过 “键 = 值” 形式传递参数
# 作用：可以让函数更加清晰、容易使用，同时也清除了参数的顺序要求


# def user_info(name, age, num):
#     print(f"您的名字是{name}，年龄是{age}，电话号是{num}")
#
#
# # 关键字传参
# user_info(name = 'jimmy', age = '18', num = '1234567')
#
# # 可以不按照固定顺序
# user_info(num = '1234567', name = 'jimmy', age = '18')
#
# # 可以和位置参数混用，位置参数必须在前，且匹配参数顺序
# user_info('jimmy', num = '1234567', age = '18')

# 注意：函数调用时，如果有位置参数时，位置参数必须在关键字参数前面，但关键字参数之间不存在先后顺序




# # 另外，如果函数定义中已经有默认参数值，我们可以只传递部分关键字参数。例如：
#
# def greet(name, message="Hello"):
#     print(f"{name}, {message}")
#
# greet(name="Alice")
# # 这将输出： Alice, Hello，因为我们只传递了一个关键字参数。








#### (3)缺省参数

# 缺省参数：也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
# 注意：写参数时，缺省参数只能放在参数列表的最后面，无论是实参还是形参，否则报错
# 作用：当调用函数时没有传递参数，就会使用默认参数的值


# def user_info(name, num, age = 18):
#      print(f"您的名字是{name}，年龄是{age}，电话号是{num}")
#
# user_info(name = 'jimmy', num = '1234567')
# user_info('小八', 1234567, 44)








#### (4)不定长参数

## 不定长参数：也叫可变参数，用于不确定调用时会传递多少个参数的场景
## 作用：当调用函数时不确定参数个数时，可以使用不定长参数
#
# 不定长参数的类型：
#  （1）位置传参
#  （2）关键字传参



##  （1）不定长位置传参
# 参数为【*变量名】表示接受任意数量的位置参数，它会将所有传入的位置参数封装成一个【元组】。
# 不定长定义的形参作为元组存在，接收不定长数量的参数传入
# 注意：不定长位置传参的形参一般叫做 *args

# def f(*num):
#     print(num)
#
# f(1, 2, 3)  # 输出：(1, 2, 3)
# f('a', 'b', 'c', 'd')  # 输出：('a', 'b', 'c', 'd')



##  （2）不定长关键字传参
# 参数为【**变量名】表示接受任意数量的关键字参数，它会将所有传入的关键字参数封装成一个【字典】。
# 注意：不定长位置传参的形参一般叫做 *kwargs

# def f(**num):
#     print(num)
#
# f(a=1, b=2, c=3)  # 输出：{'a': 1, 'b': 2, 'c': 3}
# f(name='John', age=30, gender='male')  # 输出：{'name': 'John', 'age': 30, 'gender': 'male'}


# 当同时使用位置传参和关键字传参时，【*变量名】必须放在【**变量名】前面。

# def func(*n1, **n2):
#     print(n1)
#     print(n2)
#
# func(1, 2, 3, a=4, b=5)  # 输出：(1, 2, 3) {'a': 4, 'b': 5}



##  （3）传参时的序列解包

# 与不定长参数相反，这里的序列解包是指实参，同样有*和**两种形式
# 实参中【*数据容器】，可将数据容器转化为位置参数
# 实参中【**数据容器】，可将数据容器转化为关键字参数

# # 案例如下：
# def demo(a, b, c):
#     return a+b+c
#
# list0 = [1, 2, 3]
# print(demo(*list0))  # 6，将[1, 2, 3]解包为位置参数1，2，3
# tuple0 = (1, 2, 3)
# print(demo(*tuple0))  # 6
# dict1 = {3: 'c', 1: 'b', 2: 'c'}
# print(demo(*dict1))  # 6，字典一个*解包，默认将键传给位置参数
#
# dict2 = {'c': 3, 'b': 2, 'a': 1}
# print(demo(**dict2))  # 6，这里将字典解包为关键字参数c=3,b=2,a=1

















### 3.匿名函数
## (1)函数作为参数传递
## (2)lambda匿名函数






#### (1)函数作为参数传递

# 在前面的函数学习中，都是将 数据/数据容器 作为参数传入的
# 其实，我们也可以将函数作为一个参数传入函数内


# # 如下代码：
# def test_func(f):
#     num = f(1,2)
#     print(num)
#
# def add(x, y):
#     return x + y
#
# test_func(add)
# # 函数add，作为参数，传入了函数 test_func 中使用
# #   test_func需要一个函数作为参数传入，且这个函数的参数是两个数字，有返回值
# #   add接收两个数字，返回计算结果，add作为参数传递给了test_func使用
# #   最终在test_func内部，由传入的add函数，完成了对数字的计算操作


# 所以，这是一种，【计算逻辑的传递】，而非数据的传递
# 像上述那样，不仅是相加，相减、相乘等任何逻辑都可以自定义并作为函数传入
# 数据传递和函数传递的区别在于：【一个是数据不确定，另一个是计算逻辑不确定】







#### (2)lambda匿名函数

# 函数的定义中
#   def关键字，可以定义带有名称的函数
#   lambda关键字，可以定义匿名函数(无名称)
# 有名称的函数，可以使用名称来重复调用
# 无名称的匿名函数，只可以临时使用一次


# 匿名函数
# 语法：lambda 形式参数: 函数体...（一行代码）
#
#   lambda是关键字，表示定义匿名函数
#   形参数量无限制
#   函数体，就是函数的执行逻辑，要注意；【匿名函数的函数体只能写一行，无法写多行代码】
#
## 注意：【lambda函数体不用写return语句，默认直接return】



# def test_func(f, num1, num2):
#     num = f(num1, num2)
#     print(num)
#
# test_func(lambda x, y: x + y, 2, 3)  # 5
# test_func(lambda x, y: x * y, 5, 2)  # 10

















### 4.内置函数补充

"""
(1)类型转换与判断
① bin()、oct()、hex()
② float()、complex()
③ int()
④ ord()、chr()
⑤ list()、tuple()、str()、set()、dict()
⑥ eval()
⑦ type()、isinstance()

(2)最值和求和
① max()、min()
② sum()

(3)基本输入/输出
① input()
② print()

(4)排序与逆序
① sorted()
② list.sort()
③ reversed()

(5)枚举与迭代
① enumerate()

(6) map()函数、reduce()函数、filter()函数

(7) range()函数

(8) zip()函数
"""



# # (1)类型转换与判断

# ① bin()、oct()、hex()，用来将整数转换位二进制、八进制和十六进制
# 参数要求必须是整数，但不必是十进制
#
# print(bin(555))  # 0b1000101011，py中，0b是二进制整数的开头
# print(oct(555))  # 0o1053，py中，0o是二进制整数的开头
# print(hex(555))  # 0x22b，py中，0x是二进制整数的开头


# ②float()将其他类型数据转换为实数(浮点数)；
#   complex()用来生成复数
#
# print(float(3))  # 3.0
# print(float("3.5"))  # 3.5
# print(complex(3))  # (3+0j) 指定实部，创建复数
# print(complex(3, 5))  # (3+5j) 指定实部和虚部


# ③int()获取实数的整数部分；或者将指定进制的数字str转换为十进制数
# 将指定进制的数字str转换为十进制数，语法：int(str, 进制数)，返回转换为十进制后的数字
#
# print(int(3.14))  # 3
# print(int('111', 2))  # 7  将二进制的'111'转化为十进制
# print(int('111', 8))  # 73  将八进制的'111'转化为十进制
# print(int('111', 16))  # 273
# print(int('0o1234', 8))  # 668  将八进制的0o1234转化为十进制
# print(int('0o1234', 0))  # 668  由于0o1234肯定为八进制，所以进制数可以填0


# ④ord()返回单个字符的Unicode码；chr()返回Unicode码对应的字符
#
# print(ord('a'))  # 97
# print(chr(65))   # 'A'
# print(chr(ord('a') + 1))  # 'b'


# ⑤数据容器转换函数：list()、tuple()、str()、set()、dict()
# 具体内容我们在数据容器章节详细讲过，下面是一些简单的例子：
#
# print(str({1,2,3}))  # {1, 2, 3}，直接变成字符串
# print(list(str([1,2,3])))  # ['[', '1', ',', ' ', '2', ',', ' ', '3', ']']
# print(list(range(5)))  # [0, 1, 2, 3, 4]
# print(dict(zip('1234', 'abcde')))  # {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}
# print(set('111223'))  # {'3', '1', '2'}


# ⑥内置函数eval()，用于计算字符串的值，并返回
#
# print(eval('3+5'))  # 8，eval计算字符串的值
# print(type(eval('3+5')))  # <class 'int'>，返回值为int
# print(eval('9'))    # 9
# # print(eval('09'))   # 报错，eval不允许计算以0开头的数字
# print(int('09'))    # 9，int允许以0开头的数字
# print(list(str([1, 2, 3])))  # ['[', '1', ',', ' ', '2', ',', ' ', '3', ']']
# print(eval(str([1, 2, 3])))  # [1, 2, 3]，字符串求值，还原对象
# print(eval('(1,2,3)'))  # (1, 2, 3)
# print(eval('sum(range(1,101))'))  # 5050，eval也可以计算字符串中包含的函数值


# ⑦type()和isinstance()，查看、判断数据的类型
# isinstance - 英文：是实例吗？  instance n.例子、实例
# 语法：isinstance(object, class_type)，功能：判断对象是否为指定的类型/是否在指定的类型列表中，返回bool值
#
# print(type((1,)))  # <class 'tuple'>
# print(type({3}) in (list, tuple, dict))  # False
# print(isinstance(3, int))  # True，3是int类型
# print(isinstance(3j, (float, complex)))  # True，isinstance函数的参数也可以是类型列表




# # (2)最值和求和

# ①max()、min()返回数据容器等有限个可迭代对象的最大值、最小值
# 注意：参数除了传递数据容器，还可以max(range(……))，或直接传入要比较的对象max('1', 'a', 'qwe')
#
# print(max([1, 2, 3]))  # 3
# print(min((1, 2, 3)))  # 1
# print(max("abc"))      # c
# print(min({'a', 'b', 'c'}))  # a
# print(max({1:None, 2:None, 3:None}))  # 3 （对字典的键进行比较）
# print(max(1, 2, 3, 4))       # 4
# print(min('abc', 'ABC', 'abcd'))  # ABC
#
# 注：max()和min()还支持key参数，用来指定比较大小的依据，key必须是函数
# list0 = list(map(lambda x: str(x), list(range(1, 11))))
# print(list0)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# print(max(list0, key=len))  # 10


# ②sum()计算数据容器等可迭代对象元素的和
# 计算规则和上面的差不多，但是不能直接sum字符串中元素的和，sum("123")报错
#
# print(sum([1, 2, 3]))  # 6
# # print(sum('123'))  # 报错
# print(sum({1, 2, 3}))  # 6
# print(sum({1:None, 2:None, 3:None}))  # 6




# # (3)基本输入/输出

# ①input()接收来自键盘的输入，无论用户输入什么内容，一律返回字符串
# 由于返回字符串，我们可以使用int()、float()、eval()等对用户输入的内容进行转换
#
# print(input('请输入"123":'))  # 123
# print(type(input('请输入"123":')))  # <class 'str'>
# print(type(int(input('请输入"123":'))))  # <class 'int'>
# print(eval(input('请输入"[1,2,3]":')))   # [1, 2, 3]
# print(type(eval(input('请输入"[1,2,3]":'))))  # <class 'list'>


# ②print用于输出信息到标准控制台
# 语法：print(value1, value2,...,sep=' ', end='\n', file=sys.stdout, flush=False)，这是print函数的默认形式。
# 其中常用的关键字参数就是：sep参数间修改分隔符，end修改末尾字符串
#
# print(1, 2, 3, 4, sep='|')  # 1|2|3|4
# for i in range(1, 10):
#     print(i, end='')  # 123456789




# # (4)排序与逆序

# ① sorted()函数
# 功能：对数据容器等可迭代对象以key为依据进行排序，并【不改变数据容器的内容，返回新列表】。
# 注意：sorted函数不管传入什么数据容器，都不改变其内容，但是均以list形式返回。
# 语法：sorted(iterable, cmp=None, key=None, reverse=False)  # cmp暂时不用管
#     iterable：表示可迭代对象，数据容器或range(5)等皆可
#     key：函数key作为列表的排序依据；接受一个函数（或一个lambda匿名函数），该函数【接受一个列表项】并【返回一个用于排序的键】；key默认为元素本身。例如，如果想按字符串长度降序对列表进行排序，可以使用key=len
#     reverse ：排序规则，reverse = True 降序， reverse = False 升序（默认）
#
# x0 = [5, 4, 3, 2, 1]
# x1 = sorted(x0)
# print(x0)  # [5, 4, 3, 2, 1]，sorted方法不改变数据容器自身内容
# print(x1)  # [1, 2, 3, 4, 5]，sorted方法返回存放内容的列表，默认升序
#
# print(sorted({(1,'c'), (2,'b'), (3,'a')}, key=lambda x: x[0], reverse=True))  # [(3, 'a'), (2, 'b'), (1, 'c')]，以x[0]为依据，降序排列，返回列表
# print(sorted({(1,'c'), (2,'b'), (3,'a')}, key=lambda x: x[1], reverse=True))  # [(1, 'c'), (2, 'b'), (3, 'a')]，以x[1]为依据，升序排列，返回列表
#
# # 对字典进行排序，默认只对键进行处理
# print(sorted({1:3, 3:2, 2:1}))  # [1, 2, 3]，仅返回键所在的列表
# # 虽然sorted()函数无法直接返回带有完整键值对的列表，但是我们可以通过字典的items()方法，间接对字典按想要的键/值进行排序
# x2 = {'c': 1, 'a': 3, 'b': 2}
# print(dict(sorted(x2.items(), key=lambda x:x[1], reverse=True)))  # {'a': 3, 'b': 2, 'c': 1}
# print(dict(sorted(x2.items(), key=lambda x:x[0], reverse=True)))  # {'c': 1, 'b': 2, 'a': 3}


# ②list.sort()方法
# 语法：列表.sort(key=选择排序依据的函数, reverse=True|False)
#      列表的sort方法，其使用方法与数据容器通用函数sorted()相似
# 注意：[1]sort是list的方法；[2]sort方法改变列表自身内容，返回None
#
# x0 = [(1,'c'), (2,'b'), (3,'a')]
# x1 = x0.sort(key=lambda x:x[0], reverse=True)
# print(x1)  # None，返回空
# print(x0)  # [(3, 'a'), (2, 'b'), (1, 'c')]，按x[0]进行排序


# ③reversed()函数，选则数据容器、可迭代对象进行反转，不改变数据容器原本的值，返回可迭代的生成器对象
#
# x = [1, 2, 3]
# x1 = reversed(x)
# print(x)  # [1, 2, 3]，不改变原本的值
# print(x1)  # <list_reverseiterator object at 0x0000021877B1DAB0>，返回生成器对象
# print(list(x1))  # [3, 2, 1]，将生成器对象转化为list即可得到反转后的内容




# # (5)枚举与迭代

# ①enumerate()枚举函数
# enumerate 英文：v.枚举
# 语法：enumerate(可迭代对象)  # 注：可迭代对象包含数据容器
# 功能：返回一个枚举对象，其中每个元素都是(含引索, 值)的元组；使用时，即可以把enumerate对象转换为list、tuple、set，也可以直接使用for循环遍历其中元素
#
# object = enumerate([1, 2, 3, 4, 5])
# print(object)  # <enumerate object at 0x0000023031620C20>
# print(list(object))  # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# for index, value in enumerate(('a', 'b', 'c')):
#     print((index, value), end=' ')  # (0, 'a') (1, 'b') (2, 'c')




# # (6) map()函数、reduce()函数、filter()函数
# 注意：这些函数的参数均为(func, 可迭代对象)，map按函数映射，reduce按函数化简聚合，filter按函数过滤。
#     上述函数均不改变原本可迭代对象的值，返回新的对象存放处理后的值
# 上面的函数，可以类比与pyspark模块中，对rdd对象进行处理的函数：rdd.map(func)；rdd.reduceByKey(func)；rdd.filter(func)


# ①map()函数
# map 英文：v.映射
# 语法：map(func, 可迭代对象)
# 功能：将可迭代对象的元素(以func为依据)逐个处理，返回一个map对象。不改变原对待对象的值
# map对象属于迭代器类型，其中每个元素是原本可迭代对象经过func处理后的结果，可将map对象转换为list、tuple、set，也可以直接使用for循环遍历其中元素
#
# data = ["qwe asd", "zxc rty"]
# obj = map(lambda x: x.split(" "), data)
# print(obj)  # <map object at 0x0000015D308CDAB0>，返回迭代器对象
# print(list(obj))  # [['qwe', 'asd'], ['zxc', 'rty']]，可将map对象转化为list
# print(tuple(map(lambda x: x*10, [1, 2, 3])))  # (10, 20, 30)


# ②reduce()函数
# reduce 英文：v.约简、化简到最小
# 语法：reduce(func, 可迭代对象)
# 功能：将可迭代对象的两个元素(以func为依据)从左带有依次处理，实现聚合的过程，返回聚合结果
# 如：reduce(lambda x,y:x+y, [1,2,3,4,5])，计算过程为((((1+2)+3)+4)+5)
# 注意：reduce是模块functools中的函数
#
# from functools import reduce
# a = reduce(lambda x, y: x+y, [1, 2, 3, 4])
# print(a)  # 10
# print(reduce(lambda x, y: x*y, [2, 3, 4]))  # 24


# ③filter()函数
# filter 英文：v.过滤
# 语法：filter(func, 可迭代对象)
# 注意：func传入一个参数，返回bool值。 f:(T) -> bool
# 功能：函数对可迭代对象(以func为依据)逐个过滤处理，得到True的保留至返回值的filter可迭代对象中
#
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# obj = filter(lambda x: x >= 5, num)  # 匿名函数返回x>=5，即x>=5值为True，否则为False
# print(obj)  # 返回迭代器对象
# print(list(obj))  # [5, 6, 7, 8, 9]，过滤大于等于5的数
# print(list(filter(lambda x: not(x % 2), num)))  # [2, 4, 6, 8]，过滤偶数




# # (7) range()函数
# 语法：range([start,]stop[,step])  # 方括号表示可选
# start默认为0，step默认为1，左闭右开
# 注意：range本身也是一种可迭代对象，可以转换为数据容器或者用for循环迭代
#
# x = range(5)
# print(x)  # range(0, 5)，x是可迭代对象
# print(list(x))  # [0, 1, 2, 3, 4]
# print(list(range(1, 10, 2)))  # [1, 3, 5, 7, 9]




# # (8) zip()函数
# 语法：zip(iterable1, iterable2, ..., iterableN)  # zip的参数表示可迭代对象
# 功能：返回一个zip可迭代对象，zip对象的每个元素都是（参数中多个可迭代对象对应位置元素组成的元组）。
# 注意：返回的zip对象的元素个数取决于:参数的可迭代对象中最短的那个
#
# x = zip([1,2,3,4,5], 'abc', ('q','w','e','r'))
# print(x)  # <zip object at 0x0000020177AB7E00>，返回zip对象
# print(list(x))  # [(1, 'a', 'q'), (2, 'b', 'w'), (3, 'c', 'e')]，将参数中数据容器对应位置的元素组合到元组中，zip对象元素个数==参数最短的数据容器参数个数
# print(tuple(zip('123', 'abc', 'qwe')))  # (('1', 'a', 'q'), ('2', 'b', 'w'), ('3', 'c', 'e'))
# # 可以利用zip创建字典
# print(dict(zip(range(1,4), ['a', 'b', 'c'])))  # {1: 'a', 2: 'b', 3: 'c'}



