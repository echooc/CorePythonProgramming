# coding:utf-8
import re
'''
这里是 strip 代替函数的编程
\s 匹配所有字符串前后的所有非空白
\w 匹配一个字符的空白
'''

def st():
    a = '   bbb    '
    b = re.sub(r'\s', '', a)
    print b
st()

a = '    f   bffm   '
print a.strip()[-1].lower()
print a.strip()


'''
Connected to pydev debugger (build 143.1919)
bbb
m          这里可以看出 strip()这个函数返回的是一个 内容为单个字符的(列表)
f   bffm   这里看出 strip()不能取出字符串中间的 空格

Process finished with exit code 0

'''