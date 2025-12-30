import shutil
import os # as shutil module can't delete a single folder

shutil.copy("Sita Warrior of Mithila.pdf","copied using shutil module.pdf")


'''Warning Even the higher-level file copying functions (shutil.copy(), shutil.copy2()) cannot copy all file metadata.
On POSIX platforms, this means that file owner and group are lost as well as ACLs. On Mac OS, the resource fork and other metadata are not used. This means that resources will be lost and file type and creator codes will not be correct. On Windows, file owners, ACLs and alternate data streams are not copied.'''
#USED TO COPY WITH THE EXACT METADATA
        # ||
        # \/
        
shutil.copy2("Sita Warrior of Mithila.pdf","copied using shutil module.pdf")
os.remove("copied using shutil module.pdf")

# shutil.move()'''to change a file's location'''
# shutil.copytree(src,dest)

'''Recursively copy an entire directory tree rooted at src to a directory named dst and return the destination directory. All intermediate directories needed to contain dst will also be 
created by default.
'''