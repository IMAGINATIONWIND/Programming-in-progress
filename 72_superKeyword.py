'''class Parentclass:
    def parent_method(self):
        print("THIS IS FATHER")
        
class childclass(Parentclass):
    # def parent_method(self):
    #     print("CHILD 1")
    #     super().parent_method()
    def child_method(self):
        print("CHILD 2")
        super().parent_method()
        
child_object = childclass()
child_object.child_method()
child_object.parent_method()
'''

class Teacher:
    def __init__(self,name, number , id):
        self.name = name
        self.number = number
        self.id = id
class Student(Teacher):
    def __init__(self,name,number,id,classno):
        super().__init__(name,number,id)
        self.classno = classno
        
rohan = Teacher("ROHAN KHATRI", 45 , "A01")
harry = Student(2,1,"R014","5A")
print(rohan.name)
#jo parent class hai uske constructor mei jo variable declare 
#hoga wo subclass mei hona chahiye compulsory then
#uske baad chahe to kuch extra extend kar sakate hai
#wo bhi child class mei