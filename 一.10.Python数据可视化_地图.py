"""
目录：
1.基础地图使用
2.疫情地图-国内疫情地图
3.疫情地图-省级疫情地图
"""










### 1.基础地图使用

## 想要更仔细的解释，可以去pyecharts.org看文档
## 地图基本使用方法如下：


# # (1)导包
# from pyecharts.charts import Map
# from pyecharts.options import  VisualMapOpts
#
# # (2)准备地图对象
# map = Map()
#
# # (3)测试用数据
# data = [  # 注意省字符串的名称要与地图默认省的名称保持一致
#     ("北京市", 99),
#     ("上海市", 199),
#     ("广东省", 299),
#     ("山西省", 399),
#     ("山东省", 499),
# ]
#
# # (4)添加数据
# map.add("测试地图", data, "china") # 地图名称、地图数据、地图类型
#
# # 设置全局选项
# map.set_global_opts(
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,  # 允许手动校准地图颜色显示的范围
#         pieces=[ # 这里是更改省份颜色对应的区间
#             {"min":1, "max":9, "label":"1-9", "color":"#CCFFFF"},     # 想查看颜色编码，找rgb颜色对照表 (之前的ab173网页上，前端中就能找出来)
#             {"min":10, "max":99, "label":"1-9", "color":"#FF6666"},   # lable:标签，控制每段的中文文字标签
#             {"min":100, "max":500, "label":"1-9", "color":"#990033"}
#         ]
#     )
# )
#
# # (5)生成地图
# map.render()

















### 2.疫情地图-国内疫情地图

# 首先我们分析数据，地图的数据在"D:\Python\python项目\python_learn\测试文档\地图数据\疫情.txt"中
# json数据分析需要利用网站进行，这里我们忽略分析的步骤
# 下面我们直接实现疫情地图，大体思路分为数据处理与图像构建两部分
# 步骤如下：


# # 导包
# import json
# from pyecharts.charts import Map
# from pyecharts.options import  TitleOpts, VisualMapOpts
#
#
# ### <一.处理数据>
#
# # 读取数据文件
# f = open("D:\Python\python项目\python_learn\测试文档\地图数据\疫情.txt", 'r', encoding='UTF-8')
# data = f.read()
# f.close()
#
# # 取各省份数据
# data = json.loads(data)  # 将json转化为Py字典
# province_list = data["areaTree"][0]["children"]  # 获得了存放省份数据的列表
#
# # 组装各省份的确诊人数到元组，并封装到列表中
# data_list = []
# for province_dict in province_list:
#     name_str = province_dict["name"]
#     if name_str == "北京" or name_str == "天津" or name_str == "上海" or name_str == "重庆":
#         name_str += "市"
#     elif name_str == "内蒙古" or name_str == "西藏":
#         name_str += "自治区"
#     elif name_str == "新疆":
#         name_str += "维吾尔自治区"
#     elif name_str == "宁夏":
#         name_str += "回族自治区"
#     elif name_str == "广西":
#         name_str += "壮族自治区"
#     elif name_str == "香港" or name_str == "澳门":
#         name_str += "特别行政区"
#     else:
#         name_str += "省"
#     data_list.append((name_str, province_dict["total"]["confirm"]))
#
#
# ### <二.构建图像>
#
# # 创建地图对象
# map = Map()
#
# # 添加数据
# map.add("各省份确诊人数", data_list, "china")
#
# # 设置全局选项，制定分段的视觉映射
# map.set_global_opts(
#     title_opts=TitleOpts(title="全国疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True, #是否手动分段
#         pieces=[
#             {"min":1, "max":99, "label":"1~99人", "color":"#c9da67"},
#             {"min":100, "max":999, "label":"100~999人", "color":"#d8b94b"},
#             {"min":1000, "max":4999, "label":"1000~4999人", "color":"#d8904b"},
#             {"min":5000, "max":9999, "label":"5000~9999人", "color":"#e8663b"},
#             {"min":10000, "max":99999, "label":"10000~99999人", "color":"#e93b1c"},
#             {"min":100000, "label":"100000人以上", "color":"#ac2f3f"}, # 不写max表示无上限
#         ]
#     )
# )
#
# # 生成图表
# map.render("全国疫情地图.html") # render语句中可填写html文件的名称

















### 3.疫情地图-省级疫情地图


# # 导包
# import json
# from pyecharts.charts import Map
# from pyecharts.options import  TitleOpts, VisualMapOpts
#
# # 文件读取
# f = open("D:\Python\python项目\python_learn\测试文档\地图数据\疫情.txt", "r", encoding='UTF-8')
# date = f.read()
# f.close()
#
# # 文件处理
# date = json.loads(date)
# shanxi_data = date['areaTree'][0]['children'][21]['children']
#
# # 获取城市列表
# city_list = []
# for city_data in shanxi_data:
#     city_list.append((city_data['name']+"市", city_data['total']['confirm']))
#
# # 构建地图
# shanxi_map = Map()
#
# # 添加数据
# shanxi_map.add('山西省疫情分别', city_list, "山西")
#
# # 设置全局选项
# shanxi_map.set_global_opts(
#     title_opts=TitleOpts(title="山西省疫情地图"),
#     visualmap_opts=VisualMapOpts(
#         is_show=True,
#         is_piecewise=True,
#         pieces=[
#             {"min":1, "max":99, "label":"1~99人", "color":"#c9da67"},
#             {"min":100, "max":999, "label":"100~999人", "color":"#d8b94b"},
#             {"min":1000, "label":"1000人以上", "color":"#d8904b"},
#         ]
#     )
# )
#
# # 绘图
# shanxi_map.render("山西省疫情地图.html")
