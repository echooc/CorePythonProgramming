#coding:utf-8
'''
这里是数字和英文翻译对应返回的Demo
太麻烦了 而且英文不会拼写
go died
'''

def trans():
    num = raw_input("please enter numbers(0-1000): ")
    if len(num) == 0:
        print ("emptry!")
    elif len(num) == 1:
        a = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
        print a[num]
    elif len(num) == 2:
        li = list(num)
        b = {'10': 'ten', '11': 'eleven', }

trans()