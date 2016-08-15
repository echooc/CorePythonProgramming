from keyword import kwlist

def compare():
    a = raw_input('enter world : ')
    if a not in(kwlist):
        print 'not in'
    else:
        print 'in'
def paixu():
    a = [1,2,6,5,4,84,1,51,15,54]
    b = sorted(a)
    print b

paixu()