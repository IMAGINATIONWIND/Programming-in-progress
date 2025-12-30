
s = open("test_file.txt" , "rb")
# to print it
text = s.read()
print(text)
s.close()

#  r to read it ; reads without r as well ; rb for binary , jpeg other files
# to write in a file which also erases previous data

s = open("test_file.txt" , "w")
s.write("HELLO BHAI SAHAB")
print(text)
s.close()

# to add new data without erasing the previous one 

s = open("test_file.txt" , "a")
s.write("  _ HELLO BHAI KAISA HAI")
s.close()