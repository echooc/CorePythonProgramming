#coding: utf-8
'''
这里是一个 大小写翻转的demo
'''

def upLow():
    world = list(raw_input('enter your worlds:'))
    i = 0
    while(i < len(world)):
        if world[i].islower():
            world[i] = world[i].upper()
            i += 1
        else:
            world[i] = world[i].lower()
            i += 1
    print ''.join(world)

'''
这里学到了列表和字符串之间的转换方法
列表转字符串: ''.join(list)
字符串转列表: list(str)
其他转元组: tuple()
'''

'''
下面是一个改错程序
也是6-10
我不知道为什么 - -
'''
#从标准输入输出设备输入一个字符串
num_str = raw_input('enter  a number :  ')

#将字符串 转为 int数字类型

num_num = int(num_str)

#第二个到最后一个数字
fac_list = range(1, num_num-1)
print 'BEFORE:', '%s'% fac_list

#初始值
i = 0

#当 i<fac_list时执行循环
while i < len(fac_list):
#
    if num_num % fac_list[i] == 0:
        del fac_list[i]
    i += 1
print 'AFTER:', '%s' % fac_list