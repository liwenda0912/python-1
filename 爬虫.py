import requests
from bs4 import BeautifulSoup

rl = requests.get(url='http://dict.baidu.com/s',params={'wd':'python'})#为url传递参数,带参数的get请求
r=rl.url
print(r)
soup = BeautifulSoup(rl.text,'lxml')
chapter_html=soup.find('div',class_="tab-content")
for i in chapter_html.find_all("p"):
    chapter_title1=i.text
print(chapter_title1)

with open('1.txt','w',encoding='utf-8')as f:
    f.write(chapter_title1.encode("utf-8", 'ignore').decode("utf-8", "ignore"))