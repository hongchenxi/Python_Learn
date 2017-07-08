# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''
# 题目：学习使用按位与 & 。
# 程序分析：0&0=0; 0&1=0; 1&0=0; 1&1=1。

if __name__ == '__main__':
    a = 077
    b = a & 3
    print 'a & b = %d' % b
    b &= 7
    print 'a & b = %d' % b 


        