user=['admin']
passwords=['admin']
u=['li']
p=['123']
a='y'; num=0 ; n=0
username = str(input('请输入你的用户名:'))
password = str(input('请输入你的用户名密码:'))
if password== passwords[0] and user[0]==username:
                print('管理员,你好!', end="\n")
                f='='*50
                print("%s"%f)
                print()
                print("1.添加用户账号和密码\n2.删除用户账号和密码\n3.查看用户账号和密码")
                print()
                print("%s" % f,end='\n')
                while a == 'y':
                      num=int(input('请输入你要维护的项目：\n'))
                      if num==1:
                          u1 = str(input('请输入增加的用户账号:\n'))
                          p1 = str(input('请输入增加的用户密码:\n'))
                          if u1 in u:
                              print("该用户已存在")
                          else:
                            u.append(u1)
                            p.append(p1)
                      elif num==2:
                         u2 = str(input('请输入删除的用户账号:'))
                         if u2 in u:
                          tip=u.index(u2)
                          u.pop(tip)
                          p.pop(tip)
                          print(u,p)
                          print("用户%s删除完成" %u2)
                         else:
                             print("该用户不存在")
                      elif num==3:
                          count=len(u)
                          for i in range(count):
                               print("用户账号和密码分别为:%s\t%s"%(u[i],p[i]))
                      else:
                          print("请输入正确的指令")
else:
     print('你不是管理员')






