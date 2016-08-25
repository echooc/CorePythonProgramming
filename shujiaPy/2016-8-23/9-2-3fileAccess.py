# coding: utf-8
import os

# def fileAccess(i):
#     yield i
def count(file):
    for i,j in enumerate(open(file, 'r')):
        pass
    return i

# print os.getcwd()
num = raw_input('请输入行数: \n')
filename = raw_input('请输入文件名: \n')
abc = True

if int(num) > count(filename):
    print '您输入的行数超出了文件行数'
else:
# ffile = open(filename, 'r')
    for a, i in enumerate(open(filename, 'rU')):
        if a <= int(num):
            print i

'''
这里实现了 9-2 和 9-3 两个题目的功能
'''


