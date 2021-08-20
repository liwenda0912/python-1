import requests
from bs4 import BeautifulSoup

class Novel:
 a=0
 def __init__(self,a):
     self.a=a
 def gain(self):
  if self.a==1:
    rl = requests.get(url='http://www.doupo1234.com/doupocangqiong/1.html')#为url传递参数,带参数的get请求
    r=rl.url
    rl.encoding='utf-8'#设置HTML的代码格式

    soup = BeautifulSoup(rl.text,'lxml')#html的代码格式获取

    chapter_html=soup.find('div',class_="panel-body")#查找div里的classpanel-body里的内容
    chapter_html1=soup.find('title')#查找title的

    for i in chapter_html.find_all("p"):#查找获取title里的p元素
     chapter_title1=i.text#将获取到的文字赋予给chater—title1
     print(chapter_title1)#一个一个打印出来
     with open('2.txt','a', encoding='utf-8')as f:#打开文档（如果没有就自动生成一个新文档）
        f.write(chapter_title1.encode("utf-8", 'ignore').decode("utf-8", "ignore"))#储存写入进该文档
        f.write('\n\n')#每写完一行就换行
  else:
     print('获取错误！')
c=Novel(1)
print(c.gain())
