print("查找一个在1000-10000之间的数的各位数字之和为你输入的数的数字！")
num=int(input("请输入一个正整数："))
p=0
print("1000-10000之间的数的各位数字之和为%d的数为"%(num))
for i in range (1000,10000):
    a=str(i)
    p=0
    for n in a:
        b=int(n)
        p+=b
    if num==p:
       print(a)




