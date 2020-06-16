sum=0
n=10
for i in range(1,100):
   p=n*i+2
   if(i%2==0):
       p=-p
   sum+=p
   print(p,end='+ ')
print()
print('他们的和为：',sum)