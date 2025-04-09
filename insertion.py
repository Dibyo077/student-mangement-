import mysql.connector as my


def teacher():
    con = my.connect(host='localhost', user='root',
                     passwd='babaisen1234#', db='student_management')
    cur = con.cursor()

    id_ = input("Enter the ID of the teacher: ")
    name = input("Enter the name of the teacher: ")
    subject = input("Enter the subject being taught by the teacher: ")
    no_of_classes_assigned = input(
        "Enter the No.of classes assigned to the teacher: ")
    date_of_join = input(
        "Enter the date of join of teacher (in YYYY-MM-DD format): ")
    salary = input("Enter the salary of the teacher: ")

    sql = '''insert into Teacher values(%s,%s,%s,%s,%s,%s)'''
    v = (id_, name, subject, no_of_classes_assigned, date_of_join, salary)
    cur.execute(sql, v)
    con.commit()
    print("The data of new teacher is successfully added....")

def Student():
    dict_ = {}
    con = my.connect(host='localhost', user='root',
                     passwd='babaisen1234#', db='student_management')
    cur = con.cursor()
    roll = input("Enter the roll of the new student:-")
    name = input("Enter the name of the new student:-")
    class_ = input("Enter the class of the new student:-")
    class_teacher_id = input("Enter the id of the  class tecaher for new student:-")
    doa = input("Enter the date of addmission of the new student(YYYY-MM-DD):-")

    sql_1 = '''select class_teacher_id,class from Student group by class'''
    cur.execute(sql_1)
    data = cur.fetchall()
    for i in data:
        keys = i[1]
        values = i[0]
        dict_[keys]=values
    for a in dict_:
        if int(class_) == a:
            if int(class_teacher_id) == dict_[a]: 
                sql = '''insert into Student values(%s,%s,%s,%s,%s)'''
                v = (roll, name, class_, doa, class_teacher_id)
                cur.execute(sql,v)
                con.commit()
                print("The data of new student is successfully added....")
            else:
                print("The class teacher id is not present...")
                A = input("Do you want to add new teacher with this id..(Y/N)")
                if A.upper() == 'Y' or A == 'Yes':
                    teacher()
        else:
            sql = '''insert into Student values(%s,%s,%s,%s,%s)'''
            v = (roll,name,class_,class_teacher_id,doa)
            cur.execute(sql,v)
            con.commit()
            print("The data of new student is successfully added....")
            break

        
 
def insertion():
   
    con = my.connect(host='localhost', user='root',
                     passwd='babaisen1234#', db='student_management')
    cur = con.cursor()
    print(""""Select 'a' for insert in Teacher Table
              Select 'b' for insert in Student Table
              Select 'c' for insert in Marks Table
           """)
    Ch = (input('Enter Your Choice:-'))
    if Ch == 'a':
        teacher()

    elif Ch == 'b':
        Student()

    elif Ch == 'c':
        stu_id = input('Enter Student ID:-')
        acdmark = input('Enter academic marks of Student:-')
        coactivity = input('Enter Cocuricullar activity of Student:-')
        promarks = input('Enter Marks of Project:-')
        nopro = input('Enter Number of Project Submitted:-')

        sql_1 = '''select Roll_no from Student'''
        cur.execute(sql_1)
        data = cur.fetchall()
        for a in data:
            if int(stu_id) in a:
                sql = '''insert into Marks (Stu_id,academics_marks,Cocurricular_activities, Project_marks,No_of_projects_submitted)values(%s,%s,%s,%s,%s)'''
                v = (stu_id, acdmark, coactivity, promarks, nopro)
                cur.execute(sql, v)
                con.commit()
                print("Added successfully......")
                break
        else:
                print("No student exists with this id...")

    else:
        print("Invalid option")
