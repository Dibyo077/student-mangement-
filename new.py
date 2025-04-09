# How to read n bytes and then read some more bytes

myfile = open('Poem.txt','r')
S1 = myfile.read(10)
print(S1)
S2 = myfile.read(5)
print(S2)
myfile.close()
