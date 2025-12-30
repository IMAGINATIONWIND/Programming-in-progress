class Firm:
    def __init__(self,role,salary):
        self.role = role
        self.salary = salary
        
    def show(self):
        print(f"The role of {self.role} has a salary of {self.salary}")
    
class Dept(Firm):
    def __init__(self,deptname,deptid,role,salary):
        Firm.__init__(self,role,salary)
        self.deptname = deptname
        self.deptid = deptid
        
    def show(self):
        Firm.show(self)
        print(f"The {self.deptname} can have max CTC of {self.salary} ")
        
class Staff(Dept):
    def __init__(self,deptname,name,deptid,role,salary):
        Dept.__init__(self,deptname,deptid,role,salary)
        self.name = name
    
    def show(self):
        Dept.show(self)
        print(f"The Employee {self.name} works in {self.deptname} with a CTC of {self.salary}LPA")
    
t1 = Staff("cs","MANOJ SUPER",1,"SDE 3",4800000)
t1.show()

# this should be like this 

# Example of Hybrid Inheritance 
class BaseClass:
  pass

class Derived1(BaseClass):
  pass  

class Derived2(BaseClass):
  pass  

class Derived3(Derived1, Derived2):
  pass

# Hierarchical Inheritance
class BaseClass:
  pass

class D1(BaseClass):
  pass

class D2(BaseClass):
  pass

class D3(D1):
  pass