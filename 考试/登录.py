import tkinter as tk
import tkinter.messagebox
wt=tk.Tk()
wt.title("登录！")
wt.geometry("400x300")
tk.Label(wt,text="用户名：",font=("Arial",14)).place(x=50,y=100)
tk.Label(wt,text="密码：",font=("Arial",14)).place(x=50,y=130)
user=tk.Entry(wt,show=None)
user.place(x=150,y=105)
password=tk.Entry(wt,show='*')
password.place(x=150,y=145)
def log():
    if user.get()=="admin" :
          if password.get()=="123456":
              tkinter.messagebox.showinfo(title="恭喜你！",message="登陆成功！")
bt=tk.Button(wt,text="登录",command=log).place(x=190,y=200)
wt.mainloop()