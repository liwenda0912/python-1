class Cource:
    no=0
    name=0
    teacher=0
    _add=0
    def __init__(self,no,name,teacher,add):
        self.name=name
        self.no=no
        self._add=add
        self.teacher=teacher
    def getnmessage(self):
        print("课程编号：",self.no)
        print("课程名：",self.name)
        print("课程老师：",self.teacher)
        print("课程地点：",self._add)
a=Cource(1820,'数学','李利','三教')
print(a.getnmessage())
