[TOC]

# mysql tutorial

## 安装

`docker pull mysql:5.6` [gui](https://tableplus.com/)

挂载外部配置和数据安装

```bash
mkdir -R /opt/mysql
mkdir /opt/mysql/conf.d
mkdir /opt/mysql/data/

# 创建my.cnf配置文件
touch /opt/mysql/my.cnf

cat my.cnf

[mysqld]
user=mysql
character-set-server=utf8
default_authentication_plugin=mysql_native_password
secure_file_priv=/var/lib/mysql
expire_logs_days=7
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
max_connections=1000


[client]
default-character-set=utf8

[mysql]
default-character-set=utf8


# 创建容器，并后台启动
docker run --restart=always 
--privileged=true -d 
-v /opt/mysql/data/:/var/lib/mysql 
-v /opt/mysql/conf.d:/etc/mysql/conf.d 
-v /opt/mysql/my.cnf:/etc/mysql/my.cnf 
-p 3306:3306 
--name my-mysql 
-e MYSQL_ROOT_PASSWORD=123456 mysql
```



参数说明：

```bash
--restart=always 当docker重启时，容器会自动启动
--privileged=true 容器内的root拥有真正root权限，否则容器内root只是外部普通用户权限
-v /opt/mysql/my.cnf:/etc/mysql/my.cnf 映射配置文件
-v /opt/mysql/data:/var/lib/mysql 映射数据目录
```



本练习参考[易百教程](https://www.yiibai.com/)和[示例数据](https://www.yiibai.com/downloads/yiibaidb.zip)， [Tutorial]([https://necan.gitbooks.io/mysql-tutorial)

```mysql
USE yiibaidb;
SHOW tables;

+--------------------+
| Tables_in_yiibaidb |
+--------------------+
| customers          |
| employees          |
| items              |
| offices            |
| orderdetails       |
| orders             |
| payments           |
| productlines       |
| products           |
| tokens             |
+--------------------+
10 rows in set
Time: 0.082s
```



查询语句`SELECT`

```mysql
SELECT
	column1, column2, ...
FROM
	table
[INNER |LEFT |RIGHT ] JOIN table_2 ON conditions
WHERE
	conditions
GROUP BY column1
HAVING group_conditions
ORDER BY column1
LIMIT offset, length;


eg:

SELECT * FROM employees LIMIT 5;


```

去重：`DISTINCT`

```mysql
SELECT DISTINCT
	columns
FROM
	table_name
WHERE
	where_conditions;
```

过滤`WHERE, AND, OR, IN, BETWEEN, LIKE, LIMIT, IS NULL`

数据排序`ORDER BY`

连接表`INNER JOIN, LEFT JOIN, CROSS JOIN`

分组`GROUP BY, HAVING`

子查询，派生表，通用表达式

集合操作符`UNION, UNION ALL, INTERSECT`

修改数据`INSERT, INSERT IGNORE, UPDATE, UPDATE JOIN, DELETE, ON DELETE CASCADE, DELETE JOIN, REPLACE, PREPARE`

事务

- 表锁定



---

`SQL`书写规则：

> 表名、字段名必须使用小写字母或数字，禁止出现数字开头，禁止两个下划线中间只出现数字。数据库字段名的修改代价很大。

```bash
# 创建数据库
CREATE DATABASE IF NOT EXISTS test 
DEFAULT CHARACTER SET utf8;

# 修改数据库
ALTER DATABASE test DEFAULT CHARACTER SET utf8;

# 删除数据库
DROP DATABASE IF EXISTS test;

# 选择数据库
USE test;


```



### 数据类型

`MySQL`的数据类型分为：整数型、浮点数类型和定点数类型、日期和时间类型、字符串类型、二进制类型。

> 整数类型和浮点数类型可以统称数值数据类型



- 数值类型

  - 整数类型

    ​	`TINYINT, SMALLINT, MEDIUMINT, INT, BIGINT`

  - 浮点数类型

    `FLOAT, DOUBLE`

  - 定点数类型

    `DECIMAL`

- 日期/时间类型

  `YEAR, TIME, DATE, DATETIME, TIMESTAMP`

- 字符串类型

  `CHAR, VARCHAR, BINARY, VARBINARY, BLOB, TEXT, ENUM, SET`

- 二进制类型

  `BIT, BINARY, VARBINARY, TINYBLOB, BLOB, MEDIUMBLOB, LONGBLOB`



`MySQL5.7支持的存储引擎有 InnODB, MyISAM, Memory, Merge, Archive, Federated, CSV, BLACKHOLE`



| 存储引擎  | 描述                                                         |
| --------- | :----------------------------------------------------------- |
| archive   | 用于数据存档的引擎，数据被插入后就不能在修改了，且不支持索引 |
| csv       | 在存储数据时，会以逗号作为数据项之间的分隔符                 |
| blackhole | 会丢弃写操作，该操作会返回空内容                             |
| federated | 将数据存储在远程数据库中，用来访问远程表的存储引擎           |
| InnoDB    | 具备外键支持功能的事务处理引擎                               |
| memory    | 置于内存的表                                                 |
| merge     | 用来管理由多个MyISAM表构成的表集合                           |
| MyISAM    | 主要的非事务处理存储引擎                                     |
| NDB       | MySQL集群专用存储引擎                                        |



MySQL存储引擎特性汇总和对比



| 特性         | MyISAM | InnoDB | MEMORY |
| :----------- | :----- | ------ | :----- |
| 存储限制     | 有     | 支持   | 有     |
| 事务安全     | 不支持 | 支持   | 不支持 |
| 锁机制       | 表锁   | 行锁   | 表锁   |
| B树索引      | 支持   | 支持   | 支持   |
| 哈希索引     | 不支持 | 不支持 | 支持   |
| 全文索引     | 支持   | 不支持 | 不支持 |
| 集群索引     | 不支持 | 支持   | 不支持 |
| 数据缓存     |        | 支持   | 支持   |
| 索引缓存     | 支持   | 支持   | 支持   |
| 数据可压缩   | 支持   | 不支持 | 不支持 |
| 空间使用     | 低     | 高     | N/A    |
| 内存使用     | 低     | 高     | 中等   |
| 批量插入速度 | 高     | 低     | 高     |
| 支持外键     | 不支持 | 支持   | 不支持 |



1.  MyISAM：存储引擎不支持事务和外键，所以访问速度比较快。如果应用于主要以读取和写入为主，只有少量的更新和删除操作，并且对事务的完整性、并发性要求不是很高，选择MyISAM存储引擎非常合适
2. InnoDB：在事务上具有优势，即支持具有提交、回滚和崩溃恢复能力的事务安装，所有比MyISAM存储引擎占用更多的磁盘空间。如果应用于对事物的完整性有比较高的要求，在并发条件下要求数据的一致性，数据操作除了插入和查询以外，还包括很多的更新、删除操作，InnoDB存储引擎比较合适。（如计费系统、财务系统）
3. MEMORY：将所有的数据保存在RAM中，所以该存储引擎的数据访问速度快，但是安全上没有保障。如果应用于涉及的数据比较少，且需要进行快速访问，则比较合适。



