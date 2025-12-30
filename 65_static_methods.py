'''used to call a method inside a class that isn't 
necessarily associated with the class but it needs to
be shipped with the class'''

class AEROPLANE:
    
    def __init__(self,name):
        self.name = input(name)
        print("\n->",self.name)
    
    def size(self):
        self.length = 0
        if self.name == "BOIENG 747":
            self.length = "545 ft"
        print(self.length)
    
    @staticmethod
    def square(a):
        sq = lambda a : a*a
        print("THE SQUARE OF THE NUMBER IS ",sq(a))

aeo = AEROPLANE("bamboo copter: ")
print(aeo.name)
aeo.size()


print(aeo.square(5))

# MY CODE IS KINDOF COMPLEX although it didn't need to 
# check harry bhaiya's repl for more clearity
#https://replit.com/@codewithharry/65-Day-65-Static-Methods#main.py