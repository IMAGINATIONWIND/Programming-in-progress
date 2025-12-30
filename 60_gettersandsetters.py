class AL_MURG :
    def __init__(self,some_value):
        self.a_value = some_value
        
    def UP(self):
        print(f"2 TIMES OF THE GIVEN VALUE IS {self.a_value*2}")
   
    @property
    def DOWN(self):
        return 5*self.a_value

    @DOWN.setter
    def DOWN(self,some_new_value):
        self.a_value = some_new_value/10
        
a_obj = AL_MURG(0)
a_obj.DOWN = 33
print(a_obj.DOWN)
a_obj.UP