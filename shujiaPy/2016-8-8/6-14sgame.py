#coding:utf-8
from random import uniform
import random

'''
这是一个剪刀石头布的游戏
你需要输入你出的就可以了
自己的想着太麻烦了
所以百度了思路
这思路挺不错的
先把所有的可能情况做成一个list
然后 随机的选择生成
再把所有的结果做成一个二元的list
在把结果一个个对比
其中[[,],[,],[,]]
以及random.choice
以及strip 取出空格
今天 学的不是特别的多
不过我觉得很充实 比前几天好一些了
坚持
'''

def game(inp):
    pass

def game1():
    while True:
        all_item = ['剪刀', '石头', '布']
        usr = raw_input("用户请输入: ").strip()
        win_item = [['剪刀', '布'],['石头', "剪刀"], ['布', '石头']]
        computer = random.choice(all_item)
        if usr in all_item:
            if [computer, usr] in win_item:
                print ('电脑: %s  ' %computer + "用户: %s " %usr)
                print ("电脑胜利")
            elif computer == usr:
                print ("平局")
            else:
                print ('电脑: %s' %computer + "用户: %s" %usr)
                print ('人胜利')
        else:
            print ("用户输入错误!")

game1()