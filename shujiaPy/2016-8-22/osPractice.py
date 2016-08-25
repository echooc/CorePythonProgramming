# coding: utf-8

import os

for tmpdir in ('/tmp', r'/user/bin/'):#这里应该是元组,待会试试其他的
    if os.path.isdir(tmpdir):#指定路径是否为一个目录
        print tmpdir
    else:
        print '-----'
        print tmpdir
        print 'no temp directory available'
'''
Connected to pydev debugger (build 143.2370)
/tmp
-----
/user/bin/
no temp directory available

Process finished with exit code 0

'''

tmpdir = '/'
if tmpdir:
    os.chdir(tmpdir)#跳转目录到指定目录中去
    cwd = os.getcwd()#显示当前目录
    print '*** current temporary directory'
    print cwd

print '*** creating example directory...'
# os.mkdir('example')
# os.chdir('example')
# cwd = os.getcwd()
# print '*** new working directory: '
# print cwd
#
# Traceback (most recent call last):
#   File "/Users/echoocking/PycharmProjects/Core Python Programming/shujiaPy/2016-8-22/osPractice.py", line 31, in <module>
#     os.mkdir('example')
# OSError: [Errno 13] Permission denied: 'example'

print '*** original directory listing: '
cwd = os.getcwd()
print os.listdir(cwd)#显示目录中的内容

print '*** creating test file...'
fobj = open('test.py', 'r')
# fobj.write('hello\n')
#
# fobj.write('dodo\n') 没有写的权限
print os.listdir(cwd)

for line in fobj:
    print line


fobj.close()
#  运行结果
# jijij
#
# jisajisi
#
# huhsd    看看怎么提权 让脚本有权限

print '*** renameing \'test\' to filetext  '
# os.rename('test.py', 'filetext.py')
#     os.rename('test.py', 'filetext.py')
# OSError: [Errno 13] Permission denied

print '*** update directory listing'
print os.listdir(cwd)

path = os.path.join(cwd, os.listdir(cwd)[0])
print '*** full file pathname'
print path

print '*** (pathname, basename) == '
print os.path.split(path)
# *** (pathname, basename) ==
# ('/', '.DocumentRevisions-V100')
#与path.split()不同 本句需要在括号里添加 , 或者其他的分隔符号,通过括号中的分隔符来对path进行分隔
print '*** (filename, extension) == '
print os.path.splitext(os.path.basename(path)) #('.DocumentRevisions-V100', '')

