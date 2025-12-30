print( "PLEASE ENTER THE NUMBER TO BE VERIFIED")
f = int(input("HERE : "))
for a in range (2,int((f**0.5)+1)):
   PRIME = True
   if (f/a == 0 and f/1 == 0) : PRIME = False
   break
if PRIME:
        print("THIS NUMBER IS PRIME")
else:
        print("THE NUMBER ISN'T PRIME")