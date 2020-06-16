list1=['台湾','苍老师','热','武藤']
str1=str(input("评论："))
list2=list(str1)
i=0
a=[]
p=str
for j in str1:
    if j=="苍":
         list2[i]='*'
         list2[i+1] = '*'
         list2[i+2]= '*'
    elif  j=="武":
         list2[i]='*'
         list2[i + 1] = '*'
    elif  j=="台":
         list2[i]='*'
         list2[i + 1] = '*'
    elif  j=="热":
         list2[i]='*'
    i+=1
p=''.join(list2)
a.append(p)
print(a)