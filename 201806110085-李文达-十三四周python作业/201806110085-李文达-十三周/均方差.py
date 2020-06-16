import math
list1=[1,2,3,4,5,6]

def num(list1,n = 0,p = 0,j = 0,):
  for i in list1:
       n+=i
       n=n%len(list1)
  while(j<=5):
     p+=(list1[j]-n)**2
     j+=1
  p=math.sqrt(p)
  print('方差为：%.3f'%p)
num(list1)