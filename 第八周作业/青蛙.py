a=int(input("请输入井的深度："))
b=int(input("请输入青蛙白天爬行的距离："))
c=int(input("请输入晚上滑落的距离："))
i = 0
while a>0:
    a=a-b+c
    i+=1
print("青蛙要爬行%d天才可以爬出井口"%i)