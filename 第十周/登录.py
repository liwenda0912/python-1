users=['python','java']
passwords=['123456','654321']
a='y'
num=0
n=0
while a=='y':
      username = str(input('请输入你的用户名:'))
      password = str(input('请输入你的用户名密码:'))
      b = len(users)
      d=len(passwords)
      for i in  users:
        b-=1
        if i==username :
            for j in passwords:
                d -=1
                if j == password:
                    print("登录成功，退出循环！")
                    a = 'n'
                    break
                if d == 0:
                    print('用户名正确，密码不正确！重新登录')
                    a = 'y'
                    num+=1
                    print(num)
                    break
            break
        if b==0:
            print("你输入的用户名不存在，请重新登录")
            n+=1
            if n == 3:
                a = 'n'
                print("你已用完3次登录机会了！")
            break
      if num==3:
          print("你已经输入3次了，系统锁定用户名与密码")
          a = 'n'






