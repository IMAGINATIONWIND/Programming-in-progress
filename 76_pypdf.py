import pypdf as p
import os
class Recommendations:
    def __init__(self):
        print("The available pdf are given :\n")
        for file in os.listdir():
             if file.endswith(".pdf"):
                 print(file)
class Merge(Recommendations):
    # ✔ Correct idea
# “Class variables execute BEFORE __init__() —
# which means BEFORE the parent constructor runs.”
    def __init__(self):
        super().__init__()
        a = input("ENTER THE NAME 0F THE 1ST PDF WITH EXTENSION : ")
        b = input("ENTER THE NAME 0F THE 2ND PDF WITH EXTENSION : ")
        f = input("ENTER THE NAME 0F THE output PDF WITH EXTENSION : ")
        writer = p.PdfWriter()
        writer.append(a)
        writer.append(b)
        with open(f,"wb") as file:
         writer.write(file)
        os.startfile(f)
m = Merge()
