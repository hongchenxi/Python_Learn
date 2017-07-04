# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''
# 题目：将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。

# 方法一
a = [1, 2, 3]
b = a[:]
print b

# 方法二: Python2
import copy
a = [2, 3, 4]
b = copy.copy(a)
print b

# 方法三：Python3
a = [3, 4, 5]
b = a.copy()
print b

    