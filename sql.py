import pymysql

conn = pymysql.connect(
   host='192.168.0.117',
   port=3306,
   user='zhangsan',
   password='123456')

print(conn)
cursor = conn.cursor()
select_sql ='show databases;'
cursor.execute(select_sql)
result=cursor.fetchall()
print(result)
for row in result:
 print(row[0])


