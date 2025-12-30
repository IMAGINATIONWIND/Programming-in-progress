class School:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def intro (self):
        print(f"The name is {self.name} and age is {self.age}\n")
        
class School_Principal(School):
    
    def Principal(self):
        print(f"THE PRINCIPAL OF {self.name} is Ram Gopu")
        
        
        
s1 = School("BABLU BBA", 18)
s1.intro()
s2 = School("BHAI DC" , 12)
s2.intro()
s3 = School_Principal("AK KHANNA", 28)
s3.intro()
s3.Principal()
