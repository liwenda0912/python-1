import math
print('求一元二次方程ax^2+bx+c=0的根！')
class Example:
    a=int(input("a:"))
    b=int(input('b:'))
    c=int(input('c:'))
    d = (b ** 2) - (4 * a * c)
    if d>0:
       def __init__(self, a, b, d):
            self.d = d
            self.a = a
            self.b = b
       def getDisciminamt(self):
           return self.d
       def getRoor1(self):
              x1=(-self.b + math.sqrt(self.d) )/ (2 * self.a)
              return x1
       def getRoor2(self):
              x2 = (-self.b - math.sqrt(self.d) )/ (2 * self.a)
              return x2
    if d==0:
       def getDisciminamt(self):
           return self.d
       def getRoor1(self):
              x1=(-self.b + math.sqrt(self.d) )/ (2 * self.a)
              return x1
       def getRoor2(self):
              x2 = (-self.b+ math.sqrt(self.d) )/ (2 * self.a)
              return x2
    if d< 0:
       def getDisciminamt(self):
           return self.d
       def getRoor1(self):
              x1=0
              return x1
       def getRoor2(self):
              x2 = 0
              return x2
s=Example()
print("第一个根的值为:",s.getRoor1())
print('第二个根的值为:',s.getRoor2())
print(s.getDisciminamt())