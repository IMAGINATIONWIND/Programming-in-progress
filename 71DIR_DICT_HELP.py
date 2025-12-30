'''a = [1,2,3]
print(dir(a))
#prints what methods are available'''
''''''
class Mango:
    def __init__(self,type):
        self.type = type
        
m = Mango("STAR")
#I DIDN'T USE PRINT YET

print(m.__dict__)

#this one just prints whatever is with self. in a dictionary format'''
print(help(Mango))
#"The help() function is used to get help documentation for an object,"

#Including a description of its attributes and methods."