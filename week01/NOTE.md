学习笔记


Homework1:
安装并使用 requests、bs4 库，爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，
并以 UTF-8 字符集保存到 csv 格式的文件中.
pip install requests  : 用来发http request, 获取http response
pip install bs4 :  用来解析http response内容
pip install lxml ： 使用xpath方式parse网页内容
pip install pandas : 可以用来存csv文件

1. 先使用"https://maoyan.com/films?showType=3" 获取网页内容
2. 获取10部电影的名字，链接
3. 访问链接，获取电影类型，上映日期
4. 将上面内容以字典形式存储，最后放到一个list里
5. 使用pandas将上述内容存到csv文件


Homework2:
安装scrapy, pip install scrapy.
使用到的命令有：
scrapy startproject homework2
scrapy genspider maoyan maoyan.com
scrapy crawl maoyan

1. 先使用"https://maoyan.com/films?showType=3" 获取网页内容
2. 获取10部电影的名字，链接
3. 访问链接，获取电影类型，上映日期，通过item保存名字/类型/上映日期
4. 在pipelines.py中保存到文件