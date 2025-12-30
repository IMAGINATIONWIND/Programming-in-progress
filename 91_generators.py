def anyfunctionwillbecomeagenereatorifiuseYIELDwithit():
    for i in range (8):
        yield i
        
gen = anyfunctionwillbecomeagenereatorifiuseYIELDwithit()
#more efficient
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print("yaaaaaaaaaa")
for j in gen:
    print(j)
# alsi hote hai generators 
# computation taal dete hai
'''for more details 
url = https://youtu.be/ixd-u3pmsUc?si=2o5dCZq_o4bi2sFX'''