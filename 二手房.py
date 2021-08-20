import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
head={   #这里根据自己的电脑构建
 }
url='https://gz.lianjia.com/ershoufang/pg6/'
reponse=requests.get(url,headers=head)#获取URL
reponse.encoding='utf-8'#设置URL的字符编码
html=reponse.text#获取URL的文本模式
print(html)
pattern=re.compile(r'<div class="title"><a class=.*?>(.*?)</a>.*?<div class="houseInfo".*?/span>(.*?)</div>.*?<div class="priceInfo">.*?span>(.*?)</span>万</div><div class="unitPrice".*?<span>(.*?)</span></div>',re.I|re.M)#搜索需要查找的文字并设置忽略大小写和多行模式
result=re.findall(pattern,html)#在HTML文本里面遍历匹配，可以获取字符串中所有匹配的字符串，返回一个列表
for item in result:
    house_name=item[0]
    houseinfo=item[1]
    totleprice=item[2]+'万'
    unitPrice=item[3]
    with open('二手房信息.txt','a',encoding='utf-8') as f:
        f.write((house_name+':'+houseinfo+'。'+'总价为：'+totleprice+'。'+unitPrice))
        f.write('\n\n')