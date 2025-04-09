# How to write inside a file
outfile = open('out1.txt','w')
n = []
for i in range(5):
    name = input("Enter your name :- ")
    n.append(name +'\n')
outfile.writelines(n)
outfile.close()
