import jieba
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
txt=open('文章/新闻.txt','r',encoding='utf-8').read()
word=jieba.lcut(txt)
words=' '.join(jieba.lcut(txt))
m=np.array(Image.open('文章/mao.png'))
w=WordCloud(font_path='C:/Windows/Fonts/STXIHEI.TTF',width=900,height=700,background_color='white',mask=m).generate(words)
plt.imshow(w,interpolation='bilinear')
plt.axis('off')
plt.show()
w.to_file('文章/cy2.png')
