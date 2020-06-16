#判断闰年
n=1
while(n==1):
    year=int(input("请输入年份:"))
    if  year%4==0:
        print("%d是闰年"%year)
    elif year%100!=0|year%100==0:
      print("%d是闰年" % year)
    else:
       print("%d不是闰年" % year)
    n=int(input("是否继续输入，是请输入1,否请输入任何值:"))