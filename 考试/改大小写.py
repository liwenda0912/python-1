file=open("a.txt",'r')
c=[]
for i in file:
    c.append(i.swapcase())
c=''.join(c)
print(c)
file=open("a.txt",'w')
file.write(c)
file.close()





