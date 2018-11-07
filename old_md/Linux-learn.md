-----
Linux Command Learning
-----

* 目录共享
	* <font size=5>**`sshfs`**</font>
	
	    *  <font size=4>sshfs username@Ipaddress:/path  shared -p Port </font>
	*  <font size=5> **`vboxsf`** </font>
	 
		* 	<font size=4>sudo adduser username vboxsf</font>
		 	
		* 	<font size=4>sudo mount -t vboxsf -o uid=$UID ,gid=(id -g) shared  ~/host</font>

* <font size=4> __常用命令__
	*  ls
	*  ll
	*  la
	*  touch
	*  cd
	*  pwd
	*  mkdir  
	*  ----
	*  wget

|      wget      |       usage        |  
|      :----:    |      :---- :       |
|*`wget -r url/path`* | 下载目录内所有文件 |
|*`wget -c url`*  | 断点续传，从上次断开的地方继续下载 |
| *`wget --user-agent='Mozilla/5.0' url`*  | 设置代理头 |
|*`wget  url -O newname`* | 为下载的文件重新设置名字 |
|  *`wget --limit-rate=100k url`* | 限速下载 |


*	*   scp
		
       
       scp -P port file username@host:/path  # 从本地上传文件到远程服务器
       
       scp -rp -P port username@host:/path/file .  # 从远程服务器下载本地当前目录
       
*	*  rsync	    <font size=3><span style="color:blue">`:可以实现本地复制，` `*local to remote, remote to local*`  `的复制`</span></font>
		*	-a : 保留时间戳，用户权限
		*	-z : 开启压缩
		*	-v : 显示传送信息
		*	--progress : 显示进度条
		*	-r : 递归复制
		
* 	* tar   <span style="color:red">`解压缩`</span> , 解压缩类型:<span style="color:blue"> gzip, bzip2, xz</span>
		* 	gz  
			+ 	tar zcvf test.tar.gz test.py  
				- 以gzip的方式打包 test.py文件
			+ 	tar zxvf test.tar.gz 
				- 解压
		* bz2 
            +	tar jcvf test.tar.bz2 test.py
            +	tar jxvf test.tar.bz2
       * xz
            +	tar  Jcvf test.tar.xz test.py
            +	tar Jxvf test.tar.xz
* 	* zip & unzip
		* zip -r test.zip test.py
		* unzip -o test.zip 
			* 	<font size=3><span style="color:red"> `-o 表示如果存在同名文件，则覆盖`</span></font>
* 	* tail
		* 	tail -f Ngnix.log
			* 	默认打印最新的10条日记
          
</font>