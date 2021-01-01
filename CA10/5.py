# import os 

# filelist = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c','c.ayjx']



# for i in range(len(filelist)):

#     x=filelist[i].find('.')

#     filelist.sort(key=lambda x: os.path.splitext(x))
# print (filelist)
import os

filelist  =['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']

def ext_sort(files):
    return sorted(files,key=lambda x: os.path.splitext(x)[1])

print(ext_sort(filelist ))
