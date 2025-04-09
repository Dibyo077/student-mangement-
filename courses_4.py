import pymysql
mycon = pymysql.connect("localhost","user","mypass","new_test")
mycur = mycon.cursor()

sql = """ select count(distinct fid)
          from course"""
try:
    mycur.execute(sql)
    result = mycur.fetchone()
    if result:
        print("Unique Fid",result)
except:
    mycon.close()
    mycur.close()
