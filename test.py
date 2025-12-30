result = []
num = int(input("the number : ")) 
i = 0
while (i <= num**0.5):
    i = i+1
    if (num%i == 0):
        result.append(i)
        if num//i != i:
            result.append(num//i)

print(sorted(result))
        