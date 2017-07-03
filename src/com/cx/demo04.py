# -*- coding: utf-8 -*-
'''
Created on 2017年7月4日

@author: hongchenxi
'''
import time
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

# 方法1：Python3
# date = input("输入年月日（yyyy-mm-dd）：")
# y,m,d = (int(i) for i in date.split('-'))
# special = (1, 3, 5, 7, 8, 10, 12)
# for i in range(1, int(m)):
#     if i == 2:
#         if y % 400 == 0 or (y % 100 != 0 and y%4 == 0):
#             sum += 29
#         else:
#             sum += 28
#     elif(i in special):
#         sum += 31
#     else:
#         sum += 30
# sum += d
# print("这一天是%d年的第%d天"%y%sum)

# 方法2
# date = raw_input("输入年月日（yyyy-mm-dd）：")
# dd = time.strptime(date,'%Y-%m-%d').tm_yday
# print("这一天是一年中的第{}天".format(dd))

# 方法3
year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))
days = [31,28,31,30,31,30,31,31,30,31,30,31]
if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):
    days[1] += 1
now = sum(days[0:month - 1])+day
print("这一天是一年中的第%d天"%now)