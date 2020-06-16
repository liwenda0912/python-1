# 判断象限
x=int(input("请输入x轴:"))
y=int(input("请输入y轴:"))
if (x==0 and y==0):
    print("坐标在原点上,坐标为（%d,%d）"%(x,y))
elif(x==0):
    print("坐标在x轴上,坐标为（%d,%d）"%(x,y))
elif(y==0):
    print("坐标在y轴上,坐标为（%d,%d）"%(x,y))
elif(x>0 and y>0):
    print("坐标在第一象限,坐标为（{},{}）".format(x,y))
elif(x>0 and y<0):
    print("坐标在第二象限,坐标为（{},{}）".format(x,y))
elif(x<0 and y>0):
    print("坐标在第三象限,坐标为（{},{}）".format(x,y))
else:
    print("坐标在第四象限坐标为（{},{}）".format(x,y))
