#coding: utf-8

'''
    颠倒字典中的键和值
'''

dict2 = {'fdfd': 'dsd', 'ds': 'huhu', 'fd': 'dsds'}
dict1 ={}
print len(dict2)
h = 0
while (h<len(dict2)):
    for i in dict2.keys():
        v = dict2.values()
        dict1[v[h]] = i
        h += 1

print dict1
