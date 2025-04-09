import pymysql
mycon = pymysql.connect("localhost","user","mypass","new_test")
mycur = mycon.cursor()

new = int(input("Enter update value"))
course = eval(input("Enter course name "))

sql1 = """ update course
            set fees = fees + %s
            where cname = %s """

sql2 = """ select * from course
            where cname = %s """

sql3 = """ select * from course
            where cname =  %s"""
value1 = (new,course)
value2 = (course,)
try:
    mycur.execute(sql2,value2)
    if mycur.rowcount == 0:
        raise ValueError("No such course is present")
    else:
        mycur.execute(sql1,value1)
        mycon.commit()
        mycur.execute(sql3,course)
        result = mycur.fetchall()
        for row in result:
            cid = row[0]
            fid = row[1]
            cname = row[2]
            fees = row[3]
            print("course id " , cid)
            print("faculty id", fid)
            print("course name = ", cname)
            print("Fees = ",fees)
except ValueError as err:
    print(err)
    print("Invalid Course")
    mycon.rollback()
    mycon.close()
    mycur.close()
