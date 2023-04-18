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
# 前面给出想要插入数据的列，后面以行为单位，给出每一行中各列对应的值。
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
## (3)older by / limit 排序分页


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
## (3)older by / limit 排序分页















### 6.Python & MySQL
### 7.综合案例














