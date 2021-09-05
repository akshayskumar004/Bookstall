#!C:\Users\Admin\AppData\Local\Programs\Python\Python38\python.exe
import pymysql
con = pymysql.connect(user='root', password='',
                      host='localhost', database='bookie')
cur = con.cursor()
sql = "SELECT * FROM `bookstore` WHERE Copies > 1"
try:
    cur.execute(sql)
    a = cur.fetchall()
    for i in a:
        print(i)
except:
    print("Error: unable to fecth data")
con.close()
