#!C:\Users\Admin\AppData\Local\Programs\Python\Python38\python.exe
import pymysql
import cgi
print("Content-type:text/html\n\r\n\r")
print("<body bgcolor='pink'")
form = cgi.FieldStorage()
sl = form.getvalue('sl')
nm = form.getvalue('nm')
au = form.getvalue('au')
pu = form.getvalue('pu')
cp = form.getvalue('cp')
pr = form.getvalue('pr')
con = pymysql.connect(user='root', password='',
                      host='localhost', database='bookie')
cur = con.cursor()
cur.execute('insert into bookstore values("%s","%s","%s","%s","%s","%s")' % (
    sl, nm, au, pu, cp, pr))
con.commit()
con.close()
print("<h2> Successfully inserted </h2>")
