#How to find the total size of a file

myfile = open('Poem.txt','r')
str1 = myfile.read()
size = len(str1)
print('Total Size is ',size)
myfile.close()
