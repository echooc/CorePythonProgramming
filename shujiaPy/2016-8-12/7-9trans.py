#coding: utf-8

'''

'''
def rfindchr(string, char):
    if char in string:
        index = string.find(char, 0)
        return index
    else:
        print 'not in '

def tr(srcstr, dststr, string):
    # id = rfindchr(string, srcstr)
    li = list(string) #单个存储着string所有的字符

    id =0
    newstring = string
    while(len(string)-id > len(srcstr)):
        id = rfindchr(newstring, srcstr)
        count = 0
        while(count < len(dststr)):
            li[id] = list(dststr)[count] #是string中 需要被替换的地方
            count += 1
            id += 1
            newstring = ''.join(li)

        # if len(string)-id > len(srcstr):
    return li

if __name__ == '__main__':
    print '原字符串和目的字符串的长度相同,且基本字符串的长度需要大于原字符串'
    srcstr = raw_input('请输入原字符串: ')
    dststr = raw_input("请输入目的字符串: ")
    string = raw_input('请输入基本字符串: ')
    print tr(srcstr, dststr, string)

