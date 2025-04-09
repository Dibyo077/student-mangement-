
file1 = open("myfile.txt","r")



str1 = file1.readlines()
for i in range(len(str1)):
    print("line",i+1,":",str1[i])
file1.close()  