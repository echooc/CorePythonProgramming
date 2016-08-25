#coding: utf-8

'''
阶乘
7 = 7 * 6 * 5 * 4 * 3 * 2 * 1
'''
#尝试并没有成功 没有想到使用生成器完成阶乘的比较好的方法
# def jie(a):
#     i = 0
#     while(i<a):
#         yield i
#         i += 1
#         print 'i: '+i
#
# a=jie(3)
# for i in jie(3):
#     i*(i+1)

def jicheng(a):
    if a < 0:
        print '抱歉您所输入的数字没有阶乘'
    elif a == 0:
        print '0的阶乘是1'
    elif a > 0:
        abc = 1
        for i in range(1, a+1):
            abc= i * abc
        print '您所输入的%d的阶乘是: %d' % (a, abc)
    else:
        print '您输入的不是数字,请输入一个数字'

a = int(raw_input('请输入一个数字: '))
jicheng(a)