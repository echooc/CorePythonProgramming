#coding: utf-8

'''
使用 if 判断
很多啦 又不是很有技术
所以不写
like this
'''
tmp1=eval(raw_input('pls input set A,separate by comma:'))
tmp2=eval(raw_input('pls input set B:separate by comma:'))
A=set(tmp1)
B=set(tmp2)
print A
print B
while True:
    op=raw_input('pls choose a operator from (in,not in,&,|,^,<,<=,>,>=,==,!=) for A operator B:')
    if 'in'==op:
        print 'A in B is: ',A in B
    elif 'not in'==op:
        print 'A not in B is: ',A not in B
    elif '&'==op:
        print 'A & B is: ',A&B
    elif '|'==op:
        print 'A | B is: ',A|B
    elif '^'==op:
        print 'A ^ B is: ',A^B
    elif '<'==op:
        print 'A < B is: ',A<B
    elif '<='==op:
        print 'A <= B is: ',A<=B
    elif '>'==op:
        print 'A > B is: ',A>B
    elif '>='==op:
        print 'A >= B is: ',A>=B
    elif '=='==op:
        print 'A == B is: ',A==B
    elif '!='==op:
        print 'A != B is: ',A!=B
    else:
        print 'input error'
        break