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




## pyecharts基础入门：

# 导包
from pyecharts.charts import Line

# 创建一个折线图对象
my_line = Line()

# 给折线图对象添加x轴数据
my_line.add_xaxis(['一月', '二月', '三月', '四月'])

# 给折线图对象添加y轴数据
my_line.add_yaxis('销量(吨)', [34, 21, 42, 32])

# 设置全局配置项

# 通过render方法将代码生成为图像
my_line.render()




# 知识点补充：pycharts模块中有很多的配置选项
#   全局配置选项：针对图像进行配置  (标题、图例、工具箱等)
#   系列配置选项：针对具体的轴数据进行配置  (对xy轴数据进行个性化配置)
#
#
# 全局配置选项，可以通过set_global_opts方法进行配置，相应的选项和选项的功能如下：
# 全局配置项与图表类型无关，所有图表都通用
#   TitleOpts：标题配置选项
#   LegendOpts：图例配置项
#   ToolboxOpts：工具箱配置项






### 3.pyecharts快速入门












### 4.数据处理
### 5.创建折线图

