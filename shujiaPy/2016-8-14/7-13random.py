#coding: utf-8
from random import randint,randrange

'''
生成0-9中随机选择的次数在1-10个的随机数
'''
def ran():
    i = 0
    a = set()
    b = set()
    while(i<randint(1, 10)):
        st1 = str(randint(0, 9))
        st2 = str(randint(0, 9))
        a.update(st1)
        b.update(st2)
        print a, b
        print a | b
        print a & b
        i += 1

ran()

# set.update()的参数需要可以迭代的
# 更不能直接赋值set啦
# 数字串是不能迭代的啦
# 集合,列表,字典都有自己的添加元素的方法
# list
# append()
# extend()
# +
# insert('a', 2)  