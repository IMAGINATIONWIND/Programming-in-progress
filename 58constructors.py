 # A CONSTRUCTOR HELPS IN THE AUTOMATION OF A CLASS AND IT'S EFFICIENT USAGE DEPENDING UPON IT'S APPLICATION
 
class Info :
# WHENEVER AN OBJECT IS CREATED FOR A CLASS THE INIT ( DUNDER ) METHOD IS CALLED
     def __init__(self , b , d):
        print("Good Morning")
        self.badge = b
        self.id = d
        
     def stat(self):
         print("There's info about mek\n")
         print(f"{self.badge} is associated with {self.id}")

A = Info("DORA" , "123")
B = Info("EMON" , "456")
A.stat()
B.stat()