import pymysql
mycon = pymysql.connect("localhost","user","mypass","new_test")
mycur = mycon.cursor()

sql = """ select *
          from course
          where fees BETWEEN %s AND %s"""
value = (15000,50000)
try:
    mycur.execute(sql,value)
    if mycur.rowcount == 0:
        raise ValueError("No Such Course Is Present")
    result = mycur.fetchall()
    for row in result:
        cid = row[0]
        fid = row[1]
        cname = row[2]
        fees = row[3]
        print("Course Id " , cid)
        print("Faculty Id", fid)
        print("Course Name = ", cname)
    print("Number of rows found = ", mycur.rowcount)
except ValueError as err:
    print(err)
    print("Invaid Fees Structure")
    mycon.rollback()
    mycon.close()
    mycur.close()
