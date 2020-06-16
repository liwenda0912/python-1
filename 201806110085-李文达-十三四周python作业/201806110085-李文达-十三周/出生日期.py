num=str(input("请输入你的身份证号码（18位）："))
if len(num)==18:
 def split(num):
     year=num[6:10]
     monthy=num[10:12]
     day=num[12:14]
     print("你的出生日期为：",year,'年',monthy,'月',day,'日',end='\n')
 split(num)
else:
    print('输入格式错误！')