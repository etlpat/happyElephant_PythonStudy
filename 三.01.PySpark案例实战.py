"""
目录：
1.前言介绍
2.基础准备
3.数据输入[得到RDD对象]
4.数据计算
5.数据输出
6.综合案例
"""


"""
pyspark方法汇总：
① 数据输入：
sc.parallelize
sc.textFile
② 数据计算：
rdd.map
rdd.flatMap
rdd.reduceByKey
rdd.filter
rdd.distinct
rdd.sortBy
③ 数据输出：
rdd.collect
rdd.reduce
rdd.take
rdd.count
rdd.saveAsTextFile
"""













### 1.前言介绍

# Spark是什么？
# 定义：Apache Spark是用于大模型数据处理的统一分析引擎
# 简单来说，Spark是一款分布式的计算框架，用于调度成百上千的服务器集群，计算TB、PB乃至EB级别的海量数据

# PySpark
# Spark对Python语言的支持，重点体现在，Python第三方库：pyspark上
# pyspark主要有两种用法：
# ①作为Python第三方库进行数据处理
# ②提交至Spark集群，进行分布式集群计算















### 2.基础准备


# 【构建PySpark执行环境入口对象】
# 导入pyspark后，想要使用PySpark库完成数据处理，首先要创建一个执行环境入口对象。
# PySpark的执行环境入口对象是：类SparkContect 的类对象
# 步骤如下：


# # (0)导包
# from pyspark import SparkConf, SparkContext
# # (1)创建SparkConf类对象
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")  # 链式调用，当各方法返回值都是同一个对象时，才可进行链式调用
# # (2)基于SparkConf类对象创建SparkContext类对象（执行环境入口对象）
# my_contect = SparkContext(conf = my_conf)
# # (3)打印PySpark的运行版本
# print(my_contect.version)
# # (4)停止SparkContext对象的运行（停止PySpark程序）
# my_contect.stop()


# SparkContect类对象，是PySpark编程中一切功能的入口。
# PySpark的编程，主要分为三个步骤：
# 1.数据输入  --  通过SparkContext类对象的成员方法，完成数据的读取操作
# 2.数据处理计算  --  通过RDD类对象的成员方法，完成各种数据计算的需求
# 3.数据输出  --  将处理完成后的RDD对象，调用各种成员方法完成写出文件、转换为list等操作















### 3.数据输入[得到RDD对象]
# 目录：
# (1) RDD介绍
# (2)Python数据容器转RDD对象
# (3)读取文件转RDD对象


# (1) RDD介绍
# PySpark支持多种数据的输入，再输入完成后，都会得到一个：RDD类对象
# RDD全称为：弹性分布式数据集(Resilient Distributed Datasets)
# PySpark针对数据的处理，都是以RDD对象作为载体，即：
#   数据存储再RDD内
#   各类数据的计算方法，也都是RDD的成员方法
#   RDD的数据计算方法，返回值依旧是RDD对象



# (2)Python数据容器转RDD对象
# PySpark支持通过SparkContext对象的parallelize成员方法，将：list、tuple、set、dict、str 转换为PySpark的RDD对象
# parallelize：v.使程序（适合）进行计算
#
# 注意：字符串会被产分出一个个的字符，存入RDD对象
#      字典仅有key被存入RDD对象


# # 实际例子如下：
# from pyspark import SparkConf, SparkContext
#
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# # 通过parallelize方法将Python对象加载到Spark内，成为RDD对象
# rdd1 = sc.parallelize([1,2,3,4,5])
# rdd2 = sc.parallelize((1,2,3,4,5))
# rdd3 = sc.parallelize('abcde')
# rdd4 = sc.parallelize({1,2,3,4,5})
# rdd5 = sc.parallelize({'key1':'value1','key2':'value2'})
#
# # 查看RDD里面有什么,需要用collect()方法
# print(rdd1.collect())  # [1, 2, 3, 4, 5]
# print(rdd2.collect())  # [1, 2, 3, 4, 5]
# print(rdd3.collect())  # ['a', 'b', 'c', 'd', 'e']
# print(rdd4.collect())  # [1, 2, 3, 4, 5]
# print(rdd5.collect())  # ['key1', 'key2']
#
# sc.stop()



# (3)读取文件转RDD对象
# 若想将文本文件转换为RDD对象，需要借助textFile方法
# 语法：rdd对象名 = sc接口名.textFile(文件名)
# 将文本文件的每一行变为一个字符串，一行行存入RDD对象中，即["第一行", "第二行", ...]


# from pyspark import SparkConf, SparkContext
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.textFile("D:\Python\python项目\python_learn\测试文档\文本.txt")
# print(rdd.collect())
# # 文件存入结果为：['1234567890', '114514', '1919810', 'ohhhhhh', '2333333']
#
# sc.stop()















### 4.数据计算
# PySpark的数据计算，都是基于RDD对象来进行的。
# RDD对象的计算，基于RDD内置丰富的成员方法(算子)
# 本节主要讲述RDD的算子

# 目录：
# (1)map方法
# (2)flatMap方法
# (3)reduceByKey方法
# (4)练习案例1
# (5)filter方法
# (6)distinct方法
# (7)sortBy方法
# (8)案例练习2



## (1)map方法
# map  英文：地图、映射

# 语法：rdd.map(func)
# 注意：func要求传入一个参数，一个返回值【f:(T) -> U】
# 功能：对RDD内的元素逐个处理(处理依据是func)，并返回一个新的RDD


# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"  # 这句话是让python运行时找到python解释器
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# # 创建rdd对象，并使用map方法
# rdd = sc.parallelize([1,2,3,4,5])
# rdd1 = rdd.map(lambda x: x*10)  # 用map方法计算并返回rdd中每个值*10后的新rdd
# rdd2 = rdd1.map(lambda x: x+5).map(lambda x:x/10)  # 链式调用，将值加5再除10
#
# print(rdd1.collect())  # [10, 20, 30, 40, 50]
# print(rdd2.collect())  # [1.5, 2.5, 3.5, 4.5, 5.5]
# sc.stop()





## (2)flatMap方法
# flat  a.水平的

# 功能：对rdd执行map操作,然后进行【解除嵌套】操作
# 解除嵌套：[[1,2],[3,4],[5,6]] -> [1,2,3,4,5,6]


# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# # 准备一个rdd对象，并对其使用map、flatMap算子
# rdd = sc.parallelize(["qwe rty uio", "asd fgh jkl","zxc,vbn"])
# rdd1 = rdd.map(lambda x:x.split(" "))
# rdd2 = rdd.flatMap(lambda x:x.split(" "))
#
# print(rdd1.collect())  # [['qwe', 'rty', 'uio'], ['asd', 'fgh', 'jkl'], ['zxc,vbn']]
# print(rdd2.collect())  # ['qwe', 'rty', 'uio', 'asd', 'fgh', 'jkl', 'zxc,vbn']
# # 可见flatMap具有解嵌套的功能
# sc.stop()





## (3)reduceByKey方法

# 语法：rdd.reduceByKey(func)
# 注意：func要求传入两个参数，返回一个值（返回值与两个输入值类型相同）【f:(V,V) -> V】
# 功能：针对【KV型RDD】，自动按照key分组，然后根据你提供的【聚合逻辑】，完成组内数据(value)的聚合操作
# KV型RDD：对于pyspark，KV指("a",1)这类二元元组也算
# 聚合逻辑：如lambda a,b:a+b，意思是将两个相同k的kv型数据的v相加


# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# # 准备一个rdd
# rdd = sc.parallelize([('男',75),('女',82),('男',83),('女',92)])
# # 以男女进行分组，并将各组内的值进行聚合
# rdd1 = rdd.reduceByKey(lambda a,b:a+b)
#
# print(rdd1.collect())  # [('女', 174), ('男', 158)]
# sc.stop()





## (4)练习案例1
# 案例要求：读取文件，并统计文件内每个单词出现的词数
# 文件路径："D:\Python\python项目\python_learn\测试文档\单词计数2.txt"

# # 案例实现：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"  # 找到python解释器
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")  # 构建SparkConf对象
# sc = SparkContext(conf=my_conf)  # 创建执行环境入口对象
#
# rdd = sc.textFile("D:\Python\python项目\python_learn\测试文档\单词计数2.txt")
# # 思路：①将每行进行切分，获得单词列表   ②将单词变为二元元组('单词',1)   ③用reduceByKey分组求和
# rdd1 = rdd.flatMap(lambda x:x.split(" ")).map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)
#
# print(rdd1.collect())  # [('qwe', 6), ('asd', 10), ('zxc', 8)]
# sc.stop()





## (5)filter方法
# filter  英文： v.过滤  n.过滤器

# 语法：rdd.filter(func)
# 注意：func传入一个参数，返回bool值。 f:(T) -> bool
# 功能：函数对RDD数据逐个过滤处理，得到True的保留至返回值的RDD中


# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.parallelize([1,2,3,4,5,6,7,8,9])
# rdd1 = rdd.filter(lambda x:x%2)  # 保留奇数，去除偶数
#
# print(rdd1.collect())  # [1, 3, 5, 7, 9]
# sc.stop()





## (6)distinct方法
# dintinct  英文：a.不同的、有区别的

# 语法：rdd.distinct()  无需传参
# 功能：对RDD数据进行去重，返回新RDD


# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.parallelize([1,1,2,3,3,4,5,5])
# rdd1 = rdd.distinct()
# print(rdd1.collect())  # [1, 2, 3, 4, 5]
# sc.stop()





## (7)sortBy方法

# 语法：rdd.sortBy(func, ascending=False, numPartitions=1)
# 注意：f:(T) -> U，一个参数，一个返回值；返回什么，就按谁进行排序
#      ascending=False：True升序，False降序
#      numPartitions：用多少分区排序，暂时未接触分布式，可省略
# 功能：以func为依据进行排序


# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.parallelize([(5,'c'),(3,'b'),(9,'f'),(1,'a'),(8,'e'),(6,'d')])
# # 将上面rdd数据按照数字大小进行降序排序
# rdd1 = rdd.sortBy(lambda x:x[0], ascending=False)
#
# print(rdd1.collect())  # [(9, 'f'), (8, 'e'), (6, 'd'), (5, 'c'), (3, 'b'), (1, 'a')]
# sc.stop()





## (8)案例练习2
# 将文件转换为rdd格式，文件路径如下："D:\Python\python项目\python_learn\测试文档\orders.txt"
# 问题如下：
# ①将各个城市按销售额排序，从大到小
# ②全部城市，有哪些商品类别再售卖?
# ③北京市有哪些商品在售卖?

# # 案例实现：
# from pyspark import SparkConf, SparkContext
# import os, json
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.textFile("D:\Python\python项目\python_learn\测试文档\orders.txt")
# data_json = rdd.flatMap(lambda x:x.split("|"))  # 切分每行的字符串存入rdd中
# data_dict = data_json.map(lambda x:json.loads(x))  # 将json转化为字典
#
# #①将各个城市按销售额排序，从大到小
# question_1 = data_dict.\
#     map(lambda x:(x['areaName'],int(x['money']))).\
#     reduceByKey(lambda a,b:a+b).\
#     sortBy(lambda x:x[1],ascending=False,numPartitions=1)
# print(question_1.collect())
#
# # ②全部城市，有哪些商品类别再售卖?
# question_2 = data_dict.\
#     map(lambda x:x['category']).\
#     distinct()
# print(question_2.collect())
#
# # # ③北京市有哪些商品在售卖?
# question_3 = data_dict.\
#     filter(lambda x:x['areaName']=='北京').\
#     map(lambda x:x['category']).\
#     distinct()
# print(question_3.collect())















### 5.数据输出
# pyspark数据的输入、运算，是将python数据转换为rdd类型，使用rdd类型的方法对数据进行计算；数据计算完毕之后，需要先将rdd类型数据转换回来，才能进行输出。

# 目录：
# ①输出为python对象
# (1)collect算子
# (2)reduce算子
# (3)take算子
# (4)count算子
# ②输出到文件中
# (1)saveAsTextFile算子

#### ① 输出为python对象


## (1)collect算子
# 语法：rdd.collect()
# 功能：将RDD各个分区内的数据，统一收集到Driver中，形成一个List对象

# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.parallelize([1,2,3,4,5])
# rdd_list = rdd.collect()
# print(rdd_list)  # [1, 2, 3, 4, 5]
# sc.stop()




## (2)reduce算子
# 语法：rdd.reduce(func)
# f:(T,T)->T，两参数一返回值，类型一致
# 功能：对RDD数据以func为依据进行聚合

# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.parallelize([1,2,3,4,5])
# print(rdd.reduce(lambda a,b:a+b))  # 15
# sc.stop()




# ## (3)take算子
# # 语法：rdd.take(5)
# # 功能：取RDD的前N个元素，组合成list返回给你

# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.parallelize([1,2,3,4,5])
# print(rdd.take(3))  # [1, 2, 3]
# sc.stop()




## (4)count算子
# 语法：rdd.count()
# 功能：计算RDD中有多少条数据，返回一个数字

# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.parallelize([1,2,3,4,5])
# print(rdd.count())  # 5
# sc.stop()




##### ② 输出到文件中

## (1)saveAsTextFile算子
# 语法：rdd.saveAsTextFile(文件夹名)
# 功能：将RDD的数据写入文本文件中，输出一个文件夹
# 支持本地写出，hdfs等文件系统
# 注意：想要执行该方法，需要下载配置hadoop环境

# # 例子如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# os.environ['HADOOP_HOME'] = "hadoop所在的目录"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# # 准备RDD1
# rdd1 = sc.parallelize([1,2,3,4,5])
# rdd1.saveAsTextFile("D:\Python\python项目\python_learn\测试文档\rdd_test.txt")
# # 准备RDD2
# rdd2 = sc.parallelize([('hello',3),('hi',2),('Spark',1)])
# rdd2.saveAsTextFile("D:\Python\python项目\python_learn\测试文档\rdd_test.txt")
# # 准备RDD3
# rdd3 = sc.parallelize([[1,2],[3,4],[5,6]])
# rdd3.saveAsTextFile("D:\Python\python项目\python_learn\测试文档\rdd_test.txt")















### 6.综合案例
# 案例：搜索引擎日志分析。
# 日志路径："D:\Python\python项目\python_learn\测试文档\search_log.txt"
# 案例需求 -- 读取文件转换成RDD，并完成：
# ① 打印输出：热门搜索时间段(小时精度)Top3
# ② 热门搜索词Top3
# ③ 统计"hadoop"在哪个时段被搜索最多


# # 案例如下：
# from pyspark import SparkConf, SparkContext
# import os
# os.environ['PYSPARK_PYTHON'] = "D:\Python\Python 3.11.2\python.exe"
# my_conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# sc = SparkContext(conf=my_conf)
#
# rdd = sc.textFile("D:\Python\python项目\python_learn\测试文档\search_log.txt")
# rdd_list = rdd.map(lambda x:x.split("\t"))
#
# # ① 打印输出：热门搜索时间段(小时精度)Top3
# # 思路：将数据转换为(时间,1)，reduceByKey分组聚合获得(时间,次数)，排序即可          # 注意，如下，若是一行代码太长，可以用【\+回车】来换行，在运行是按照一行的逻辑来运行（代码长度最好不要超过这条虚线）
# rdd1 = rdd_list.map(lambda x:(x[0][0:2],1)).\
#     reduceByKey(lambda a,b:a+b).\
#     sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
#     take(3)
# print(rdd1)  # [('20', 3479), ('23', 3087), ('21', 2989)]
#
# # ② 热门搜索词Top3
# # 思路：和①相同，把时间换成关键词
# rdd2 = rdd_list.map(lambda x:(x[2],1)).\
#     reduceByKey(lambda a,b:a+b).\
#     sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
#     take(3)
# print(rdd2)  # [('scala', 2310), ('hadoop', 2268), ('博学谷', 2002)]
#
# # ③ 统计"hadoop"在哪个时段被搜索最多
# # 思路：先将符合'hadoop'的过滤从来，再重复①的按时间排序
# rdd3 = rdd_list.filter(lambda x:x[2]=='hadoop').\
#     map(lambda x:(x[0][0:2],1)).\
#     reduceByKey(lambda a,b:a+b).\
#     sortBy(lambda x:x[1],ascending=False,numPartitions=1).\
#     take(3)
# print(rdd3)  # [('23', 294), ('20', 294), ('21', 245)]

