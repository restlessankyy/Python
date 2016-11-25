import os
dirpath = "c:\\Python27\\Python-Trailning"
for dirpath, dirnames,filenames in os.walk(dirpath):
    print    "Current Path : " ,dirpath
    print    "Directories List :" , dirnames
    print  "Filenames : ",filenames
    print " "
    
