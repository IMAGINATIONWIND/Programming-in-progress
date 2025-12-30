a =input("Enter a number :   ")
try:
    a = int(a)
    print(f"Multiplication table of {a} is :")
    for i  in range (1,11):
     print(f"{a}   *  {i} = {int(a)*i}")

# except Exception as e :
#     print(e,"\nInvalid Input")  
except ValueError:
    print("PLEASE ENTER A VALID INTEGER")
except SyntaxError:
    print("PLEASE CHECK THE SYNTAX")