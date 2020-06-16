list1=[]
print("请输入一组数字：")
for i in range(6):
       num=int(input(''))
       list1.append(num)
num1=int(input('请输入第一个数作为索引：'))
num2=int(input('请输入第二个数作为索引：'))
print(list1[list1[num1-1]:list1[num2]])