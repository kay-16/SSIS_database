import mysql.connector as mysql


def initialise_conn():
    connec = mysql.connect(
        host = "localhost",
        user = "root",
        password = "elijang0011!!"
    )

    C = connec.cursor()
    use_student_database(C)
    student_table(C)
    course_table(C)

    return connec, C
    

def use_student_database(C):
    C.execute("SHOW DATABASES")
    temp = C.fetchall()
    databases = [item[0] for item in temp]

    if "sql_ssis" not in databases:
        C.execute("CREATE DATABASES sql_ssis")

    C.execute("USE sql_ssis")


def student_table(C):
    C.execute("SELECT * FROM student")
    rows = C.fetchall()
    for row in rows:
        print(row)


def course_table(C):
    C.execute("SELECT * FROM course")
    rows = C.fetchall()
    for row in rows:
        print(row)




