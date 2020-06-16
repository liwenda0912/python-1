message={'李文达':"计科2班 201806110085 李文达 "}
m=str(input('请输入键：'))
n=message.get(m)
if n==None:
    print('你输入的键不存在！')
else:
    print(n)
