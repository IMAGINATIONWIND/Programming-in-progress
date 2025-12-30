letter = input("PLEASE ENTER THE STRING IN SMALL LETTERS: ")
flag = 0
for let in letter:
    if let == 'a':
        flag += 1
    elif let == 'e':
        flag += 1
    elif let == 'i':
        flag += 1
    elif let == 'o':
        flag += 1
    elif let == 'u':
        flag += 1

print("Total number of vowels:", flag)
