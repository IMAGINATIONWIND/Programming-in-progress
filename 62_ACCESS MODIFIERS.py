# class SUSHANT:
#     def __init__(self):
#         self.name = "KUMAR"
#         self.__age = 38
        
        
# s=SUSHANT()
# print(s.name)
# #print(s.__age)#it should show up as an error
# '''to avoid collision basically # name mangling'''
# print(s._SUSHANT__age)
# '''Now! this works fine'''

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())