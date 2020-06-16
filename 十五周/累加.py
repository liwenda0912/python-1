import tkinter as tk
num=tk.Tk()
num.title('累加')
num.geometry("300x300")
a=tk.Label(num,text="请输入计算数据：")
b=tk.Label(num,text="请单击确认：")
c=tk.Label(num,text="累加的结果是：")
n3=tk.Entry(num,show=None)
a.grid(row=1,column=1,pady=10)
n3.grid(row=1,column=2)
b.grid(row=2,column=1)
c.grid(row=3,column=1,pady=10)
def sum():
    sum=0
    for i in range(int(n3.get())+1):
        sum+=i
    d=tk.Label(text=sum)
    d.grid(row=3,column=2)
bt=tk.Button(num,command=sum,text="计算",width=10,height=1)
bt.grid(row=2,column=2)
num.mainloop()

