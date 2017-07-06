# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''
# 题目：求100之内的素数。
lower = int(raw_input("输入区间最小值："))
upper = int(raw_input("输入区间最大值："))
for num in range(lower, upper + 1):
#     素数大于1
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                break
        else:
            print num
    