with open('test_file93.txt' , 'r') as f :
    print(type(f))
    
    f.seek(10) #LEAVES FIRST 10 BYTES
    
    print(f.tell())# TELLS THE BYTES SEEKED 
    # reads the stuff after the 10 bytes
    dta = f.read(5)
    print(dta) 
    
    
with open('test_file.txt' , 'w') as f :
    f.write("Hello World!")
    # limits the input number of bytes to 8
    f.truncate(8)


with open('test_file.txt' , 'r') as f :
    print(f.read())