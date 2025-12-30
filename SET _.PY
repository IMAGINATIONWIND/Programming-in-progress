S = {2,299,3,4,6,6,"6gyv76",6,8}
print(S)
'''empty set is recognised as set() and not {} as {} is used for dictionary''' 
p = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}

ap = S.intersection(p)
print(ap)
ap = S.symmetric_difference(p)
print(ap)
ap = S.union(p)
print(ap)
ap = S.difference(p)    # S - P
print(ap)
print(S.isdisjoint(p))  
s1={"a","b","c","d","e","f","g","h","i","j"}
print(p.issuperset(s1))
print(s1.issubset(p))
s1={"a","b","c","d","e","f","g","h","i","j"}
s1.add("k")
print(s1)
p.remove("a")
print(p)
#p.remove("a")  #error
p.discard("a")  #no error
#pop removes random element in a set and returns 
# it as a set is unordered and unindexed so the element bieng
# deleted is also randomised to a certain extent
del p  #deletes the set
print(p) #error as set is deleted
p.clear()
print(p) #empty set

if "c" in s1:
     print("yeah")