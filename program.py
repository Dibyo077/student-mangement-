
import insertion
import update
def query():
    A = 'Y'
    
    while A.upper() == 'Y' or A == 'Yes':
        print('''Select 1 for teacher information
         Select 2 for Student information
         Select 3 for Student's marks information
         Select 4 for insertion
         Select 5 for update''')
        Ch = int(input("Enter choice: "))
        import mysql.connector as my
        con = my.connect(host = 'localhost',user = 'root',passwd = 'babaisen1234#',db='student_management')
        cur =con.cursor()
        if Ch == 1:
            Enter = input("Enter teacher's id for the required information(id starting from 100:-)")
            print ("""Select 'a' for teacher's name  
                Select 'b' for subject 
                Select 'c' for  total number of classes assigned to the teacher
                Select 'd' for date of join 
                Select 'e' for salary
                select 'f' for full information altogether """)
            in_ = input("Enter your choice :- ")
        
            if in_.lower() == 'a':
                sql = "select Name from teacher where id ="+ Enter 
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])
            

            elif in_.lower() == 'b':
                sql = "select Subject from teacher where id ="+Enter 
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])

            elif in_.lower() == 'c':
                sql = "select No_of_classes_assigned from teacher where id ="+ Enter 
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])

            elif in_.lower() == 'd':
                sql = "select Date_of_join  from teacher where id ="+ Enter
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])

            elif in_.lower() == 'e':
                sql = "select salary from teacher where id ="+ Enter 
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])

        


            elif in_.lower() == 'f':
                sql = "select * from teacher where id ="+ Enter 
                cur.execute(sql)
                data = cur.fetchone()
                print(f"""Teacher's id ={Enter}
                Teacher's Name ={data[1]}
                Teacher's Subject ={data[2]}
                Number of classes assigned to the teacher ={data[3]}
                Teacher's date of joining ={data[4]}
                Teacher's salary = {data[5]}""")
            else:
                print("Invalid option")


    
        
        elif Ch == 2:
            print('''Press 'a' for Student's name
            Press 'b' for Class
            Press 'c' for Student's Class Teacher
            Press 'd' for Date of Admission
            Press 'e' for Entire Student Information''')
            Ch = input('Enter Your Choice:-')
            rol = input("Enter Student's Roll Number:-")
            if Ch == 'a':
                sql = f'''Select Name from student where Roll_no={rol}'''
                cur.execute(sql)
                data = cur.fetchone()
                print("Student's Name =",data[0])
            elif Ch == 'b':
                sql2 = f'''Select Class from Student where Roll_no = {rol}'''
                cur.execute(sql2)
                data = cur.fetchone()
                print("Student's Class =",data[0])
    
            elif Ch == 'c':
                sql3 =f'''Select Name,id from teacher join teacher.id = Student.class_teacher_id '''
                cur.execute(sql3)
                data = cur.fetchone()
                print("Student's Class Teacher's Id =",data[0])
            elif Ch == 'd':
                sql4 = f'''select Date_of_Addmission from student where Roll_no = {rol}'''
                cur.execute(sql4)
                data = cur.fetchone()
                print("Studemt's Date of Addmission =",data[0])
            elif Ch == 'e':
                sql5 = f'''select * from student where Roll_no = {rol}'''
                cur.execute(sql5)
                data = cur.fetchone()
                print(f"""Student's Roll No ={rol}
                Student's Name ={data[1]}
                Student's Class ={data[2]}
                Student's Class Teacher's Id ={data[3]}
                Studemt's Date of Addmission ={data[4]}""") 
            else:
                print("Invalid option")
        
        elif Ch == 3:
            print("""Select 'a' for Academic marks
            Select 'b' for Co-curricular Activites
            Select 'c' for Project Marks
            Select 'd' for No. of Projects Submitted
            Select 'e' for Overall Percentage
            Select 'f' for all information
            """)
            in_ = input("Enter option: ")
            if in_.lower() == 'a':
                id = input("Enter id: ")
                sql= f"select academic_marks from marks where Stu_id = {id}"
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])
            elif in_.lower() == 'b':
                id = input("Enter id: ")
                sql= f"select Cocurricular_activities from marks where Stu_id = {id}"
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])
            elif in_.lower() == 'c':
                id = input("Enter id: ")
                sql= f"select Project_marks from marks where Stu_id = {id}"
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])
            elif in_.lower() == 'd':
                id = input("Enter id: ")
                sql= f"select No_of_projects_submitted from marks where Stu_id = {id}"
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])
            elif in_.lower() == 'e':
                id = input("Enter id: ")
                sql= f"select Overall_percentage from marks where Stu_id = {id}"
                cur.execute(sql)
                data = cur.fetchone()
                print(data[0])
            elif in_.lower() == 'f':
                id = input("Enter id: ")
                sql= f"select * from marks where Stu_id = {id}"
                cur.execute(sql)
                data = cur.fetchone()
                print(f"""
                Id of the student is {data[0]}
                Academics mark is {data[1]} 
                Cocurricular Acitivity is {data[2]}
                Project marks is {data[3]} 
                No. of Project Submitted is {data[4]}
                Overall Percentage is {data[5]}""")
            else:
                print("Invalid option")

        elif Ch == 4 :
            insertion.insertion()
        elif Ch == 5:
            update.update()
        else:
            print("Invalid option")

        A = input("Do you want to contine(Yes/No):-")
query()
