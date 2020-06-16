import jieba
extend={'起来','姑娘','这里','出来','他们','众人','自己','知道','说道','如今','你们','那里','我们','什么','一个','一面' }
txt=open('文章/红楼梦.txt','r',encoding='utf-8').read()
word=jieba.lcut(txt)
count={}
for key in word:
    if len(key)==1:
        continue
    elif key=="黛玉忙" or key=="黛玉因 "or key=="黛玉"or key=="黛玉道"or key=='林妹妹'or key=='黛玉笑':
         keys="林黛玉"
    elif key == "宝钗笑" or key == "宝钗道" or key == "宝钗":
         keys = "薛宝钗"
    elif key == "听宝玉" or key=="宝玉" or key =='向宝玉':
         keys="贾宝玉"
    elif key =="贾母忙"or key=="贾母王"or key=="贾母笑" or key=='贾母因'or key=='老太太':
         keys="贾母"
    elif key == "凤姐儿"or key=="凤丫头":
         keys = "凤姐"
    elif key=='太太':
        key='王夫人'
    else:
        keys=key
    count[keys]=count.get(keys,0)+1
for words in extend:
    del (count[words])
list1=list(count.items())
list1.sort(key=lambda x:x[1],reverse=True)
for i in range(6):
    a,b=list1[i]
    print('{:<10}---{:>5}'.format(a,b))
print(list1)


