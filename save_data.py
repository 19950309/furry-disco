#!/usr/bin/python3
# vim: set fileencoding= utf-8

import tushare as ts
def pull_tushare_data(beg_date, end_date, filename):
    ts.set_token('ff08684f06ec5a81164471fd1e1c2cca1951bca5fbe34f155ca221fb')
    pro = ts.pro_api()
    df = pro.daily(exchange= '',start_date=beg_date, end_date=end_date)
#    with open(filename,'w') as file_object:
 #       for index,row in df.iterrows():
  #           file_object.write(str(index)+ ' ' + str(row) + '\n')
    df.to_csv(filename)

if __name__ == '__main__':
    pull_tushare_data(beg_date='20211021', end_date='20211113', filename='daily_tushar.txt')
