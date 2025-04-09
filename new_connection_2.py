import mysql.connector
mydb = mysql.connector.connect(host='localhost',user = 'myuser',password = 'mypass',database = 'student')
if mydb.is_connected():
    print("Successfully Connected")
else:
    print("Try Again")

mycur = mydb.cursor()
mycur.execute("select * from marks")
data = mycur.fetchmany(3)
count = mycur.rowcount
print("Number of rows fetched = ", count)
for row in data:
    print(row)
