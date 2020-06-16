import tkinter as tk
num=[]
t=tk.Tk()
t.title('数学')
t.geometry('500x500')
tk.Label(t,text="整数1:",).place(x=100,y=100)
tk.Label(t,text="整数2:",).place(x=100,y=150)
a1=tk.Entry(t,show=None)
a2=tk.Entry(t,show=None)
a3=tk.Entry(t,show=None)
a3.place(x=100,y=220)
a1.place(x=150,y=100)
a2.place(x=150,y=150)
def number():
        if int(a1.get())% int(a2.get())== 0:
          result=a1.get()
          a3.insert(100,result)
        if int(a1.get())% int(a2.get())!= 0:
            j=2
            sum=1
            for i in range(2,10):
                 if  int(a1.get())%j==0 and int(a2.get())%i==0:
                       if i==j==2:
                           sum=(int(a1.get())*int(a2.get()))/2
                 else:
                           sum=int(a1.get())*int(a2.get())
            a3.insert(100, int(sum))
bt=tk.Button(t,text="求最小公倍数",command=number).place(x=100,y=190)
t.mainloop()

