n = int(input("Enter a number: "))
rem = 0
sum = 0
rev = 0
q=0
while n > 0:
   p = n%10
   q =q*10+p
   n=  n// 10
while q > 0:
    rem = q % 10
    print(rem, end = " ")
    q = q // 10
print("")