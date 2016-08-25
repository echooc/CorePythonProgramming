#coding: utf-8

def fe():
    yield 5
    yield 6

a = ((i, n) for i in range(0, 10) for n in fe())
for i in a:
    print i

def fe1():
    yield 5
    print '111111'
    yield 6
    print '222222'
a = (n for n in fe())

for i in a:
    print i
'''
1过程:
a 返回一个生成器的对象
for 循环开始时计算a
然后 返回a的计算,其中n的计算需要使用到fe函数
所以调用fe函数 到yield5 返回yeild的值并且中止fe函数的执行
到a i和n都计算出 所以得到a的值 成功的执行for循环的一次循环
下一次循环开始时又需要计算a 然后大同小异,不同的地方为 执行fe函数时 直接跳到yeild的下一句开始执行

2过程:
a 需要获取值 然后调用fe fe函数调用后
返回5,然后进行循环,一次循环完成后
在进行下一次循环时需要获取a的值 然后再次调用fe函数
fe函数返回从yeild5后开始执行先输出然后到yeild6,返回值为6
然后进行循环。完成循环后再次开始循环时继续到fe函数中。从yeild6 之后开始运行
输出后 fe函数结束 a的取值完毕
终止循环

'''