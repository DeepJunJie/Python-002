# 学习笔记
## 异常
### 区别错误与异常
错误的范围较广，只要发生预期之外的事情，都称作错误发生；而异常主要分为两种：

系统异常：系统发生错误；

程序异常：程序接收到异常的输入。

### 异常处理机制的原理
异常也是一个类，所有的异常都继承自BaseException类

异常产生以及被捕获的过程：

1、异常类把错误消息打包到一个对象；

2、然后该对象自动查找函数调用栈；

3、传递该对象，知道遇到捕获该异常类的位置

Traceback显示了出错的位置，显示的顺序与实际的调用顺序相同。

## 改变数据的存储方式：使用数据库来存储数据
### 利用数据库进行数据存取操作的一般流程
开始-》创建数据库连接connection-》获取游标curser
-》CRUD操作-》关闭连接-》结束

操作MySQL数据库的一个比较稳定的库pymysql

### 需要注意的几点
1、数据库操作完成之后，及时断开数据库连接，减少连接带来的资源消耗；

2、尽量复用已有的连接。

## 反爬虫与反反爬虫
爬虫软件：模拟浏览器获取网页信息，并从中提取出有用的信息

反爬虫软件：检测异常网页请求

反反爬虫：针对反爬虫机制的相应应对策略，尽可能的模拟浏览器及用户的行为

### 模拟浏览器的方式：

注：httpbin是一个专门用来对http进行学习和调试的网站

模拟头部：user-agent, host, referer

模拟登录：cookie

post方式进行登录，scrapy框架中，在start_request里进行登录模拟
```python
import requests
s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
```
模拟浏览器的点击行为：

通过selenium库中webdriver包提供的方法，直接调用浏览器来发起请求，获取cookie，或进行其他操作
（网页加密处理过，需要我们去阅读JavaScript代码来进行，解密操作，但如果我们的JavaScript掌握的不够好的话，可以利用webdriver来临时的解决这个问题。这种情况单纯用python不是很好处理）

### 文件下载

```python
########## 小文件下载：
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
r = requests.get(image_url)
with open("python_logo.png",'wb') as f:
    f.write(r.content)

############# 大文件下载：
# 如果文件比较大的话，那么下载下来的文件先放在内存中，内存还是比较有压力的。
# 所以为了防止内存不够用的现象出现，我们要想办法把下载的文件分块写到磁盘中。
import requests
file_url = "http://python.xxx.yyy.pdf"
r = requests.get(file_url, stream=True)
with open("python.pdf", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)
```
 
