# simple inheritance is single inheritance
class School:
    def __init__(self,classes,sections):
        self.classes = classes
        self.sections = sections
    def showsections(self):
        print(f"THE AVAILABEL SECTIONS ARE : {self.sections}")
class Students(School):
    def __init__(self,name, roll,classes,sections):
        #HERE NOT USING SUPERKEYWORD THEREFORE SELF WILL BE USED
        #                 ||
        #                 \/
        School.__init__(self,classes,sections)
        self.name = name
        self.roll = roll
    def tellname(self):
        print(f"MY NAME IS {self.name} AND SECTION IS {self.sections}")
s1 = Students("ARAB",34,5,"5A")
s1.tellname()