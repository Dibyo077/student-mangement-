# How to find the size of a file after remoing EOL char
myfile = open('Poem.txt','r')
str1 = " "
size = 0
tsize = 0
while str1:
    str1 = myfile.readline()
    size = size+len(str1)
    tsize = tsize+len(str1.strip())
print("Total Size of the file is before removing is ", size)
print("Total Size of the file is after removing is ", tsize)
myfile.close()
