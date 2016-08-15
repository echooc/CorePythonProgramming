#coding:utf-8
'''
这里是找字符串的函数
'''

def findchr(string, char):
    if char != '' and string != '':
        if char in string:
            i, j = 0, 0
            while(i<len(char)-1 or j<len(string)-1):
                if list(char)[i] == list(string)[j]:
                    i += 1
                    j += 1
                else:
                    i = 0
                    j += 0
            print j-len(char)+1
        else:
            print '-1'
    else:
        print 'wrong input!'

def rfindchr(string, char):
    if char != '' and string != '':
        if char in string:
            i = len(char)-1
            j = len(string)-1
            while(i!=0 and j!=0):
                if list(char)[i] == list(string)[j]:
                    i -= 1
                    j -= 1
                else:
                    i = len(char)-1
                    j += 0
            print j
        else:
            print '-1'
    else:
        print 'wrong input!'

if __name__ == '__main__':
    rfindchr('ancncn','cn')

