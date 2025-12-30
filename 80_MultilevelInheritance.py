class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    
    def describe(self):
        print(f"The name of the animal is {self.name} & \n it's species is {self.species}")

class Bird(Animal):
    def __init__(self,name,region):
        Animal.__init__(self,name,species="Bird")
        self.region = region
        
    def describe(self):
        Animal.describe(self)
        print(f"The region of the {self.species} is {self.region} ")
#agar dekha jaye to iske neeche wala class jab tak call nahi hoga 
# tab tak upar wale me region user ko hi dena padega 
# and jab cuckoo call hoga to region automatically kolkata hojayega
class Cuckoo(Bird):
    def __init__(self,name,color):
        Bird.__init__(self,name,region = "Kolkata")
        self.color = color
        
    def describe(self):
        Bird.describe(self)
        print(f"The color of the {self.species} is {self.color}")

b = Bird("bholu","North America")
b.describe()
print(Cuckoo.mro())

Cuckoo("bhola","pink").describe()