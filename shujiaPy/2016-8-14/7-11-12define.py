#coding: utf-8

'''
7-11
什么组成字典中合法的键? 举例说明字典中合法的键和非法的键。
'''

# 合法的键 应该是可哈希的
# 所有的不可变量都是可哈希的 或者是函数但是其本质返回的是可哈希的
# 不合法的键 是不可哈希的
# 比如 变量 列表 字典等等


#
# 7-12
# (a)在数学上，什么是集合?
# 集合是一些不重复的 有穷的
# 集合是具有某种特定性质的事物的总体 ---百度
# (b)在 Python 中，关于集合类型的定义是什么？
# 集合是一种基本的数据类型 是一种无序不重复元素集
# 可以进行 各种操作

#定义一个集合
set1 = {'a', 'a', 'f', 'g', 'g', 'm'}
print set1
a = ['a', 'a', 'f', 'g', 'g', 'm', 'asa', 'rejriji']
#集合转化
b = set(a)

print '%s' % (b | set1) + '并'
print '%s' % (b & set1) + '交'
print '%s' % (b - set1) + '差'
b.add('python')
print '%s' % (b)
set1.update('python')
print '%s' % (set1) + '整个字符串拆分后 每个元素一个一个的添加'


#
# Connected to pydev debugger (build 143.1919)
# set(['a', 'm', 'g', 'f'])
# set(['a', 'm', 'g', 'f'])
#
# Process finished with exit code 0
# ------------------------------------------
# 记录一个错误
# print '%s' % (b.add(set1)) + 'set1整个作为一个整体传入' + '%s' % (b.add('python i like'))
# TypeError: unhashable type: 'set'  说明 add()参数必须是可哈希的 具体深层的原因有待发掘
#
# 而且 print '%s' % (b.add('python')) 返回的是 None 说明调用的函数没有返回值 其直接改变的set对象的内容
