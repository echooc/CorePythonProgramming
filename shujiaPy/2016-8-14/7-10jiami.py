#coding: utf-8

'''
前半部分的子母变为后半部分的子母
chr()返回字符
ord()返回ascll码
'''

def jiami(letter):
    print ord('a'),'----', ord('z'), '-------', ord('A'), '----', ord('Z')
#97 ---- 122 ------- 65 ---- 90
    ascll = ord(letter)
    if (109>=ascll & ascll>=97):
        newAsc = ascll+13
    elif  (ascll>=110 & ascll<=122):
        newAsc = ascll - 13
    elif (ascll>=65 & ascll<= 77):
        newAsc = ascll + 13
    elif (ascll>78 & ascll <=90):
        newAsc = ascll - 13
    else:
        print '输入的不是字符,请输入一个字符'
    print chr(newAsc)


jiami('d')
'''
97 ---- 122 ------- 65 ---- 90
q

Process finished with exit code 0
正确.
'''