n1=int(input("求两个数的公约数\n请输入第一个数："))
n2=int(input("请输入第二个数："))
num=[]
def number(n1,n2):
  for i in range(1,100):
     if n1%i==0 and n2%i==0 :
         num.append(i)
  p=max(num)
  print('它们的最大公约数为：',p)
number(n1,n2)