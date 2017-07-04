# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''
# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。

import time
myD = {1: 'a', 2: 'b'}

for key, value in dict.items(myD):
    print key, value
    time.sleep(1.0) # 暂停一秒