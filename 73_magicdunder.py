class Customer:
    name=input("ENTER NAME : ")
    def __len__(self):
        i = 0 
        for c in self.name:
            i +=1
        return i
    
    def __str__(self):
        return f"The name of Customer is {self.name}"
    def __repr__(self):
        return f"Customer :(' {self.name}')"
    def __call__(self):
        print("SOME POTENTIAL USE CASE--> if u()")
        
u = Customer()
print(u.name)
print(len(u))
print(repr(u))
# AGAR STR NOT FOUND ->> FALLBACK TO REPR
''' TO UNDERSTAND THIS PROPERLY READ THE REPL
https://replit.com/@codewithharry/73-Day-73-MagicDunder-Methods#main.py
'''
u()