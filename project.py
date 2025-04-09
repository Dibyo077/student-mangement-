import mysql.connector
mycon = mysql.connector.connect(host = 'localhost',user = "root",passwd = "babaisen1234#",database = "student_management")
mycur = mycon.cursor()
sql_1 = """create table if not exists Teacher(
    id int not null  primary key,
    Name varchar(25) not null,
    Subject varchar(25) not null,
    No_of_classes_assigned int not null,
    Date_of_join date not null,
    salary int not null
) """
mycur.execute(sql_1)
mycon.commit()

sql_2 = """create table if not exists Student(
    Roll_no int not null  primary key,
    Name varchar(20) not null,
    class int not null,
    class_teacher_id int not null,
    
    Date_of_addmission date not null,
    foreign key (class_teacher_id) references Teacher(id)
    on delete cascade on update cascade
) """
mycur.execute(sql_2)
mycon.commit()

sql_3= """  create table if not exists Marks(
  Stu_id int not null,
    academics_marks int not null,
    Cocurricular_activities int not null,
    Project_marks int not null,
    No_of_projects_submitted int not null,
    Overall_percentage  float not null as (((academics_marks+Cocurricular_activities+Project_marks)/300)*100) ,
    foreign key (Stu_id) references Student(Roll_no)
    on delete cascade on update cascade
) """
mycur.execute(sql_3)
mycon.commit()