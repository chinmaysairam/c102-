import os
import shutil

print(os.getcwd())
fromdir='/Users/maithreyisairam/Documents/Document_files'
todir='/Users/maithreyisairam/Library/Mobile Documents/com~apple~CloudDocs/c102 project'
listoffiles=os.listdir(fromdir)
print(listoffiles)
for filename in listoffiles:
    name,extension=os.path.splitext(filename)
    if extension=='':
        continue
    if extension in(['.txt', '.doc', '.docx', '.pdf']):
        path1=fromdir+'/'+filename
        print(path1)
        path2=todir+'/'+"imagefiles" 
        print(path2)
        path3=todir+'/'+"imagefiles"+'/'+filename
        print(path3)
        if os.path.exists(path2):
            shutil.move(path1,path2)
        else:
            os.mkdir(path2)
            print("moving"+filename)  
            shutil.move(path1,path3)  
