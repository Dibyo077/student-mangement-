# How to find the size of a file after 
myfile = open('Poem.txt','r')
str1 = " "
size = 0
tsize = 0
while str1:
    str1 = myfile.readline()
    size = size+len(str1)
print("Total Size of the file is ", size)
myfile.close()
