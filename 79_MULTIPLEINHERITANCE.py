class SchoolTeacher:
    def __init__(self,school):
        self.school = school
    def show(self):
         print(f"I AM A SCHOOL TEACHER THE SCHOOL IS {self.school}")

class TuitionTeacher:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"I AM A COACHING TEACHER , THE NAME IS {self.name}")

class Teacher(SchoolTeacher,TuitionTeacher):
    def __init__(self,school,name):
        self.school = school
        self.name = name
        print("I am a Teacher")
 
t = Teacher("KVS", "RAJEEV")
print(t.school)
print(t.name)
t.show()
print(Teacher.mro())