#child class ke andarr jo parent class sse method aayega 
#usi ko change karna
'''Situation	What to pass to super()
Parent takes 2 params	pass 2 params
Parent takes 5 params	pass 5 params
Child has EXTRA params	pass only the parent’s required params
If flexible or unknown	use *args and **kwargs'''
class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x+self.y
    def sub(self):
        return self.x-self.y
    def mul(self):
        return self.x*self.y
    def pow(self):
        return self.x**self.y
class Value(Calculator):
    def __init__(self,x, y):
        super().__init__(x,y)
    
    def add(self):
        return f"Using method overriding : {super().add()}"
v = Value(2,3)
print(v.add())

    
    
    
    