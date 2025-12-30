import os
# print(os.listdir())#shows all the files in a given directory
#print(os.listdir("C:/"))#shows all the files in a specific directory
# i = 0
# for file in os.listdir():
#     i += 1
#     if file.endswith(".png"):
#         os.rename(file,f"{i}.png")
    
# XDDDD
i = 0
for file in os.listdir():
    if file.endswith(".png"):
        i += 1
        os.rename(file,f"{i}.png")







''''''