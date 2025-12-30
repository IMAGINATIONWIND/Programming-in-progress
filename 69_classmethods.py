# A WAY TO SIMPLY INTERACT WITH THE  CLASS AND CHANGE SOME CLASS VARIABLES
class Teacher:
    classroom = "5 A"
    def show(self):
        print(f"THE TEACHER'S NAME IN CLASS {self.classroom} is {self.name}")
        
    @classmethod
    def changeCLASSroom(YahaPeKuchBhiVariableNameChalega , newclassroom):
        YahaPeKuchBhiVariableNameChalega.classroom = newclassroom
        
s1 = Teacher()
s1.name = "GOUTAMI TEACHER"
s1.show()

s1.changeCLASSroom("7 A")
s1.show()
print(Teacher.classroom)