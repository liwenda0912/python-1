sum=0
n=1
a=0
fenzi=2
fenmu=1
for i in range(20):
    a=fenzi
    b=fenmu
    sum += a / b
    print(a,b)
    fenzi=a+b
    fenmu=a
print("前20项的和为：",sum)

