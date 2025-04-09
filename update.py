import mysql.connector as my
def Teacher():
    con = my.connect(host='localhost', user='root',
                     passwd='babaisen1234#', db='student_management')
    cur = con.cursor()
    print ("""Select 'a' for  updating in teacher's name  
                Select 'b' for updating  subject 
                Select 'c' for updating   total number of classes assigned to the teacher
                Select 'd' for updating  date of join 
                Select 'e' for updateing salary  """)
    in_ = input("Enter your choice :- ")
        
    if in_.lower() == 'a':
        id_ = input("Enter the id of the Teacher")
        name = input("Enter the new name :- ")
                
        sql = "update Teacher set name = %s where id = %s"
        value = (name,id_) 
        cur.execute(sql,value)
        con.commit()
        print("The name updated successfully....")
            

    elif in_.lower() == 'b':
        id_ = input("Enter the id of the Teacher:-")
        subject = input("Enter the new subject :- ")
                
        sql = "update Teacher set subject = %s where id = %s"
        value = (subject,id_) 
        cur.execute(sql,value)
        con.commit()
        print("The subject updated successfully....")
            
               

    elif in_.lower() == 'c':
        id_ = input("Enter the id of the Teacher:-")
        nca = input("Enter the new number of classes assigned :- ")
                
        sql = "update Teacher set  No_of_classes_assigned = %s where id = %s"
        value = (nca,id_) 
        cur.execute(sql,value)
        con.commit()
        print("The number of classes assigned updated successfully....")
            

    elif in_.lower() == 'd':
        id_ = input("Enter the id of the Teacher:-")
        doj = input("Enter the new date of join :- ")
            
        sql = "update Teacher set  Date_of_join = %s where id = %s"
        value = (doj,id_) 
        cur.execute(sql,value)
        con.commit()
        print("The date of join updated successfully....")
            
               

    elif in_.lower() == 'e':
        id_ = input("Enter the id of the Teacher:-")
        salary = input("Enter the new date of join :- ")
        sql = "update Teacher set salary =%s where id =%s" 
        value = (salary,id_) 
        cur.execute(sql,value)
        con.commit()
        print("The salary updated successfully....")
               
    else:
        print("Invalid option")


def marks():
    con = my.connect(host='localhost', user='root',
                     passwd='babaisen1234#', db='student_management')
    cur = con.cursor()
    print("""Select 'a' for updating Academic marks
         Select 'b' for updating Co-curricular activites
         Select 'c' for updating Project marks
         Select 'd' for updating No. of Projects submitted""")

    a = input("Enter choice: ")

    if a.lower() == 'a':
        id_ = input("Enter id: ")
        update = input("New value: ")
        sql = "update Marks set academics_marks = %s where Stu_id = %s"
        cur.execute(sql, (update, id_))
        con.commit()
        print("The Academic marks updated successfully....")

    elif a.lower() == 'b':
        id_  = input("Enter id: ")
        update = input("New value: ")
        sql = "update Marks set Cocurricular_activities = %s where Stu_id = %s"
        cur.execute(sql, (update, id_))
        con.commit()
        print("The Co-curricular activites updated successfully....")
        

    elif a.lower() == 'c':
        id_  = input("Enter id: ")
        update = input("New value: ")
        sql = "update Marks set Project_marks = %s where Stu_id = %s"
        cur.execute(sql, (update, id_))
        con.commit()
        print("The Project marks updated successfully....")
        

    elif a.lower() == 'd':
        id_ = input("Enter id: ")
        update = input("New value: ")
    
        sql = "update Marks set No_of_projects_submitted = %s where Stu_id = %s"
        cur.execute(sql, (update, id_))
        con.commit()
        print("The No of projects submitted updated successfully....")

    else:
        print("Invalid option")

def student():
    con = my.connect(host='localhost', user='root',
                     passwd='babaisen1234#', db='student_management')
    cur = con.cursor()
    print ("""Select 'a' for updating name  
                Select 'b' for updating class
                Select 'c' for  updating Date_of_Addmission""")
    in_ = input("Enter your choice :- ")


    if in_.lower() == 'a':
        id_ = input("Enter the id of the Student:")
        class_ = input('Enter New Name of the student:-')
        sql = "update Student set Name = %s  where Roll_no =%s" 
        cur.execute(sql,(class_,id_))
        con.commit()
        print("The name updated successfully....")
            

    elif in_.lower() == 'b':
        id_ = input("Enter the id of the Student:")
        class_ = input('Enter New class of the student:-')
        sql = "update Student set class = %s  where Roll_no =%s"
        cur.execute(sql,(class_,id_))
        con.commit()
        print("The class updated successfully....")
            

    elif in_.lower() == 'c':
        id_ = input("Enter the id of the Student:")
        class_ = input('Enter New Date_of Addmission of the student:-')
        sql = "update Student set Date_of_addmission = %s  where Roll_no =%s" 
        cur.execute(sql,(class_,id_))
        con.commit()
        print("The date of addmission  updated successfully....")
        
    else:
         print("Invalid option")
     
    
def update():
   
    con = my.connect(host='localhost', user='root',
                     passwd='babaisen1234#', db='student_management')
    cur = con.cursor()
    print(""""Select 'a' for update in Teacher Table
              Select 'b' for update in Marks Table
              Select 'c' for update in Student Table
           """)
    Ch = (input('Enter Your Choice:-'))
    if Ch == 'a':
        Teacher()

    elif Ch == 'b':
        marks()

    elif Ch == 'c':
        student()
       
