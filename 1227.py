import pymysql.cursors

connection = pymysql.connect(host='localhost',user='root',password='123456',db='tushare',charset='utf8')

try:
    cursor = connection.cursor()
    sql = 'select * from stock '
    result = cursor.execute(sql)
  #  result = cursor.fetchall()
   # for data in result:
   #     print(data)
    print(result)

except Exception :print('查询失败！')

cursor.close()
