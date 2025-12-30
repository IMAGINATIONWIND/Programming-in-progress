#to sum all the numbers in a list
def sumoflist(list):
    a=len(list)
    sum=0
    for i in range(0,a):
        sum+=list[i]
    print(sum)
#TO MULTIPLY ALL THE NUMBERS IN A LIST
def multiplyoflist(list):
    a=len(list)
    multiply=1
    for i in range(0,a):
        multiply*=list[i]
    print(multiply)        
list=[1,2,3,4,5]
sumoflist(list)
multiplyoflist(list)


#STRING REVERSAL
def reversestring(string):
    print(string[::-1])
    
    
string=input("Please enter the string:")
reversestring(string)




list1=[1,2,3,4,5]
sumoflist(list1)