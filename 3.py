import pymysql
connect = pymysql.connect(host='localhost',user='root',password='123456',database='tushare')

cursor = connect.cursor()
#定义SQL语句
insert_sql = "insert into stock_daily values('SSE',20210309,1,20210418)"
#执行SQL语句
rows= cursor.execute(insert_sql)
#提交
connect.commit()
connect.close()

