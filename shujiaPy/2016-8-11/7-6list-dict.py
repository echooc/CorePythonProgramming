#coding: utf-8

'''
这是一个仿真的题目~

'''

'''
符号:
持有的股票:
购买价格:
当前价位:
其他的数据项任意添加  append()这个函数是list的添加函数,只接受一个参数,但是参数的类型随意
extend 只接受一个参数 是另外的list的名称 是将另外的list元素一个一个添加到原list中
'''

lie = ['fuhao', 'chiyou', 'goumaijiage', 'dangqianjiawei']
li = []
li1 = ['', '', '', '']
# fuhao, chiyou, goumaijiage, dangqianjiage = '', '', '', ''
done = True
while(done):
    li1[0] = raw_input('请输入符号: \n')
    li1[1] = raw_input('请输入持有的股票: \n')
    li1[2] = raw_input('请输入购买价格: \n')
    li1[3] =raw_input('请输入当前价格: ')
    d = raw_input("还需要继续输入么?继续(t/T)中断输入(请按任意键): ").strip().lower()
    li.append(li1)
    if d == 't':
        done = True
    else:
        done = False

print li
prompt ='''
请选择一项数据项,该数据项将作为排序的依据
(F)符号
(C)持有
(G)购买
(D)当前价位
'''
xuanze = ['f', 'c', 'g', 'd']
keys = raw_input(prompt).strip()[0].lower()
dic = {}
if keys in xuanze:
    if keys == xuanze[0]:
        i = 0
        j = 0
        while(i < len(li)):
            dic[li[i][j]] = li[i]
            i += 1
    elif keys == xuanze[1]:
        i = 0
        j = 1
        while(i < len(li)):
            dic[li[i][j]] = li[i]
            i += 1
    elif keys == xuanze[2]:
        i = 0
        j = 2
        while(i < len(li)):
            dic[li[i][j]] = li[i]
            i += 1
    elif keys == xuanze[3]:
        i = 0
        j = 3
        while(i < len(li)):
            dic[li[i][j]] = li[i]
            i += 1
else:
    print 'wrong input'
print dic


