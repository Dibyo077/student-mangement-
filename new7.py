#How to find the number of lines in a file
myfile = open('Poem.txt','r')
S1 = myfile.readlines()
count = len(S1)
print(S1)
print('Total lines = ',count)
myfile.close()
