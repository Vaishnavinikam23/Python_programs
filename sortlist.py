class Student:
    def setdate(self,sid,sname):
        self.id=sid
        self.name=sname
    def showdata(self):
        print(self.id,self.name)

class Mark(Student):
    def setmarks(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def showmarks(self):
        print(self.m1,self.m2)

ob=Mark()
ob.setdate(1,"abc")
ob.setmarks(90,80)
ob.showmarks()
    
        