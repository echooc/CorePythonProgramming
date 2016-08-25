#coding: utf-8
count = 0
def gene(i):
    yield i


def bitOperation():
    while(True):
        print ('SAMPLE OUTPUT %d') % count
        print '------------------'
        min = raw_input('Enter begin value: ')
        max = raw_input('Enter end value: ')
        if int(min) > 128:
            print 'DEC     BIN     OCT     HEX'
            for i in range(int(min), int(max)+1):
                 digit= gene(i)
                 print '%d     %s     %o     %s' % (i, bin(i), i,  hex(i))
        else:
            print 'DEC     BIN     OCT     HEX     ASCII'
            for i in range(int(min), int(max)+1):
                 digit= gene(i)
                 print '%d     %s     %o     %s     %s' % (i, bin(i), i,  hex(i), chr(i))

bitOperation()
print '\n %s ' %chr(5)

# /System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7 "/Users/echoocking/PycharmProjects/Core Python Programming/shujiaPy/2016-8-16/8-12Bit_operation.py"
# SAMPLE OUTPUT 0
# ------------------
# Enter begin value: 5
# Enter end value: 10
# DEC     BIN     OCT     HEX     ASCII
# 5     0b101     5     0x5     
# 6     0b110     6     0x6     
# 7     0b111     7     0x7     
# 8     0b1000     10     0x8     
# 9     0b1001     11     0x9
# 10     0b1010     12     0xa
#
#
#  
#
# Process finished with exit code 0
#  不知道为什么 没有chr的输出??

# ord() 输入一个字符 然后返回ascll码
# chr() 输入ascll对应的十进制 然后输入ascll对应的符号
