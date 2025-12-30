a = int(input("Enter any value between 5 and 9 :   "))
 
if(a<5 or a>12):
     raise ValueError("value should be within the given range")