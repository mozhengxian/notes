title:MySQLdb的操作
-----
配置安装环境

	sudo apt install python3-dev default-libmysqlclient-dev mysql-server
    
安装虚拟环境包 pipenv autoenv

autoenv 用法：
	
    echo "source 'which activate.sh'" >> .zshrc
    
在项目目录下建.env文件，并添加：
	
    echo "source $HOME/.local/xx/bin/activate" > .env
    
 安装mysqlclient
 	
    sudo apt install mysqlclient sqlalchemy
    

-------
连接MySQL

	conn = MySQLdb.connect('localhost', 'Username', 'Passwd', 'Database')
    
获取游标

	cursor = conn.cursor()
    
demo

	sql = 'select * from movies limit 100'
    cursor.execute(sql)
    
获取数据结果

    cursor.fetchone()	# 获取一条
    
*(1, 'Toy Story (1995)', 'Adventure|Animation| Children| Comedy| Fantasy')*
    
    cursor.fetchmany(5) # 获取5条数据
    
*((2, 'Jumanji (1995)', 'Adventure|Children|Fantasy'),*
 
 *(3, 'Grumpier Old Men (1995)', 'Comedy|Romance'),*

*(4, 'Waiting to Exhale (1995)', 'Comedy|Drama|Romance'),*
 
 *(5, 'Father of the Bride Part II (1995)', 'Comedy'),*

*(6, 'Heat (1995)', 'Action|Crime|Thriller'))*

    cursor.fetchall() # 获取剩下所有的
    
  ...............................
  
 关闭连接 
 
    cursor.close()
    conn.close()
    
导入csv数据

-----使用pandas

	pd.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None)


*schema:指定构架*

|if_exists | 判断table                                |
|:----:     | :----                                    |
|fail      | 抛出 ValueError|
|replace   | 在插入数据之前删除旧的，然后创建新的，再导入                                                    |
|append    | 在已存在的表中，添加数据                 |

index

*DataFrame columns的名，并且index_lable作为值*

把csv数据文件导入MySQL

	pd.to_sql(name='movies', con=conn, if_exists='replace')
    
 ![error](./images/error.png)
 抛出DatabaseError，经搜索，改为 sqlalchemy
 
 	from sqlalchemy import create_engine
    
 
 	create_engine('mysql+mysqldb://username:passwd@localhost/database', encoding='utf-8', echo=True)
    
 *echo ,if True, 则Engine会将所有语句及其参数列表的repr（）记录到引擎记录器，默认为sys.stdout。*
 
 ![error2](./images/error2.png)
 
 
**修改 **
	
```Python

create_engine('mysql+mysqldb://username:passwd@localhost/database?charset=utf8', encoding='utf8', echo=True)
```

----
### sql基本操作
-----

##### insert 

	INSERT INTO tableNmae (attrib1,attrib2,attrib3) VALUES (values1,values2,values3)

##### update

	UPDATE tableName SET key1=values1,key2=values2,key3=values3 WHERE key=values
    
  ##### alter
  
  	ALTER TABLE tableName ADD attrib type AFTER attrib1
    
    ALTER TABLE tableName CHANGE attrib new_attrib type
    
  ##### delete
  
  	ALTER TABLE tableName DROP attrib
    
  ##### rename
  
	  ALTER TABLE tableName RENAME newTableName
      
   
   ------------------------------
   
   ### create user
   
  1. <font color=#0099ff size=4>CREATE USER 'username'@'localhost' identified by 'Password'</font>     *create method*
  2.	<font color=#0099ff size=4>INSERT INTO mysql.user (User,Host,Password,ssl_cipher,x509_issuer,x509_subject)VALUES ("username","hostname",PASSWORD("password"),'','','');</font>
   *ssl_cipher,x509_issuer,x509_subject---没有默认值，否则报错，使用PASSWORD函数加密*
   
 
*FLUSH PRIVILEGES*  *插入更新*

	GRANT ALL ON database.table TO 'username'@'localhost' IDENTIFIED BY 'passwd'
    
 