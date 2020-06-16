import matplotlib.pyplot as plt
import warnings
import pandas as pd
warnings.filterwarnings("ignore")
plt.figure(figsize=(100,80))
plt.rcParams['font.family']='SimHei'
plt.rcParams['axes.unicode_minus']=False
data=pd.read_csv('time-series-19-covid-combined_csv.csv')#
plt.title('不同国家油价变化')
plt.plot(data.year,data.Country)
plt.gca().set_xticks(data.year[::80])
#plt.gca().set_xlabel('年份')
#plt.gca().set_ylabel('油价')
plt.legend(bbox_to_anchor=(1.01,0),loc=3,borderaxespad=0)
plt.show()