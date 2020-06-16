import random
print("欢迎来到猜数字游戏！")
number= random.randint(0,9)
num = int(input("请输入你要猜的数字(0-9)："))
a=1
while(a==1):
    if number==num:
       print("恭喜你！猜对了！")
       a=int(input("是否继续游戏，继续输入1：不继续请随意输入："))
       if a==1:
         number = random.randint(0, 9)
         num = int(input("请输入你要猜的数字："))
    if num>9:
        num = int(input("输入有误！请重新输入："))
    if num<0:
        num = int(input("输入有误！请重新输入："))
    else:
       if num>number:
          print("数字太大了")
       if num<number:
          print("数字太小了")
       num = int(input("猜错了，请重新输入："))