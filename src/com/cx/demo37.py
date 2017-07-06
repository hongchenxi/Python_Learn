# _*_ coding: UTF-8 _*_
'''
Created on 2017年7月4日

@author: Chenxi
'''

# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

if __name__ == "__main__":
    N = 10
    print "请输入10个数：\n"
    l = []
    for i in range(N):
        l.append(int(raw_input('输入一个数字: \n')))
    print
    for i in range(N):
        print l[i]
    print
    
# 排列10个数字
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if l[min] >l[j]:min = j
        l[i],l[min] = l[min],l[i]
    print '排列之后'
    for i in range(N):
        print l[i]