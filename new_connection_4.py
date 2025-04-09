import mysql.connector
mydb = mysql.connector.connect(host='localhost',user = 'myuser',password = 'mypass',database = 'student')
if mydb.is_connected():
    print("Successfully Connected")
else:
    print("Try Again")

mycur = mydb.cursor()
st = "select * from marks where science >%s and roll_no > %s" % (60,3)
mycur.execute(st)
data = mycur.fetchall()
for row in data:
    print(row)
