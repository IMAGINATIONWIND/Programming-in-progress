#finally always works even if the value is
# returned finally executes but normal code doesn't 👍


def func1():
    
    try:
       print( "please enter a number")
       a = int(input())
       return a 
    except: 
       print("Some error ocurred")
       return 2
    finally:
       print("ALWAYS EXECUTED")
       
       
X = func1()
print(X)