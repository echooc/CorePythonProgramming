#coding: utf-8
from operator import itemgetter
import operator
'''
输入 雇员姓名-编号
然后可以排序
可以根据 雇员姓名 或者 编号
'''

def input():
    prompt = '''
    这里是一个输入的程序
        '''
    employ = {}
    done = True
    while done:
        name = raw_input('雇员姓名: ')
        employ[name] = raw_input('雇员编号: ')
        judge = raw_input('是否继续输入?(y)继续 或者按任意键结束输入').split()[0].lower()
        if judge == 'y':
            done = True
        else:
            done = False

    return employ

def paixu(dic):
    key = dic.keys()
    b = sorted(key)
    for i in b:
        print '雇员: %s' %i + '编号: %s' % dic[i]

    # print dic.keys()
    # for i in dic.keys():
    #     print '雇员: %s' % i + '编号: %s' % dic[i]


'''

:key 的返回值是key 因为 key = dic.keys().sort()中sort()不会返回一个新的list 而是在原有的list上进行排序
None

Process finished with exit code 0
---------------------

    print dic.keys().sort()
    print dic.keys()
再次调用的时候.已经没有了排序的效果 ORZ 给跪了

妈个鸡 sorted就可以哇
>>> students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10),]

用元素索引做 key:
>>> sorted(students, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

----------------------

'''

t = input()
paixu(t)