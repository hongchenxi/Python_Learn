# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''
# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。
TRUE = 1
FALSE = 0
def SQ(x):
    return x*x
print '如果平方运算后小于 50 则退出'
again = 1
while again:
    num = int(raw_input('请输入一个数字：'))
    print '运算结果为：%d' %(SQ(num))
    if SQ(num) >= 50:
        again = TRUE
    else:
        again = FALSE
           
        