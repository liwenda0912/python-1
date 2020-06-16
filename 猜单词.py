import random
iscontinue='y'
while iscontinue=='y':
 words=('code','well','good','advance','school','study','adjust','process','updata','spicy','')
 print("{:*^50}".format("开始猜单词"))
 a=(input("请输入你的学号(12位数字)："))
 if len(a)==12:
   num=int(a[11:])
   if num<3:
       num=3
   else :
       num = int(a[11:])
 else:
     iscontinue = input("学号格式有误！\n你是否继续猜（y/n）：")
 word=random.choice(words)
 corrert=word
 disorder=''
 i=1
 p=num
 while word:
    position=random.randrange(len(word))
    disorder+=word[position]
    word=word[:position]+word[position+1:]
 print("你有%d次机会猜！\n请把%s组成正确的单词！"%(num,disorder))
 print("{:*^50}".format("猜单词"))
 guess=input("请输入你要猜的单词：")
 while guess!=corrert and i<num:
       i+=1
       p=p-1
       guess=input("对不起！你猜的单词是错的！(再重新输入%d次为错则退出本次游戏）)\n请重新输入："%p)
 if guess==corrert:
      print("恭喜你！在第%d次机会就猜对了！"%(i))
 else:
     print("对不起！%d次机会已用完！" % (num))
 iscontinue=input("\n你是否继续猜（y/n）：")










