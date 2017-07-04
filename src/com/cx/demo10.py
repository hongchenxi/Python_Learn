# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''
# 题目：暂停一秒输出，并格式化当前时间。

import time

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time.sleep(1)
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))