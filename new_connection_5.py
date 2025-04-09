import mysql.connector
mydb = mysql.connector.connect(host='localhost',user = 'myuser1',password = 'mypass',database = 'student')
if mydb.is_connected():
    print("Successfully Connected")
else:
    print("Try Again")

mycur = mydb.cursor()
st = "select * from marks where science > {} and stu_name = '{}'".format(47,'Amar')
mycur.execute(st)
data = mycur.fetchall()
for row in data:
    print(row)
