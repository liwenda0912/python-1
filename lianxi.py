import random
print("欢迎来到猜数字游戏！")
number= random.randint(0,9)
num=int(input("请输入你要猜的数字："))
while(num!=number):
    if number==num:
       print("恭喜你！猜对了！")
    else:
        if num>number:
           print("数字猜大了")
        if num<number:
          print("数字猜小了")
    num=int(input("猜错了，请重新输入："))
    if number==num:
       print("恭喜你！猜对了！")