class Student:
    def __init__(self,name,age,scores):
        self.name =name
        self.age =age
        self.scores=scores
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getcourse(self):
        c= max(self.scores)
        return c
c=Student('李文达',18,[85,90,88])
print('姓名：',c.getname())
print('年龄',c.getage())
print("最高分：",c.getcourse())