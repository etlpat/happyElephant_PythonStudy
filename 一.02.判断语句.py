"""
目录：
一、布尔类型和比较运算符
二、if语句的基本格式
三、if else语句
四、if elif else语句
五、判断语句的嵌套
六、实战案例
"""






# 一、布尔类型和比较运算符
#
# 布尔类型 - bool
# 布尔类型的字面量只有两个：True 和 False
# True表示真，本质是数字1
# False表示假，本质是数字0

# print(type(True))  #<class 'bool'>
# print(int(True))  # 1
# print(int(False))  # 0




# 注意：非0值转换为bool值为True，0转换为bool值为False
# print(bool(3))  # True
# print(bool(-1))  # True
# print(bool(0))  # False
# print(bool("ass"))    # True




# #比较运算符的运算结果是布尔类型
#  ==  !=  >  <  >=  <=
#
# print(2 >= 1)  # True
# print(2 <= 1)  # False
# print("abc" == "abc")  # True  ##注意！和C不用，【py可以用比较运算符来比较字符串】
# print("abc" >= "abb")  # True  ##    字符串比较规则：先逐个字母进行比较，直到找到不同的字母，比较其ASCII大小









# 二、if语句的基本格式

# 格式如下：

# if 条件:
#     执行语句
#     ...

# 注意：【1】不要把if条件后面的 冒号: 丢了
#     【2】py通过空格划分代码块，习惯上来讲是四个空格


# age = 10
# if age < 18:
#     print("未成年")
#     print("孩子还小")



## 注意：
# if "qwer":
#     print(1) # 1
#
# print(bool("qwer")) # True

# 上面代码可以看出，非0(包括字符串)的布尔类型都为True









# 三、if else语句

# 格式如下

# if 条件:
#     执行语句
#     ...
# else:
#     执行语句
#     ...

# else: 后面不用写判断条件，但是记得写冒号
# else代码块同样以四个空格为缩进


# age = int(input("请输入年龄："))
# if age < 18:
#     print("未成年")
#     print("孩子还小")
# else:
#     print("成年")









# 四、if elif else语句

# 格式如下

# if 条件1:
#     执行语句1
#     ...
# elif 条件2:
#     执行语句2
#     ...
# else:
#     执行语句3
#     ...

# 注意：判断是有顺序的，从上到下依次匹配。
#      符合上面的条件，执行上面的语句，就不会执行下面的了



# age = int(input("请输入年龄："))
# if age < 18:
#     print("未成年")
# elif 18 <= age < 30:  # 注意：Py支持连续判断
#     print("青年")
# elif 30 <= age < 55:
#     print("中年")
# else:
#     print("老年")



# # 三次机会的猜数字
# num = 10
# if int(input("请猜一个数字:")) == num:
#     print("猜对了，一次猜中")
# elif int(input("猜错了，请再猜一个数字:")) == num:
#     print("猜对了，两次猜中")
# elif int(input("猜错了，请再猜一个数字:")) == num:
#     print("猜对了，三次猜中")
# else:
#     print(f"三次全猜错了，数字是{num}")









# 五、判断语句的嵌套

# if 条件1:
#     if 条件2:
#         执行语句1
#     else:
#         执行语句2
# else:
#     执行语句3



# #游乐设施买票
# if int(input("你的身高是多少：")) > 120:
#     print("身高过高，不够免费条件\n但是若vip等级>3可免费")
#     if int(input("请输入你的vip等级：")) > 3:
#         print("vip等级达标，恭喜免费！")
#     else:
#         print("Sorry,你需要买票")
# else:
#     print("恭喜你能免费游玩")



# 公司领取奖励条件：1.年龄在18到30间；2.入职时间大于两年，或级别大于3

# if 18 <= int(input("请输入年龄：")) <30:
#     print("你的年龄达标了")
#     if int(input("请输入入职时间：")) > 2:
#         print("恭喜你，年龄和入职时间达标，可领奖")
#     elif int(input("你的工龄未达标\n请输入级别：")) >3:
#         print("恭喜你，年龄和等级达标，可领奖")
#     else:
#         print("您的条件未达标，无法领奖")
# else:
#     print("您的条件未达标，无法领奖")



# # 或者可以使用逻辑运算来化简
# if (18 <= int(input("请输入年龄：")) <30) and (int(input("恭喜哦，年龄达标\n请输入入职时间：")) > 2 or int(input("你的工龄未达标\n请输入级别：")) >3):
#     print("恭喜你，条件达标，可以领奖")
# else:
#     print("您的条件未达标，无法领奖")









# 六、实战案例

# 猜数字
# 案例要求：
# 1.数字随机产生
# 2.三次机会猜数字，用三次嵌套判断实现
# 3.每次猜不中，都会提示大了或者小了

# # 产生随机数代码如下
# import random
# num = random.randint(1,10)



# import random
# num = random.randint(1,10)
# guess = int(input("请输入数字："))
# if  guess== num:
#     print("一次猜中了！")
# else:
#     if guess > num:
#         print("猜大了")
#     else:
#         print("猜小了")
#     guess = int(input("请输入数字："))
#     if guess == num:
#         print("两次猜中了！")
#     else:
#         if guess > num:
#             print("猜大了")
#         else:
#             print("猜小了")
#         guess = int(input("请输入数字："))
#         if guess == num:
#             print("三次猜中了！")
#         else:
#             print("猜错了，机会用完了")
