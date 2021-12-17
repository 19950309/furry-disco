
#!/usr/bin/python3
#vim: setfileencoding=utf-8:
#filename: save_data.py

import pandas as pd
import tushare as ts

TOKEN = 'ff08684f06ec5a81164471fd1e1c2cca1951bca5fbe34f155ca221fb'

class SaveData:
	def __init__(self):
		self._pro = ts.pro_api(TOKEN)
		self._ver = ts.__version__
		print('tushare version: %s.', str(self._ver))
	
	def daily_data(self,start_date, end_date):
		df = self._pro.daily(start_date=start_date, end_date=end_date)
		print(df)

	
if __name__ == "__main__":
	beg_time = '20210901'
	end_time = '20211216'
	s = SaveData()
	s.daily_data(start_date=beg_time, end_date=end_time)

