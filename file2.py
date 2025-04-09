fileout = open("myfile.txt","w")
for i in range(5):
    name = input("enter the name:")
    fileout.write(name)
    fileout.write('\n')
fileout.close()    
  
