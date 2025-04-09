myfile = open("new.txt","w")
myfile.write("hi....i m a human!!!")
myfile.close()


fileout = open("/home/dibyojyoti/Documents/PROGRAMS/new.txt","r")
s = fileout.read()
print(s)