a=[1,6,2,3,4]
b=[1,2,3,5]
d=[7,8,9,10]
f=[11,4,5,6,1,8]
def list(*num):
    print('它们最大值分别为：',end="\n")
    for i in num:
       c=max(i)
       print(c)

list(a,b,d,f)