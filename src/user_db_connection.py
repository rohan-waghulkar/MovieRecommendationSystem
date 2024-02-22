import mysql.connector
conn=None
def make_db_connection():
    global conn 
    print("hello")
    conn=mysql.connector.connect(host="localhost",username="root",password="rohan-121",database="recommendation_db")
    print("hello")
    my_cursor=conn.cursor()



def admit_user(username,password,mobile_number):
    make_db_connection()
    my_cursor=conn.cursor()
    my_cursor.execute("CREATE TABLE IF NOT EXISTS user(username varchar(25) UNIQUE,password varchar(20) not null,mobile_number varchar(10) not null,primary key(username))")
    sql ="INSERT INTO user (username, password, mobile_number) VALUES (%s,%s,%s)"
    my_cursor.execute(sql,(username,password,mobile_number))
    print("Entry done")
    conn.commit()
    my_cursor.close()


def user_in_db(username,password):
    make_db_connection()
    my_cursor=conn.cursor()
    sql="select username,password from user where username=%s"
    my_cursor.execute(sql,(username,))

    for (u_name,passwd) in my_cursor.fetchall():
        if u_name==str(username) and passwd==str(password):
            return True
    return False
    

# make_db_connection()
# admit_user("rohan","rohan","8767885882")
