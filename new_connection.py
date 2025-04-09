import mysql.connector
mydb = mysql.connector.connect(host='localhost',user = 'myuser',password = 'mypass',database = 'student')
if mydb.is_connected():
    print("Successfully Connected")
else:
    print("Try Again")

mycur = mydb.cursor()
stu_name = 'Dibojyoti'
roll_no = 3
inp = (stu_name,roll_no)
query = "update marks set stu_name = %s where roll_no = %s"
mycur.execute(query,inp)
data = mycur.fetchall()
for row in data:
    print(row)
