"""
目录：
1.基础柱状图
2.基础时间线柱状图
3.GDP动态柱状图绘制
(1)列表.sort() 方法补充
(2)绘制GDP动态柱状图
"""










### 1.基础柱状图

# 我们使用Bar构建柱状图。
# 柱状图的构建方法与折线图的方法相似，都是创建对象、添加x、y轴、配置选项、生成图表。
# 本篇我们要实现各国GDP的动态柱状图，使用需要将柱状图横过来，需要反转xy轴并将数字标签改到柱的右侧。
# 步骤如下:


# # 导包
# from pyecharts.charts import Bar
# from pyecharts.options import LabelOpts
#
# # 使用Bar构建基础柱状图对象
# bar = Bar()
#
# # 添加x、y轴
# bar.add_xaxis(['中国', '美国', '英国'])
# bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))  # label_opts参数是将数字标签显示在柱的右侧
#
# # 反转x轴和y轴
# bar.reversal_axis()
#
# # 绘图
# bar.render()

















### 2.基础时间线柱状图

# Timeline() - 时间线
# 柱状图描述的是分类数据，回答的是一个分类中[有多少？]这个问题，这是柱状图的主要特点；
# 同时柱状图很难动态的描述一个趋势性数据，这里pyecharts为我们提供了一种解决方案 - 时间线

# 如果说一个Bar、Line对象是一张图表的话，时间线就是创建一个一维的x轴，轴上的每一个点就是一个图表对象
# 时间轴：——o——o——o——o——o——o——o——o————>
# 上面就是一个时间轴，每个点表示一个图表对象



# ## 步骤如下：
#
# # 导包
# from pyecharts.charts import Bar, Timeline
# from pyecharts.options import LabelOpts
# from pyecharts.globals import ThemeType
#
# # 创建多个柱状图对象
# bar1 = Bar()
# bar1.add_xaxis(['中国', '美国', '英国'])
# bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
# bar1.reversal_axis()
#
# bar2 = Bar()
# bar2.add_xaxis(['中国', '美国', '英国'])
# bar2.add_yaxis("GDP", [50, 40, 30], label_opts=LabelOpts(position="right"))
# bar2.reversal_axis()
#
# bar3 = Bar()
# bar3.add_xaxis(['中国', '美国', '英国'])
# bar3.add_yaxis("GDP", [70, 60, 60], label_opts=LabelOpts(position="right"))
# bar3.reversal_axis()
#
#
# # 创建时间线对象
# GDP_timeline = Timeline({"theme":ThemeType.LIGHT})  # 创建时间线对象时，括号中可以放主题的字典，可以更改主题 (记得导包)
#
# # 为时间线添加柱状图对象
# GDP_timeline.add(bar1, "点1")  # 括号内是图标对象,时间节点名称
# GDP_timeline.add(bar2, "点2")
# GDP_timeline.add(bar3, "点3")
#
# # 自动播放设置
# GDP_timeline.add_schema(
#     is_auto_play=True,      # 是否自动播放
#     play_interval=1000,     # 自动播放的时间间隔 (单位：毫秒)
#     is_timeline_show=True,  # 是否在自动播放时，显示时间轴
#     is_loop_play=True       # 是否循环自动播放
# )
#
# # 绘图
# GDP_timeline.render()

















### 3.GDP动态柱状图绘制



## (1)列表.sort() 方法补充


# 知识点补充 -- 列表的sort方法
# 在前面我们学习过sorted函数，可以对数据容器进行排序
# 在后面的数据处理中，我们需要对列表进行排序，并指定排序规则，sorted就无法完成了，我们这里补充sort方法：
#
# 【语法：列表.sort(key=选择排序依据的函数, reverse=True|False)】
#       参数key：函数key作为列表的排序依据；接受一个函数（或一个lambda匿名函数），该函数【接受一个列表项】并【返回一个用于排序的键】。例如，如果想按字符串长度降序对列表进行排序，可以使用key=len
#       参数reverse：是否反转排序结果，默认升序
#
# 注意：由于列表本身可变，使用列表的方法都是直接改动列表内部的内容，返回None；【而不是】列表本身不变，返回新列表



# my_list = [['a',33], ['b', 55], ['c', 11]]
#
# # ① 定义排序方法函数作为key
# def choose_key(element): # key的函数的参数为列表中的一个元素
#     return element[1] # 返回下标1的数字，作为排序依据
#
# my_list.sort(key=choose_key, reverse=True)
# print(my_list)  # [['b', 55], ['a', 33], ['c', 11]]
#
#
# # ② key的函数也可以是lambda匿名函数
# my_list.sort(key=lambda element:element[1], reverse=False)
# print(my_list)  # [['c', 11], ['a', 33], ['b', 55]]










## (2)绘制GDP动态柱状图

# 动态图要求如下：
# 1.GDP单位为亿
# 2.有时间轴，以年份为时间轴的节点
# 3.x轴和y轴反转，同时每一年数据只有前8名国家
# 4.有标题，标题的年份会动态更改
# 5.设置了主题为LIGHT



# 大体思路分为数据处理和图表绘制
# 图表数据位置如下："D:\Python\python项目\python_learn\测试文档\动态柱状图数据\历年全球GDP数据.csv"
# 步骤如下：



# 导包

# 读取数据
f = open('D:\Python\python项目\python_learn\测试文档\动态柱状图数据\历年全球GDP数据.csv', 'r', encoding='GB2312') # 这里使用文件自身的编码格式，就不用UTF-8了
data_lines = f.readlines()
f.close()

# 数据处理
data_lines.pop(0)  # 删除第一条无关内容
data_list = []
for x in range(1960,2010):
    data_list.append({x:[]})
print(data_list)
for element in data_lines:
    element = element.split(',')
    #print(element)
    print(int(int(element[0])-1960))
    #print(data_list[int(element[0])-1960])
    #data_list[int(element[0])-1960][x].append([element[1], element[2].strip()])
print(data_list)
