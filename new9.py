#How to insert multiple information inside a file
count = int(input("How many studentsyou want to add more:- "))
fileout = open('info.txt','a')
for i in range(count):
    roll_no = int(input("Entre roll no"))
    name = input("Enter Name")
    marks = int(input("Enter Marks "))
    A = str(roll_no) + "," +name+ "," +str(marks)+'\n'
    fileout.write(A)
fileout.close()
