
try:
    a = "y"
    while (a == 'y'):
      r = float(input("请输入你要进行计算的圆体的半径:"))
      if r<0:
       print("对不起,输入的球体半径不能小于0")
       a=input("是否重新输入（y/n）:")
      elif r>0:
        R=r*2
        C=2*3.14*r
        S=4*3.14*r*r
        V=4/3*3.14*r*r*r
        print("球体的直径为%0.2f,球体的圆周长为%0.2f,球体的表面积为%0.2f,球体的体积为%0.2f" % (R, C, S, V))
        a ="n"
except Exception as result:
    print(result)

