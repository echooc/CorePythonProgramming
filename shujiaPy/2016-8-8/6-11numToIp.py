# coding: utf-8

'''
这里是一个输入证书 转换为IP地址的DEMO
'''
def trans(num):
    s = []
    for i in range(4):
        s.append(num%256)
        print s
        num /= 256
    return '.'.join(s[::-1])

trans(123545678)