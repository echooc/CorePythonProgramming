#coding: utf-8

'''
这里是一个日期差值计算的demo
对于日期 有 DD/MM/YY 格式,计算出两个日期的差值
这是基础 然后再继续对月份进行判断
1 3 5 7 8 10 12月为31日
其余为 30 日
对于 年份来说闰年日子不同 且2月份计算日子不同
每一个写一个if的判断
迭代器不太可能
还是做判断
恩所以不再继续写了
'''

def caculate(date1, date2):
    # 使用 分割的函数 将DD MM YY变成list
    date11 =date1.split('/', 2)
    date22 =date2.split('/', 2)
    day1 = int(date11[0])*365 + int(date11[1])*30 + int(date11[2])
    day2 = int(date22[0])*365 + int(date22[1])*30 + int(date22[2])
    print abs(day1-day2)

caculate('2016/5/2', '2014/5/2')