# def add(some_fn):
#     def jkl():
#         print("Hi !!")
#         print("\n How are you\n")
#         some_fn()
#         print("Thanks for your service")
#     return jkl

# @add
# def addingder():
#     a = 3+5
#     print(a)
    
# #  A DECROTATOR JUST EXTENDS THE FUNCTIONALITY OF A FN JUST GIVES IT A FEW EXTRA FUNCTIONS

# addingder()

def add(some_fn):
    def jkl(*args,**kwargs):
        print("Hi !!")
        print("\n How are you\n")
        some_fn(*args,**kwargs)
        print("Thanks for your service")
    return jkl

@add
def addUngder( a,b ):
    print(a+b)
    
# add(addUngder)(3,5)
# or just
addUngder(2,567)