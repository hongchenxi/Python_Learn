# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''
# 题目：输出指定格式的日期。
# 程序分析：使用 datetime 模块。

import datetime

if __name__ == '__main__':
    
# 输出今日日期，格式为 dd/mm/yyyy
    print(datetime.date.today().strftime('%d/%m/%Y'))

# 创建日期对象
    testDate = datetime.date(1992, 9, 22)
    print(testDate.strftime('%d/%m/%Y'))
    
# 日期算数运算
    nextDate = testDate + datetime.timedelta(days =1)
    print(nextDate.strftime('%d/%m/%Y'))
    
# 日期替换
    firstDay = testDate.replace(year = testDate.year + 1)
    print(firstDay.strftime('%d/%m/%Y'))
    
    