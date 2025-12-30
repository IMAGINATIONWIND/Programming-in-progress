class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)
string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
#here the fromStr is an extension of the constructor init
#it just takes in the class in which it is created
#which is same as some any other method which takes the self object as input
#TRUST ME I TRIED EVERY POSSIBLE THING I COULD THINK OF 
#BUT STILL FOR THIS USE CASE THIS IS THE BEST METHOD
#NO YOU CAN'T USE SIMPLE METHOD TO DO IT , IT JUST WON'T WORKOUT