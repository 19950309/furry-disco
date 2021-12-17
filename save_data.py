import tushare as ts
import pymysql
import pandas as pd
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine

pro = ts.pro_api('ff08684f06ec5a81164471fd1e1c2cca1951bca5fbe34f155ca221fb')
df = pro.daily(start_date='20210901', end_date='20211216')
#print(df)
daily_all = create_engine('mysql+pymysql://root:123456@localhost/tushare')
res = df.to_sql('stock',daily_all,index=False,if_exists='append',chunksize=5000)
sql = 'select * from stock'
df = pd.read_sql_query(sql, daily_all)
# print(tushare.__version__)

