# a = open("test_file.txt" , "r")
# i = 0 
# while True : 
#     i = i + 1 
#     l = a.readline()
#     if not l : 
#         break
#     mark1 = int(l.split(",")[0])
#     mark2 = int(ll.split(",")[1])
#     mark3 = int(l.split(",")[2])
#     print(f"THE MARKS OF STUDENT {i} IN SST IS {mark1}")
#     print(f"THE MARKS OF STUDENT {i} IN PE IS {mark2}") 
#     print(f"THE MARKS OF STUDENT {i} IN C IS {mark3}")
#     # it's a string so you have to typecast it and then it will be integer
#     print(l)


f = open("test_file93" , "w")
lines = ["abra\n" , "ka\n" , "dabra\n"]
f.writelines(lines)
f.close()
