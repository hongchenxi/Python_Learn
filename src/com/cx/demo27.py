# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''
# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

def output(s, l):
    if l == 0:
        return
    print (s[l-1])
    output(s,l-1)

s = raw_input('Input a string:')
l = len(s)
output(s, l)