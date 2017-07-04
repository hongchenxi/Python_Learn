# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''
# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

height = []
tour = []
hei = 100.0
tim = 10
for i in range(1,tim + 1):
    if i == 1:
        tour.append(hei)
    else:
        tour.append(hei*2)
    hei /= 2
    height.append(hei)
print('总共经过tour= {0}米'.format(sum(tour)))
print('第10次反弹高度：height = {0}米'.format(height[-1]))
print tour
print height