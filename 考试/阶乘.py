sum=0
for i in range(1,21):
    t = 1
    for j in range(1,i+1):
        t*=j
    print(t)
    sum+=t
print("1-20的阶乘的和的值为：",sum)