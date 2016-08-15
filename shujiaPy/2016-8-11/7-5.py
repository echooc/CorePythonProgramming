#coding: utf-8
import time
'''
this is a big deal~
这次是长长的编程哦~
这个程序管理用于登录系统的用户信息
'''
db = {}
def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('password: ')
    db[name] = pwd

def olduser():
    prompt = 'user name: '
    prompt1 = 'password: '
    name = raw_input(prompt)
    password = raw_input(prompt1)
    while True:
        if db.has_key(name):
            if db[name] == password:
                print 'welcome back ', name
                a = time.time()
                print a
                break
            else:
                print 'wrong password, please try again'
                continue
        print 'no user named %s' %name + 'please register first!'
        continue

def showmenu():
    prompt = '''
    (N)ew User Login
    (E)xisting User Login
    (Q)uit
    Enter choice:
    '''
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
                print('\n you picked : %s') % choice
            if choice not in 'neq':
                print '\n invalid option, try again'
            else:
                chosen = True
                done = True

newuser()
olduser()

if __name__ == '__main__':
    showmenu()
