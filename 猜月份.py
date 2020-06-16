# 输入月份，判断季节
mooth=int(input("请输入月份（1-12）："))
if 3<=mooth<=5 :
    print("%d是春季度，第一季度"%mooth)
elif 6<=mooth<=8:
    print("%d是夏季度，第二季度" % mooth)
elif 9<=mooth<=11:
    print("%d是秋季度，第三季度" % mooth)
elif 1<=mooth<=2:
    print("%d是冬季度，第四季度" % mooth)
elif mooth==12:
    print("%d是冬季度，第四季度" % mooth)
else:
    print("输入有误！")
