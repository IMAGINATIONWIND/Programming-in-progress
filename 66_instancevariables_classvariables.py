class Home:
#class variable||
#              \/
    cost = 1000
    Membercount = 0
    def __init__(self,name):
        self.name = name
        self.ownerName = "MOHAN" #INSTANCE VARIABLE
        Home.Membercount += 1
    def detailingIs(self):        #                                
        print(f"THE NAME OF THE OWNER IS {self.ownerName}\n AND THE HOUSE NAME IS {self.name}\n THE COST OF THE HOUSE FOR {self.Membercount} people IS {self.cost}")
        
a = Home("SWEET HOME")
a.ownerName = "RAVI KISHAN"
print(a.detailingIs())
Home.cost = 19000
print(Home.cost)
b = Home("CASTLE OF GLASS")
b.cost = 500
print(b.detailingIs())
