#How to read complete file - line by line
myfile = open('Poem.txt','r')
str1= " "
while str1:
    str1 = myfile.readline()
    print(str1,end = ' ')
myfile.close()
