#!usr/bin/env python
#coding:utf-8
stack = []
# CMDs = {'u': 'pushIn', 'p': 'popOut', 'v': "viewStack", 'q': 'Quit'}

pr = '''
pUsh
pOpo
View
Quit

please enter the key(use one picture):
'''
def pushIn():
	stack.append(raw_input('enter the string you want to push:').strip())#默认去除前后空格字符
	print stack


def popOut():
	if len(stack) == 0:
		print("ERROR!stack is empty,you can not pop it !")
	else:
		print ('removed %s' % stack[-1])#最后一个先出 堆起来的东西
		stack.pop()


def viewStack():
	print stack

CMDs = {'u': pushIn, 'o': popOut, 'v': viewStack}
def showImfor():
	while True:
		p = raw_input(pr).lower()
		if p != 'u' or 'q' or 'o' or 'v':
			if p == 'q':
				print "you choice Quit"
				break
			else:
				CMDs[p]()
		else:
			print "ERRPR INPUT!"


if __name__ == '__main__':
	showImfor()
