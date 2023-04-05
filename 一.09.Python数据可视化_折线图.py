"""
目录：
1.json数据格式
2.pyecharts模块介绍
3.pyecharts快速入门
4.数据处理
5.创建折线图
"""











### 1.json数据格式


## (1)json介绍：

# 什么是 json ?
# json是一种轻量级的数据交互模式。可以按照json指定的格式去组织和封装数据
# json本质上是一个带有特殊格式的【字符串】

# 主要功能：
# json就是一种在各个编程语言中流通的数据格式，【负责不同编程语言中的数据和交互】
# 不同的语言有不同的数据格式，想相互传递数据，需要通用的json
#   json类似于：国际通用语言 - 英语 ； 中国不同地区的通用语 - 普通话

# 用法：
# 若想用C语言接收Python的数据，需要先把C语言格式的数据转换为json格式的数据，之后再把json转化为Python的格式，给Python接收。
# 同理，若想用Python接收C语言数据，需要把C语言转换为json，之后再转换为Python语言






## (2)json数据格式化

## json数据的格式要求很严格，下面我们看一下它的要求：

# # json数据的格式可以是：
# {"name":"admin", "age":18}
#
# # 也可以是：
# [{"name":"admin", "age":18}, {"name":"root", "age":16}, {"name":"张三","age":20}]

# 我们发现，json要求的格式要么是字典，要么是列表，其元素为字典
# 这就是Python在不同语言中转换的优势，可以和json格式无缝切换






## (3)Python数据和Json数据的相互转换

# 步骤如下：

# # ① 导入json模块
# 语法：import json

# # ② 准备符合json格式要求的Python数据
# 语法：data = [{"name":"张三", "age":18}, {"name":"amy", "age":16}]

# # ③ 通过json.dumps(data)方法把Python数据转化为json数据
# 语法：data = json.dumps(data)
# 【dump】 英文  v.倾倒、转储
#
# print(data)  # '[{"name": "\u5f20\u4e09", "age": 18}, {"name": "amy", "age": 16}]'
# #我们可以看出，json的本质是把字典/列表直接转化为字符串，并把中文转换成编码形式。

# # ④ 通过json.loads(data)方法把json数据转化为Python数据
# 语法：data = json.loads(data)
# 【load】 英文  v.装上、加载



## 实操演示：
#
# import json
# data1 = [{'name':'张三', 'age':23}, {'name':'李四', 'age':24}, {'name':'王五', 'age':25}]
# data1_j = json.dumps(data1)
# print(data1_j)  # '[{"name": "\u5f20\u4e09", "age": 23}, {"name": "\u674e\u56db", "age": 24}, {"name": "\u738b\u4e94", "age": 25}]'
# print(type(data1_j))  # <class 'str'>
# # 可以看出json本质为字符串
#
# data2 = {'name':'张三', 'age':22}
# data2_j = json.dumps(data2, ensure_ascii=False)  # 这里不将中文转化为编码
# print(data2_j)  # '{"name": "张三", "age": 22}'
# print(type(data2_j))  # <class 'str'>
#
# s1_j = '[{"name": "\u5f20\u4e09", "age": 23}, {"name": "\u674e\u56db", "age": 24}, {"name": "\u738b\u4e94", "age": 25}]'
# s1 = json.loads(s1_j)
# print(s1)  # [{'name': '张三', 'age': 23}, {'name': '李四', 'age': 24}, {'name': '王五', 'age': 25}]
# print(type(s1))  # <class 'list'>
#
# s2_j = '{"name": "张三", "age": 22}'
# s2 = json.loads(s2_j)
# print(s2)  # {'name': '张三', 'age': 22}
# print(type(s2))  # <class 'dict'>

















### 2.pyecharts模块介绍

# 如果想要做出数据可视化效果图，可以借助pyecharts模块来完成

# 概况：
#   Echarts是个由百度开源的数据可视化，凭借良好的交互性，精巧的图标设计，得到了众多开发者的认可。
#   而Python是门富有表达力的语言，很适合用于数据处理。当数据分析遇上可视化时，pyecharts旧诞生了。


# 参考网站：
# pyecharts.org  -- 官网，有众多的中文文档供我们参考
# gallery.pyecharts.org  -- 画廊，提供各种可视化图标的成品展示

















### 3.pyecharts快速入门

## pyecharts完成一个基础的折线图：
## 步骤如下：

# # (1)导包
# from pyecharts.charts import Line # 折线图的包
# from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts  # 标题、图例、工具箱、视觉映射的控制选项
#
# # (2)创建一个折线图对象(获得了空的x轴y轴)
# my_line = Line()
#
# # (3)给折线图对象添加x轴数据
# my_line.add_xaxis(['一月', '二月', '三月', '四月'])
#
# # (4)给折线图对象添加y轴的名称和数据
# my_line.add_yaxis('月销量(吨)', [34, 21, 42, 32])
#
# # (5)设置全局配置项
# my_line.set_global_opts(
#     title_opts=TitleOpts(title="月销量展示", pos_left="50%", pos_bottom="1%"), # 控制标题名称，位置
#     legend_opts=LegendOpts(is_show=True), # 将图例调为可展示 (这里写不写一样，图例is_show默认True)
#     toolbox_opts=ToolboxOpts(is_show=True), # 将工具箱调为可展示
#     visualmap_opts=VisualMapOpts(is_show=True)  # 将视觉映射调为可展示
# )
#
# # (6)通过render方法将代码生成为图像
# my_line.render()



# 知识点补充：pycharts模块中有很多的配置选项
#   全局配置选项：针对图像进行配置  (标题、图例、工具箱等)
#   系列配置选项：针对具体的轴数据进行配置  (对xy轴数据进行个性化配置)
#
#
# 全局配置选项，可以通过set_global_opts方法进行配置，相应的选项和选项的功能如下：
#   全局配置项与图表类型无关，所有图表都通用：
#   title_opts：标题配置选项 (或者写成TitleOpts)
#   legend_opts：图例配置项
#   toolbox_opts：工具箱配置项
#   visualmap_opts：视觉映射
#   ...
# 若想具体了解其功能，请看网址pyecharts.org中的文档

















### 4.数据处理

# 首先我们要分析数据，D:\Python\python项目\python_learn\测试文档\折线图数据\美国
# 以上数据为json数据
# 我可以借助网页【ab173.com】对json进行处理
# 转换为Python数据并整理后,数据如下:
# {
#     "status":0,
#     "msg":"success",
#     "data":[
#         {
#             "name":"美国",
#             "trend":{
#                 "updateDate":[ ... ],
#                 "list":[
#                     {"name":"确诊", "data":[ ... ]},
#                     {"name":"治愈", "data":[ ... ]},
#                     {"name":"死亡", "data":[ ... ]},
#                     {"name":"新增确诊", "data":[ ... ]}
#                 ]
#             }
#         }
#     ]
# }






## 在我们分析完数据的基础上，我们要对数据进行处理
## 步骤如下：


# # (0) 导包
# import json
#
# # (1) 打开需处理的文件
# f_us = open("D:\Python\python项目\python_learn\测试文档\折线图数据\美国.txt", "r", encoding="UTF-8")
# data_us = f_us.read()  # 获得美国文件的全部内容
# # 我们可以注意到，文档中首尾有一部分非json的内容需要去除：首:【"jsonp_1629344292311_69436("】  尾:【");"】
#
# # (2) 去掉不合json规范的开头
# data_us = data_us.replace("jsonp_1629344292311_69436(", "")
#
# # (3) 去掉不合json规范的结尾
# # 由于结尾的 ");" 太普遍，若replace，说不定会将文本内容中的相同符合误改
# data_us = data_us[:-2]
#
# # (4) 将json数据转换为Python形式
# dict_us = json.loads(data_us)
#
# # (5) 获得 键trend 对应的值
# value_trend = dict_us['data'][0]['trend']
#
# # (6) 获取日期数据，用于x轴，取2020年(到包含313下标结束)
# us_x = value_trend['updateDate']
# us_x = us_x[:314]
# print(us_x)  # ['2.22', '2.23', '2.24',...]
#
# # (7) 获取确诊数据，用于y轴，取2020年(到包含313下标结束)
# us_y = value_trend['list'][0]['data'][:314]
# print(us_y)  # [34, 34, 34,...]
#
# # (8) 关闭文件
# f_us.close()


# 以上，我们就完成了图表的数据准备，接下来，就要进行图表的绘制

















### 5.创建折线图

## 在这里，我们参考上面数据处理中处理US数据的代码，进行改进，将对文件的处理封装成函数
## 并且完成折线图的创建
## 步骤如下：



# import json
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,ToolboxOpts,LabelOpts
#
#
# def get_xydata(file_name, head_str, data_num):
#     """
#     将传入的json文件进行处理，返回所需的xy轴数据的函数
#     :param file_name: 要处理的文件名
#     :param head_str: 要去除的文件头部内容
#     :param data_num: 要截取的日期所对应的行数
#     :return: x、y轴数据的列表信息
#     """
#     f = open(file_name, "r", encoding="UTF-8")
#     f_data = f.read()
#     f_data = f_data.replace(head_str, "")[:-2]  # 去首尾不和格式的内容
#     f_data = json.loads(f_data)  # 转为Python类型数据
#     value_trend = f_data['data'][0]['trend']
#     x = value_trend['updateDate'][:data_num]
#     y = value_trend['list'][0]['data'][:data_num]
#     f.close()
#     return x, y
#
# # 获得三个国家的xy轴数据
# us_x, us_y = get_xydata("D:\Python\python项目\python_learn\测试文档\折线图数据\美国.txt", "jsonp_1629344292311_69436(", 314)
# jp_x, jp_y = get_xydata("D:\Python\python项目\python_learn\测试文档\折线图数据\日本.txt", "jsonp_1629350871167_29498(", 314)
# in_x, in_y = get_xydata("D:\Python\python项目\python_learn\测试文档\折线图数据\印度.txt", "jsonp_1629350745930_63180(", 314)
#
# # 构建折线对象
# line = Line()
#
# # 添加x轴数据
# line.add_xaxis(us_x)
#
# # 添加y轴数据，并对y轴进行系列配置
# line.add_yaxis("美国确诊人数", us_y, label_opts=LabelOpts(is_show=False))  # 最后一个参数是系列配置选项
# line.add_yaxis("日本确诊人数", jp_y, label_opts=LabelOpts(is_show=False))  # 由于默认y轴值对显示，太乱了，这里将其关闭
# line.add_yaxis("印度确诊人数", in_y, label_opts=LabelOpts(is_show=False))
#
# # 配置全局选项
# line.set_global_opts(
#     title_opts=TitleOpts(title="2020年美日印三国疫情确诊人数折线图", pos_left="50%", pos_bottom="1%"),
#     toolbox_opts=ToolboxOpts(is_show=True),
# )
#
# # 生成图表
# line.render()