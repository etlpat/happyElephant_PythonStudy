
#print("111","222")
#rint('111','222')#字符串可以单引号
#print("111"+"222")#连接字符串
#rint('1122"1122"')#打印带双引号
#print("122'1122'")#打印带单引号
#print("1122\"112\'qw\"")#转义字符打印但/双引号
#print("1122\n3344")#换行符
#print("""
#嗨嗨嗨
#嗨嗨
#来了嗷
#""")#三引号不仅是注释，还能被打印多行





"""
a = "张三"
b = "李四"
print("名字是"+a)
print("名字是"+b)
"""





# #乘方
# #print(2**3)# 2**3 为 2的三次方
#
# #导入函数库
# import math
# # 格式：math.函数名(...)
# print(math.log2(8))
#
# #下面利用乘方及math函数求一元二次方程的两根
# import math
# a=-1
# b=-2
# c=3
# print((-b+(b**2-4*a*c)**(1/2))/2/a)
# print((-b-math.sqrt(b**2-4*a*c))/2/a)







# # 字符串
# # 用 ” “ 或 ‘ ’ 引起来的内容为字符串
# # 字符串重每个符号占一个字符，转义字符整体占一个字符
#
# #计算字符串函数为 len()
# print(len('114514'))
# print(len("1919810"))
#
# # 通过索引获取字符串的字符（下标引用操作符[]）
# # 注：字符串的索引（下标）还是从0开始
# # 可以 "字符串"[]  也可以  数组名[]
# '12345'[2] #为 3
#
#
# s = "1919810"
# print("hello"[2])
# print("114"[2])
# print(s[5])
# print(s[len(s)-1])





# # 数据类型 - NoneType - 空置类型
# # 值为None，表示完全没有值
#
# print(type(None))




# # 布尔类型（bool）
# # 值为 True(1)和 False(0)
# # 记得首字母大写
#
# t1 = True
# t2 = False
# print(type(t1))
# print(type(t1))






# # 输入函数 input() 和类型转换函数 int() float() str()...
#
# # input("xxx") 函数从用户哪里获取输入
# # 其在屏幕上先打印字符串内容xxx,然后等用户输入。
# # input()函数的返回值即【字符串形式】的用户键入的内容
#
# a = input("请输入内容") #a的类型为字符串
# print("键入的内容为："+a)
#
#
# # 由于input()函数返回值为字符串，有时需要将其转换为特定的类型
# # int()函数可将字符串转换为整数
# # float()可将字符串转换为浮点型
# # str()将变量转换为字符串
# # 区别与C语言的强制类型转换，Py的类型转换为函数，括号在变量上int("a");而C语言强转为操作符，括号在类型上(int)a
#
# print(int("114") + 400)
# print(float("3.14")+1)
# print("字符串"+str("114514")+"hhh")
#
#
# # #input()与int()的应用
# age = input("请输入用户年龄：")
# print("用户年龄为"+age+"岁")
# age = int(age)+10
# print("用户十年后年龄为"+str(age)+"岁")
#
#
# # 计算用户BMI指数，BMI = 体重/(身高**input**2
# weight = float(input("请输入体重(kg):"))
# height = float(input("请输入身高(m):"))
# BMI = weight/(height**2)
# print("你的BMI指数为"+str(BMI))










# # 条件语句 if else
# # 注：条件的值为布尔值（True False）
# # Py语句通过缩进格数划分代码块（if下面的执行语句一般为4空格缩进）
#
#
# ## if条件语句如下
# #
# # if 条件:
# #     执行语句1
# #     执行语句2
# # else:
# #     执行语句3
#
#
# num = int(input("请输入你的成绩"))
# if num>=60:
#     print("恭喜你")
#     print("你及格了")
# else:
#     print("很遗憾")
#     print("你没及格")



# ## if条件语句的嵌套（也是通过缩进实现划分代码块）
# #
# # if 条件1:
# #     if 条件2:
# #         执行语句1
# #     else:
# #         执行语句2
# # else:
# #     执行语句3
#
#
# num = int(input("请输入你的成绩"))
# if num>0:
#     if num<60:
#         print("没及格")
#     else:
#         print("及格了")
# else:
#     print("无效成绩")



# ## if的多个条件判断（if/ elif/ else）
# #该语句思路和C语言一样，从上到下依次执行
# #
# # if 条件1:
# #     执行语句1
# # elif 条件2:
# #     执行语句2
# # elif 条件3:
# #     执行语句3
# # else:
# #     执行语句4
#
#
# num = int(input("请输入你的成绩"))
# if 0<num<60:
#     print("不及格")
# elif 60<=num<75: #注：和C语言必须用&&、||不一样，Py中表达式可以连续判断【60<=x<=100】
#     print("及格了")
# elif 75<=num<85:
#     print("良好")
# elif 85<=num<=100:
#     print("优秀")
# else:
#     print("离谱")



# # 计算用户BMI指数，BMI = 体重/(身高**input**2)
# # 并且判断身体肥胖程度
# weight = float(input("请输入体重(kg):"))
# height = float(input("请输入身高(m):"))
# BMI = weight/(height**2)
# print("你的BMI指数为"+str(BMI))
# if BMI <= 18.5:
#     print("偏瘦")
# elif 18.5 < BMI <= 25: # 可以连续判断
#     print("正常")
# elif 25 < BMI <= 30:
#     print("偏胖")
# else:
#     print("肥胖")









# # 逻辑运算符号（对布尔值进行运算）
# # and -- 与（&&）
# # or  -- 或（||）
# # not -- 非（!）
# # 注：和C语言一样，逻辑运算符优先级【not > and > or】；且逻辑运算符存在短路规则
#
#
# # 判断平年闰年
# year = int(input("请输入年份："))
# if not(year%4) and year%100 or not(year%400):
#     print("闰年")
# else:
#     print("平年")













# # 列表 - list
# # 一个空列表用一个方括号[]表示，若存放元素应用逗号将其隔开
# # 列表可以类比C的数组，但Py的列表可以放不同类型的数据
#
# None_list = []    #这是空列表
# num_list = [1,2,3,4,5]    #不同元素间用逗号隔开
# list_1 = [1,"abc",3.14,True,None]    #列表可存放不同类型元素
# print(list_1)
#
#
#
# # 列表和函数一样，可用 len() 函数求长度，返回列表中元素的数量
# # 列表可用【索引】获得特定位置的元素；列表索引从0开始
#
# shopping_list = ["键盘","显示器","鼠标"]
# print(shopping_list)    # 打印整个列表 ['键盘', '显示器', '鼠标']
# print(len(shopping_list))    # 打印元素个数 3
# print(shopping_list[0])    # 打印0位置的元素 键盘
# print(shopping_list[1])
# print(shopping_list[2])




# # 若像往定义号的列表中[添加东西]，可以用针对列表的【方法】 - append
# # 方法与函数类似，都是用于实现某个特定功能
# # 【方法】格式:  对象.方法名(...)  如 num_list.append(114)
# # 【函数】格式:  函数名(对象)  如 len(num_list)
#
#
# # 列表 list 与 str/int/float/bool 等类型的区别是：列表是可变的
# # 如何结解释上面这句话？
# # 以str型的"abc"为例，"abc"本身就是"abc"，我们把"abcd"赋给存放"abc"的变量，改变的是变量，而不是改变"abc"
# # 但是list型的[1,2,3]，我们可以append一个4进去，list变为[1,2,3,4]，列表本身改变
#
#
# # 下面以列表名为list_1为例
# # 往列表中加元素 - 【方法】append
# # list_1.append(123)
# # 删除列表中元素 - 【方法】remove
# # list_1.remove(123)
#
#
#
# shopping_list = ["显示器","鼠标"]
# shopping_list.append("键盘")
# print(shopping_list)    # 打印 ['显示器', '鼠标', '键盘']
# shopping_list.remove("显示器")
# print(shopping_list)    # 打印 ['鼠标', '键盘']



# 补充：Py还有许多关于列表的内置函数
# max(num_list)    # 返回列表里元素的最大值
# min(num_list)    # 返回列表里元素的最小值
# sorted(num_list)    # 返回(小到大)排序好的新列表，同时不改变原列表
# ......



# shopping_list = []
# shopping_list.append("键盘")
# shopping_list.append("键帽")
# shopping_list.append("显示器")
# print(shopping_list)
# shopping_list.remove("键帽")
# print(shopping_list)
# shopping_list[1] = "电竞椅"
# print(shopping_list, "\n")
#
# price_list = [800,1024,35,399]
# print(max(price_list))
# print(min(price_list))
# sorted_list = sorted(price_list)
# print(sorted_list)
# print(price_list)  # 可见排序函数不改变列表内容











# # 【字典】 - dict (dictionary缩写)
# # 字典用于储存【键值对】 - 【键(key) : 值(value)】，字典可变
# # 空的字典用一对花括号表示 {},多个键值对用逗号将其隔开
# # 如下
# contacts = {"小明":"114514","小花":"1919810"}
#
# # 字典名[键] - 可获得 "键" 的 “值”
# contacts["小明"]  # 获得小明的"值" - 114514
# # 注：“键”的类型必须为不可变的 - 如列表可变，就不能作为键；整数、浮点、字符串等不可变，可作为键
#
# print(contacts["小明"]) # 打印值





# 【元组】 - tuple
# 元组是可放多个元素，但【不可变】的结构；相当于不可变的列表
# 空的元组用一对圆括号表示 ()，多个键值对用逗号将其隔开
# 由于元素不可变，所以不能对其使用添加append、删除remove等方法
# 如下
# tuple1 = ("键盘","鼠标")
# 由于元素不可变的属性，我们经常拿它充当键值对的“键”
# 如下
# dictionary1 = {("沙发","红"):"37.5", ("沙发","黑"):"57.99", ("茶几","棕"):"114"}





## 下面是对字典的一些操作

# # 获得字典中键值对个数 - len()
# contacts = {"小明":"114514","小花":"1919810"}
# print(len(contacts)) # 2



# # 字典中常用的 方法
# # 字典名.keys()  - 返回字典中所有键， 全部键存放在列表中
# # 字典名.values()  - 返回字典中所有值， 全部值存放来列表中
# # 字典名.items()  - 返回字典中所有键值对， 每对键值对的键与值存放在一个元组中，全部元组一个个存放在列表中
#
# contacts = {"小明":"114514","小花":"1919810","小李":"15478"}
# print(contacts.keys())    # dict_keys(['小明', '小花', '小李'])
# print(contacts.values())    # dict_values(['114514', '1919810', '15478'])
# print(contacts.items())    # dict_items([('小明', '114514'), ('小花', '1919810'), ('小李', '15478')])
# # 从上面打印值可看出，keys/values将键/值存放在列表中
# # items将键值对的键.值存放到元组中，再将元组存放到列表中



# # 字典中添加键值对
# # 格式: 字典名[键] = 值
# # 注意，对键赋值来覆盖原先的值也是该操作
#
# contacts = {"小明":"114514","小花":"1919810"}
# print(contacts)
# contacts["张三"] = "12315" # 在字典中添加"张三"键值对
# print(contacts)



# # 判断某个"键"是否存在 - in
# # 格式: 【键名 in 字典名】 - 键存在返回True，不存在返回False
#
# contacts = {"小明":"114514","小花":"1919810"}
# print("小明" in contacts) # True



# # 删除键值对 - del
# # 格式: del 字典名[键]
# # 可以将键和对应的值在字典里删除;若键本身不存在,则报错
#
# contacts = {"小明":"114514","小花":"1919810"}
# del contacts["小明"] # 将小明键值对从字典中删除
# print(contacts)



# name_dict = {"老大":"12345","老二":"123446","老三":"12347"}
# name_dict["老四"] = "12348"
# name_dict["老五"] = "12349"
# name_dict["老六"] = "12340"
# print(name_dict)
# name = input("请输入要查找的用户名字:")
# if name in name_dict:
#     print("你查询的"+name+"电话号码为:\n"+name_dict[name])
# else:
#     print("未收录要查询的人")
#     print("本通讯录收录人数为:"+str(len(name_dict))+"人")












# for循环
# 格式如下
#
# for 变量名 in 可迭代对象:
#     # 对每个变量执行的操作
#     # ...
#
# 注：上面变量名是自己取的，每次循环，变量名会被依次赋值为列表里的每一个元素，直到最后一个
# 下面代码块以缩进来判断是否在for循环内



# # for循环对列表的使用
# temperature_list = [36.4, 36.6, 37.4, 35.6, 36.1, 37.1, 36.2]
# num = 0
# for temperature in temperature_list:
#     if temperature > 37:
#         num += 1
# print("体温过高人数为："+str(num)+"人")





# temperature_dict = {"111":36.4, "112":36.6, "113":37.4, "114":35.6, "115":36.1, "116":37.1, "117":36.2}
# print(temperature_dict.items())
# # 这是打印结果：dict_items([('111', 36.4), ('112', 36.6), ('113', 37.4), ('114', 35.6), ('115', 36.1), ('116', 37.1), ('117', 36.2)])
# # 注意结果为列表，列表元素为元组



# # for循环对字典的使用
# temperature_dict = {"111":36.4, "112":36.6, "113":37.4, "114":35.6, "115":36.1, "116":37.1, "117":36.2}
# # 上面体温表前面是工号，后面是温度
# num = 0
# for (staff_id,temperature) in temperature_dict.items():
# # for循环跟了两个变量：temperature_list.items()将每个键值对以元组的形式存放到列表中，在在每次列表的循环中，前后两个变量存放元组中的键与值
#     if temperature >= 37:
#         print("工号"+staff_id)
#         num += 1
# print("体温过高人数为："+str(num)+"人")
#
#
#
# # 上面那段代码还可以有这种写法
# temperature_dict = {"111":36.4, "112":36.6, "113":37.4, "114":35.6, "115":36.1, "116":37.1, "117":36.2}
# # 字典中键值对（工号:温度）
# num = 0
# for temperature_tuple in temperature_dict.items():  # 字典名.items先将字典转换为元素为元组的列表
# # temperature_tuple元组中，下标为0的是工号，下标为1的是温度
#     if temperature_tuple[1] >= 37:
#         print("工号"+temperature_tuple[0])
#         num += 1
# print("体温过高人数为："+str(num)+"人")







# # range()
# # range() 用来表示整数数列
# # range(5, 10) 括号里第一个数字表示起始值，最后一个数字表示结束值（结束值不在序列范围内）
# # 即 range(5,10) 左闭右开，取值范围相当于[5, 10)
#
# # 若 range() 中只放1个值，起始值默认为0
# # 如 range(10) ，值的范围是[0, 10)
#
# # range还可以包含第三个参数，表示步长(每次跨几个数字)，不写默认为1
#  # range(5,10,2) 即步长为 2，其中值为 5 7 9
#
#
#
# for i in range(5,10):
#     print(i) # 打印 5~9
#
# for i in range(5,10,2):
#     print(i) # 打印 5 7 9
#
#
# sum = 0
# for i in range(1,101):
#     sum += i   # 1到100求和
# print(sum)  #值为5050











# # while循环
# # 格式如下
# #
# # while 条件A
# #     行动B
# #
# # 当条件A为True,执行循环语句，当条件为False，退出循环
# # 大部分情况while和for是可以相互转换的，但当循环结束条件未知时，如记录亮度，当环境亮度低于一定值时结束循环，即用while
#
#
# a = 1
# sum = 0
# while a<=100:
#     sum += a
#     a += 1
# print(sum)  # 打印5050



# # 各种循环打印列表内容
# list1 = ['嗨','嗨','嗨','来','了','嗷','\n']
#
# for x in list1:
#     print(x)
#
# for i in range(len(list1)): # range()中只放1个值，起始值默认为0
#     print(list1[i])
#
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1



# # while循环实现求数字平均值，输入OK结束
# sum = 0
# num = 0
# x = input("请输入求平均值的数字，OK结束输入:")
# while "OK" != x:
#     sum += float(x)
#     num += 1
#     x = input("请输入求平均值的数字，OK结束输入:")
# if num == 0:
#     print("平均数为：0")
# else:
#     print("平均数为"+str(sum/num))












# 如何在一段不变的句子中插入部分可变的变量？


# # 用循环实现
# student_list = [("张三",97),("李四",55),("王五",76)]
# for stu_tuple in student_list:
#     print("学生姓名为：" + stu_tuple[0] + "；成绩为 "+str(stu_tuple[1]))



# # 用 .formate-方法 在文章结尾指定文中要替换的对象
#
# student_list = [("张三",97),("李四",55),("王五",76)]
# for stu_tuple in student_list:
#     massage = """学生姓名为：{0}；成绩为 {1}""".format(stu_tuple[0],stu_tuple[1])
#     print(massage)
# # format:格式化  在字符串中添加{0}{1}，字符串末添加.format()，括号中根据对应下标填入相应的替换对象，即可对特定位置内容进行替换



# # .format()根据关键字来替换对象
#
# student_list = [("张三",97),("李四",55),("王五",76)]
# for stu_tuple in student_list:
#     massage = """学生姓名为：{name}；成绩为 {grade}""".format(name = stu_tuple[0],grade = stu_tuple[1])
#     print(massage)
# # 这样是根据关键字对应，无所谓format中替换对象的位置



# # 可以使用 f-字符串 对字符串内容进行替换
# student_list = [("张三",97),("李四",55),("王五",76)]
# for stu_tuple in student_list:
#     name = stu_tuple[0]
#     grade = stu_tuple[1]
#     massage = f"""学生姓名为：{name}；成绩为 {grade}"""
#     print(massage)
# # 使用f字符串，对变量赋值，在把{变量}放到字符串中，即可替换字符串内容



# student_list = [("张三",97.69),("李四",55.55),("王五",76.99)]
# for stu_tuple in student_list:
#     massage = """学生姓名为：{0}；成绩为 {1:.1f}""".format(stu_tuple[0],stu_tuple[1])
#     print(massage)
# # 当format中变量为浮点/整型时，不用转化为字符串也能将其打印出来
# # 当变量为浮点数时，可以{数字:.2f}规定保留几位小数，表达式同理









# DRY原则：Don't Repeat Yourself # 不要做代码复读机
# 所以要学会封装函数

# # Py中定义函数的格式：
#
# def f():
#     #接下来时函数的执行步骤
#     #...
#
# # 定义函数时，内部代码不会被执行，只有在调用函数时代码会被执行

# 和C一样，py函数中创建的变量为临时变量，出函数时被删除释放空间
# 不写return时，默认返回None



# # 以下面计算扇形面积的函数为例
#
# def s(angle,R):
#     return angle / 360 * 3.14 * R**2
#
# stctor_list = [(180,5),(120,9),(270,8)]  # 存放扇形(角度,半径)的函数
# for (a,r) in stctor_list:
#     print("角度为", a, "，半径为", r, "的扇形面积为", s(a,r))



# # 用函数计算BMI的函数，函数名为 calculate_BMI
# # 1.计算BMI
# # 2.执行过程中打印一句化，“您的BMI分类为：xx”
# # 3.返回BMI
#
# def calculate_BMI(weight,height):
#     BMI = weight/height**2
#     if BMI <= 18.5:
#         category = "偏瘦"
#     elif BMI <= 25:
#         category = "正常"
#     elif BMI <= 30:
#         category = "偏胖"
#     else:
#         category = "肥胖"
#     print(f"您的BMI分类为{category}")
#     return BMI
#
# weignt = float(input("请输入体重(kg):"))
# height = float(input("请输入身高(m):"))
# BMI = calculate_BMI(weignt,height)
# print("BMI为"+str(BMI))













# Py模块引入
# import:进口、输入、导入
# 下面是三种格式


# # 1.import
# #
# # 格式：【 import 模块名 】
# # 之后用模块内函数/变量时，【 模块名.函数名 】/【 模块名.变量名 】
#
# import statistics
# print(statistics.median([19, -3, 89]))
# print(statistics.mean([19, -3, 89]))



# # 2.from...import...
# #
# # 格式：【 from 模块名 inport 函数名/变量名】 若多个函数名、变量名时，用逗号分隔
# # 之后再用被引入的函数/变量时，不用再带上模块名
#
# from statistics import mean,median
# print(median([19, -3, 89]))
# print(mean([19, -3, 89]))



# # from...import *
# #
# # 格式：【from 模块名 inport *】 会把模块内所有内容都进行引入
# # 之后用该模块内所有函数/变量时，都不用加模块名了
# #(占空间，且引入函数名/变量名多，容易造成命名冲突，不推荐使用)
#
# from statistics import *
# print(median([19, -3, 89]))
# print(mean([19, -3, 89]))











# ## 类 - class
# # class: 类别 ，把..分类
# # 再定义类时，Py用的是Pascal命名法，用大写字母来分隔单词（除了Pascal命名法，还有下划线命名法，即用下划线分隔单词）
#
# # 类定义的格式:
#
# class NameOfClass:
#     #接下来是一些定义类的代码
#     #...
#



# # 上代码：
#
# class CuteCat:
#     # 创建新对象，并定义对象属性(规定第一个变量为self - 把属性绑定到对象自身上)
#     def __init__(self, cat_name, cat_age, cat_color): # 构造对象的属性，必须命名为 __init__()，括号中可放任意参数，第一个参数默认为self，用于表示对象自身，不用手动传入，把属性的值绑定再实例对象上
#         self.name = cat_name # 注意将参数值赋给 self.name ，说明是对象的name属性的值
#         self.age = cat_age
#         self.color = cat_color
#
#     # 定义对象拥有的方法(规定第一个变量为self - 去获取、修改对象属性)
#     def speak(self):
#         print(f"小猫{self.name}的叫声是：" + "喵~" * self.age) # 字符串乘整数，表示重复整数次的字符串，这里表示猫几岁就叫几次
#
#     def think(self, imagine):
#         print(f"小猫{self.name}在想:'{imagine}'")
#
#
#
# # 类名(变量1,变量2...)可以创建新对象
# cat1 = CuteCat("jimmy", 3, "green") # 创建 CuteCat 类的对象cat1,并赋属性值
# print(f"猫猫的名字为{cat1.name},年龄为{cat1.age},花色为{cat1.color}")
#
# # 对象的方法: 对项名.方法名(参数)
# cat1.speak()
# cat1.think("嗨嗨，吃饱啦!")





# # 实践：定义一个学生类
# # 要求：
# # 1.属性包括姓名、学号，以及语数英三科成绩
# # 2.能够设置学生某项科目的成绩
# # 3.能够打印出该学生的所有科目的成绩
#
# class Student:
#     def __init__(self, stu_name, stu_id):
#         self.name = stu_name
#         self.id = stu_id
#         self.grade = {"语文":0, "数学":0, "英语":0}
#
#     def set_grade(self, subject, subject_grade):
#         if subject in self.grade:
#             self.grade[subject] = subject_grade
#         else:
#             print(f"你输入的{subject}科目不存在")
#
#     def print_grade(self):
#         for (subject,subject_grade) in self.grade.items():
#             print(f"该学生{subject}的成绩为:{subject_grade}分")
#
#
# student1 = Student("小明","1234567")
# print(f"学生名为{student1.name},学号是：{student1.id},各科成绩初值为:{student1.grade}")
# student1.set_grade("语文",80)
# student1.set_grade("数学",60)
# student1.set_grade("英语",70)
# student1.print_grade()








# # 类的继承
# #
# # 先正常定义一个类作为父类，之后定义子类时:
# # class 子类名(父类名):
# #     #定义类中内容
# #     #...
# #
# # # 关于类的继承的逻辑：
# # # 有限看子类有没有该方法，若子类中有，则使用子类方法。若子类没有，则向上找父类的同名方法。
# # # 若在子类中写__init__方法，则创建子类实例时，优先调用子类的构造函数，所以要在子类__init__函数中使用super().方法。super会返回当前类的父类
#
#
# class Mammal: # 哺乳类 - 作为父类
#     def __init__(self, name, sex):
#         self.name = name
#         self.sex = sex
#         self.num_eyes = 2
#
#     def breathe(self):
#         print(self.name + "在呼吸")
#
#     def think(self, imagine):
#         print(f"{self.name}在想:'{imagine}'")
#
#
# class Human(Mammal):
#     def __init__(self, name, sex):
#         super().__init__(name, sex)  # super()【返回当前类的父类】，这里使用super继承父类中的__init__函数
#         self.has_tail = False
#
#     def read(self):
#         print(f"{self.name}在阅读")
#
#
# class Cat(Mammal):
#     def __init__(self, name, sex):
#         super().__init__(name, sex)
#         self.has_tail = True
#
#     def scratch_sofa(self):
#         print(f"{self.name}在挠沙发")








# # 类继承的练习
# # 员工分为两类:全职员工 FullTimeEmployee 、兼职员工 PartTimeEmployee
# # 全职和兼职员工都有”姓名 name“、”工号 id“属性，都具备”打印信息 print_info“(打印姓名、工号)方法
# # 全职有"月薪 month_salary"属性
# # 兼职有"日新 daily_salary"属性、”每月工作天数 work_days“的属性
# # 全职和兼职都有"计算月薪 calculate_nobthly_pay"的方法，但计算过程不一样
#
# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def print_info(self):
#         print(f"姓名为:{self.name},工号为:{self.id}")
#
#
# class FullTimeEmployee(Employee):
#     def __init__(self, name, id, month_salary):
#         super().__init__(name, id)
#         self.month_salary = month_salary
#
#     def calculate_nobthly_pay(self):
#         return self.month_salary
#
#
# class PartTimeEmployee(Employee):
#     def __init__(self, name, id, daily_salary, days):
#         super().__init__(name, id)
#         self.daily_salary = daily_salary
#         self.work_days = days
#
#     def calculate_nobthly_pay(self):
#         return self.daily_salary * self.work_days
#
#
# zhangsan = FullTimeEmployee("张三", "114514", 6000)
# lisi = PartTimeEmployee("李四", "1919810", 250, 15)
# zhangsan.print_info()
# lisi.print_info()
# print(f"{zhangsan.name}每月工资为:{zhangsan.calculate_nobthly_pay()}")
# print(f"{lisi.name}每月工资为:{lisi.calculate_nobthly_pay()}")


