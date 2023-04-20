"""
目录：
1.数据库介绍
2.MySQL的入门使用
3.SQL基础与DDL
4.SQL - DML
5.SQL - DQL
6.Python & MySQL
7.综合案例
"""






### 1.数据库介绍

# # 什么是数据库?
# 数据库就是指数据存储的库，作用是组织数据并存储数据
#
# # 数据库如何存储数据？
# 数据库的数据存储，是按照【库->表->数据】这三个层级来组织的。
#
# # 我们如何实现数据库？
# 我们需要借助【数据库管理系统】，也就是【数据库软件】来实现这种数据库。
# 常见的数据库软件有：Oracle, MySQL, SQL Server, PostgreSQL, SQLite等
# 这里我们使用MySQL来进行数据库的学习



# # 数据库和SQL的关系
# 【数据库】是用来存储数据的，在这个过程中，会涉及到：
#  ·数据的新增
#  ·数据的删除
#  ·数据的修改
#  ·数据的查询
#  ·数据库、数据表的管理
#  等等
# 而【SQL语言】，就是一直对数据库、数据进行操作、管理、查询的工具
# SQL -- Structured Query Language 结构化查询语言
#
# # 使用数据库软件去获得 库->表->数据，这种数据组织、存储的能力，
# # 并借助SQL语言，完成对数据的增删改查等操作















### 2.MySQL的入门使用

# # cmd中的MySQL使用（首先要清楚数据库的层次【库->表->数据】）
# # 下面是一些SQL语言
#
#
# # (1)命令：MySQL -uroot -p
# 功能：以root用户身份进入MuSQL环境，需要输密码
#
# # (2)命令：show databases;
# 功能：查看有哪些数据库（记得写分号）
# 英文：database -- 数据库
#
# # (3)命令：use 库名;
# 功能：使用某个数据库
#
# # (4)命令：show tables
# 功能：查看当前库内有哪些表
# 英文：table -- 表格
#
# # (5)命令：exit
# 功能：退出MySQL环境















### 3.SQL基础与DDL

#### (1)SQL基础
#### (2)DDL的使用



#### (1)SQL基础

# # SQL的概述
# SQL全称：Structured Query Language 结构化查询语言
# SQL语言：用于访问和处理数据库的标准的计算机语言
# 简单来说，SQL语言就是操作数据库的专用工具


# # SQL语言的分类
# 由于数据库管理系统(数据库软件)功能非常多，不仅仅是存储数据，还要包含：数据的管理、表的管理、库的管理、账户管理、权限管理等等。
# 所以，操作数据库的SQL语言，也基于功能，可划分为4类：
#
# (1) 数据定义：DDL（Data Definition Language）
#           库的创建删除、表的创建删除
#
# (2) 数据操纵：DML（Data Manipulation Language）
#           新增数据、删除数据、修改数据等
#
# (3) 数据控制：DCL（Data Control Language）
#           新增账户、删除账户、密码修改、权限管理等
#
# (4) 数据查询：DQL（Data Query Language）
#           基于需求查询和数据计算



# # SQL语言语法特征
# (1)大小写不敏感
# (2)可以单行或多行书写，最后以;号结束
# (3)SQL支持注释：
#   单行注释： -- 注释内容 (-- 后面一定要有一个空格)
#   单行注释： # 注释内容 (# 后面可以不加空格，推荐加上)
#   多行注释： /* 注释内容 */






#### (2)DDL的使用
# DDL--数据定义语言，英文全称是Data Definition Language
# 大体上来看，有库、表的查看、创建、删除等
# 我们分为库管理和表管理来分别讲述


# # DDL-库管理
# 下面的SQL语句可以完成库管理的操作，我们同样可以通过图形化界面完成这些操作。
#
#
# ①查看数据库列表
# show databases;
#
#
# ②使用指定数据库
# use 库名;
#
#
# ③创建数据库
# create database 库名 [charset UTF8]
#   上面中括号[]表示可选
#
#
# ④删除指定数据库
# drop database 库名;
# drop database if exists 库名;
#
#
# ⑤查看当前使用的数据库
# select database();




# # DDL-表管理
#
# ①查看指定库中的所有表
# show tables;  （注意：需要先选择数据库）
#
#
# ②创建表
# create table 表名(
#    列名称 列类型,
#    列名称 列类型,
#    ......
# );
#
# # 【列类型】如下：
# # int           -- 整数
# # float         -- 浮点数
# # varchar(长度)  -- 文本，长度为数字，做最大长度限制（最大255） [varchar也叫可变长字符串，相当于python中的str，但是可限制长度]
# # date         -- 日期类型
# # timestamp     -- 时间戳类型
# # ......
#
#
# ③删除表
# drop table 表名;
# drop table if exists 表名;


# # e.g.创建表的格式如下：
#
# create table student(
# 	name varchar(10),
# 	id varchar(20),
# 	age int
# );















### 4.SQL - DML

## (1)insert 数据插入
## (2)delete 数据删除
## (3)update数据更新



# DML--数据操作语言，英文全称是Data Manipulation Language
# 用来对数据库中表的数据记录进行 插入(insert)、删除(delete)、更新(update)


# # (1)insert 数据插入
# 语法：insert into 表[(列1,列2,...,列N)] values(值1,值2,...值N)[,(值1,值2,...值N),......,(值1,值2,...值N)];
#   注意：上面方括号[]代表可选内容
# 语法解析：前面给出想要插入数据的列，后面以行为单位，给出每一行中各列对应的值。
# 功能：将(values)数据(insert into)插入指定的列中
# 补充：表名后面不指定列，默认按顺序插入全部列


# # 示例：
# create table student(
# 	id int,
# 	name varchar(10),
# 	age int
# );
#
# # ①仅向student表中插入id列数据，一次插入三行
# insert into student(id) values(10001), (10002), (10003);
#
# # 上面一次插入行，等效于一行一行的插入
# insert into student(id) values(10001)
# insert into student(id) values(10002)
# insert into student(id) values(10003)
#
#
# # ②向student表中插入(id,name,age)列数据，传入数据时顺序要对应
# # 注意：数据库的字符串只能识别单引号''
# insert into student(id,name,age) values(10004,'张三',31),(10005,'李四',32),(10006,'王五',33);
#
#
# # ③插入全部列数据，快速写法
# insert into student values(10007,'小明',15),(10008,'小美',13);
# # 当表名后面不指定要插入的列时(即省略括号)，默认按表格顺序插入全部列






# # (2)delete 数据删除
# 语法：delete from 表名 [where 条件判断];
#   条件判断：列 操作符 值
#   操作符：= < > <= >= != 等等 （注意，不是==）
#   id = 5，id < 3,age >= 18
# 功能：删除指定条件的行数据
# 若不写 where 判断条件，默认清空整张表的数据


# # 示例：
# # 删除指定条件的数据
# delete from student where id <= 10003;
# delete from student where name = '张三';
# delete from student where age < 18;
#
# # 删除全部数据
# delete from student;






# # (3)update 数据更新
# 语法：update 表名 set 列 = 值 [where 条件判断];
#   该语法的条件判断与delete中的相同
# 功能：根据判断条件，设置指定列中符合的值为新值
# 若不写 where 判断条件，默认将整列数据都改为指定的值

# # 示例：
# # 根据条件更新指定数据
# update student set name = '小红' where name = '张三';
# update student set age = 23 where id = 2;
# update student set name = '杰克' where age = 52;
#
# # 更新某列的全部数据
# update student set id = 0;















### 5.SQL - DQL

## (1)select 基础数据查询
## (2)group by 分组聚合
## (3)older by / limit  排序/分页

# # 综合语法如下：（从上到下有序）
# select 列/聚合函数/* from 表
# where 条件判断
# group by 列
# order by 列 [asc/desc]
# limit n[,m];
#
# 即：select 列/聚合函数/* from 表 [where 条件判断] [group by 列] [order by 列 [asc/desc]] [limit n[,m]];


# DQL--数据查寻语言，英文全称是Data Query Language
# DQL包含基础查询、分组聚合、排序分页等操作



## (1)select 基础数据查询
# 之前想要查看列表内容，我们只能通过数据库软件的图形化界面来查询，利用select数据查询语句，可以让我们用sql语言之间查询表的内容。
#
# 语法：select 字段列表/* from 表 [while 条件判断];
# 功能：从(from)表中，选择(select)某些列(字段列表或*)进行展示，可以用where条件判断筛选结果
# 不写[while 条件判断]，默认打印一整列；   * 通配符代表全部。


# # 示例：
# # 输出表中的全部内容
# select * from student;
#
# # 输出表中的name,id列
# select name,id from student;
#
# # 输出表中age>=30的人的全部信息
# select * from student where age >= 30;
#
# # 输出id>100的人的name和age列
# select name,age from student where id >100







## (2)group by 分组聚合

# 分组聚合应用场景非常多，如：统计班级中男生和女生人数。
# select sex,count(name) from student group by sex;
# 这种需求就需要：
#   ·按性别分组
#   ·统计每个组人数
# 这就称之为：分组聚合


# 【语法】：（前面和基础数据查询一样，后面多了group by）
# select 字段/聚合函数 from 表 [where 条件判断] group by 列;
# 聚合函数： sum(列)  求和
#          avg(列)   求平均值
#          min(列)   求最小值
#          max(列)   求最大值
#          count(列/*)   求数量 （一组中成员数量一定，无论写哪列，或者*，结果都是组中人的数量）
#
# 功能：对列中符合where条件的列元素进行【分组】(group by)，将各组元素通过聚合函数进行【聚合】
# 如 select sex,avg(age) from student group by sex;  # 以学生性别为分组，显示各分组的性别和平均年龄
#
# 注意：【group by中出现了哪个列，哪个列才能出现在selest的字段中】
#       若以sex分组，那么字段中只能出现sex，而聚合函数则没有限制。
#       （除了sex的字段有多个，但一个分组结果只出一行，没法选择其他字段，但可以使用聚合函数）


# # 示例：
# # 对相同年龄的学生进行分组，显示每组年龄已经id的最大最小值
# select age,max(id),min(id) from student group by age;
#
# # 对年龄小于18的学生以性别进行分组，显示各组的性别和年龄的平均值
# select sex,avg(age) from student where age < 18 group by sex;
#
# # 对id>100的学生以id进行分组，显示各组的id、年龄的平均、最大、最小值
# select id,avg(age),max(age),min(age) from student where id > 100 group by id;
#
# # 对年龄>20的学生以年龄进行分组，输出各组的年龄、人数，以年龄升序输出。
# select age,count(name) from  student
# where age > 20
# group by age
# order by age;






## (3)older by / limit  排序/分页

## order by 排序
# 可以对查询的结果，使用older by关键字，指定某个列进行排序。
# 可以对以上学的内容进行order by排序（基础查询和分组聚合都可以）
#
# 语法如下：
# select 列/聚合函数/* from 表
# where 条件判断
# group by 列
# order by 列 [asc/desc];  （asc升序，desc降序，默认升序）
# # SQL语言支持写多行，遇;结束。相当于写到一行


# # 示例：
# # 按年龄对学生进行升序排序
# select * from student order by age;
#
# # 按id对年龄>30岁的学生进行降序排序
# select * from student where age > 30 order by id desc;




## limit 分页
# 同样，可以使用limit关键字，对查询结果进行数量限制或分页排序
# 即在上面语法的后面，直接加一个 limit n[,m]
# 若 limit n     表示从头向下输出n行（默认条0行）
# 若 limit m,n   表示跳过m行，从m+1行开始，向下输出n行

# 语法：
# select 列/聚合函数/* from 表
# where 条件判断
# group by 列
# order by 列 [asc/desc]
# limit n[,m];


# # 示例：
# # 输出student表中的5条结果
# select * from student limit 5;
#
# # 输出student表中按id降序排序的前5条结果
# select * from student order by id desc limit 5;
#
# # 输出student表中按年龄升序排序的第3-6行结果（跳过两行，数4行）
# select * from student order by age limit 2,4;















### 6.Python & MySQL

# 除了使用图形化工具以外，我们也可以使用编程语言来执行SQL从而操作数据库。
# 在Python中，使用第三方库：pymysql来完成对MySQL数据库的操作。


# 在Python中操作MySQL，需要先创建链接对象，在最后关闭链接对象
# 创建链接对象后，就可以执行操纵数据库的sql语句
#   首先要获得游标对象，其次选择指定的数据库，即可用 游标对象.execute()执行sql语句
#   执行完sql语句后，若想更新数据同步到数据库，需要 链接对象.conmmit() 确认更新
#                 若想查看打印信息，需要 游标对象.fetchall() 接收返回信息
# 具体步骤如下：



# # # (1)导包
# from pymysql import Connection
#
#
# # # (2)获取MySQL数据库的链接对象（构建链接）
# conn = Connection(
#     host = 'localhost',         # 主机名，ip地址是127.000.000.001
#     port = 3306,                # MySQL数据库端口，默认是3306
#     user = 'root',              # 用户名
#     password = '123321WSSZW'    # 密码
#     # autocommit = True         # 可设置自动提交，更改数据是不用conmmit确认
# )
#
#
# # # (3)打印MySQL基础信息
# # print(conn.get_server_info())  # 8.0.32 （这是我们的MySQL版本，打印该信息表示链接成功）
#
#
#
# # # (4)执行【非查询数据、更改数据的SQL】
# # ①获取游标对象
# cursor = conn.cursor()
# # ②选择数据库，相当于sql语言的【use 库名;】
# conn.select_db('py_test')
# # ③执行sql语句
# cursor.execute('create table student(id int, name varchar(15), age int, sex varchar(5));')  # 创建student表
#
#
#
# # # (5)执行【更改数据的SQL】
# # ①获取游标对象
# cursor = conn.cursor()
# # ②选择数据库，相当于sql语言的【use 库名;】
# conn.select_db('py_test')
# # ③执行sql语句
# cursor.execute('insert into student(name,id,sex,age) values("张三",1001,"男",18);')  # 为表中添加数据
# # ④通过commit确认更改信息
# conn.commit()
#
#
#
# # # (6)执行【查询数据的SQL】
# # ①获取游标对象
# cursor = conn.cursor()
# # ②选择数据库
# conn.select_db('py_test')
# # ③执行sql语句
# cursor.execute('select * from student;')  # 查看表中数据
# # ④返回执行结果
# results = cursor.fetchall()  # 返回执行结果到一个元组中去
# print(results)
#
#
#
# # # (7)关闭链接
# conn.close()















### 7.综合案例

# 将下面两个文件的内容写入数据库中：
# 一月份数据是普通文件，使用逗号分割数据，从前到后分别是(日期，订单id，销售额，销售省份)，路径如下：'D:\Python\python项目\python_learn\测试文档\某公司一二月份数据\2011年1月销售数据.txt'
# 二月份数据是JSON数据，同样包含(日期，订单id，销售额，销售省份)，路径如下：'D:\Python\python项目\python_learn\测试文档\某公司一二月份数据\2011年2月销售数据JSON.txt'
# 本次需求我们创建按一个数据库来使用，数据库名称：py_sql
#
# 在MySQL中创建好py_sql数据库，剩下步骤要求用Python代码来将数据存入表中。
# 基于数据结构，构建一个orders表来存储数据，以下是建表语句：
# create table orders(
#   order_date date,
#   order_id varchar(255),
#   money int,
#   province varchar(10)
# );



# (0)导包
from pymysql import Connection


# (1)构建数据对象
class Data:
    def __init__(self, data, id, money, province):
        self.data = data
        self.id = id
        self.money = money
        self.province = province

class FileToList:
    """该对象的功能是：初始输入文件名；可通过调用file_to_list方法，获得一个列表，列表成员是Data对象"""
    def __init__(self,file_name):
        self.file = file_name
    def file_to_list(self):
        pass

class TxtFileToList(FileToList):
    def file_to_list(self):
        f = open(self.file, 'r', encoding='UTF-8')
        txt_list = []
        for line in f.readlines():
            line_list = line.strip().split(',')
            line_data = Data(line_list[0], line_list[1], int(line_list[2]), line_list[3])
            txt_list.append(line_data)
        f.close()
        return txt_list

class JsonFileToList(FileToList):
    def file_to_list(self):
        import json
        f = open(self.file, 'r', encoding='UTF-8')
        json_list = []
        for line in f.readlines():
            line_dict = json.loads(line)
            line_data = Data(line_dict['date'],line_dict['order_id'],int(line_dict['money']),line_dict['province'])
            json_list.append(line_data)
        return json_list


# (2)将两个月份的数据合并为1个list来储存
txt_object = TxtFileToList('D:\Python\python项目\python_learn\测试文档\某公司一二月份数据\\2011年1月销售数据.txt')
json_object = JsonFileToList('D:\Python\python项目\python_learn\测试文档\某公司一二月份数据\\2011年2月销售数据JSON.txt')
txt_list = txt_object.file_to_list()
json_list = json_object.file_to_list()
all_list = txt_list + json_list


# (3)获得MySQL链接对象
coon = Connection(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '123321WSSZW'
)


# (4)执行sql语句
coon.select_db('py_sql')  # 选择数据库
cursor = coon.cursor()  # 创建游标对象
# ① 创建orders表
cursor.execute("create table orders(order_date varchar(20), order_id varchar(255), money int, province varchar(10));")
# # ② 传入数据
# for object in all_list:
#     cursor.execute(f"insert into orders(order_date, order_id, money, province) values({object.data}, {object.id}, {object.money}, {object.province});")
# # ③ 查看数据
# cursor.execute("select * from orders")
# results = cursor.fetchall()
# print(results)
# # ④ 确认上传数据
# coon.commit()


# (5)关闭链接
coon.close()
