# ⭐ Giving special meaning to Python operators (+, -, *, <, == etc.) when they are used with objects of your own class.
# In simple terms:
# You teach Python how to use operators on your custom objects.

class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k "
    def __add__(self,x):
        return Vector(self.i + x.i , self.j + x.j , self.k + x.k)
v1 = Vector(2,3,4)
print(v1)

print(v1+v1)
print(type(v1+v1))