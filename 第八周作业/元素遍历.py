c="y"
while c=="y":
  list=str(input("请输入一串字符:"))
  for item in list:
     if item ==',':
        item =''
     if item == '，':
        print("输入有误！")
        c=input("是否继续输入（y/n）：")
     if item=="z":
        break
     print(item,end=" ")
  break
print()
print("输出结束！")