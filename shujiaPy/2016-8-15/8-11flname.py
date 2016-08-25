#coding: utf-8

do = True
count = 0
while(do):
    a = raw_input('请输入姓名。(名,姓): ').strip()
    li = list(a)
    if ',' in li :
        if ',' != li[-1]:
            print "%s %s" %(a.split(',')[1], a.split(',')[0])
            do = False
        else:
            print '逗号不能在末尾 请重新输入'
            count +=1
            print '您输入错误的次数为: %d' %count

    else:
        print '请使用','分隔姓和名,输入错误请重新输入。'
        count +=1
        print '您输入错误的次数为: %d' %count

# Connected to pydev debugger (build 143.2370)
# 请输入姓名。(名,姓): echo
# 请使用 分隔姓和名,输入错误请重新输入。
# 您输入错误的次数为: 1
# 请输入姓名。(名,姓): echo,
# 逗号不能在末尾 请重新输入
# 您输入错误的次数为: 2
# 请输入姓名。(名,姓): echo,zeng
# zeng echo
#
# Process finished with exit code 0