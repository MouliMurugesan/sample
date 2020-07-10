class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class Attendence(Student):
    def Att_Marks(self,marks):
        print(self.marks)
class Assignment(Student):
    def Ass_Marks(self,Assing_marks):
        print(self.Assign_marks)
        

class Internal(Attendence,Assignment):
    def tot_Marks(self):
        print(self.marks+self.Assign_marks)

a=Internal()
a.Att_Marks(20)
a.Ass_marks()
a.tot_marks()
