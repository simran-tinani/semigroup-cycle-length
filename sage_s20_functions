def cycle_length(x):
    N=1
    match=False
    while match is False:
        N=2*N
        q=ceil(sqrt(N))
        L=0
        xx=[]
        y=[]
        for i in range(0,q):
            xx.append(exp2(x,N+i))
            if i>0 and xx[i] == xx[0]:
                L=i
                match=True
                return L
        for j in range(0,q):
            y.append(exp2(x,(N+j*q)))
            for i in range(1,q):
                if y[j] == xx[i]:
                    L=j*q-i
                    match=True
                    return L
    return "fail"
    
def cycle_start(x, L):
    s=1
    b=1
    while exp2(x,s+L)!=exp2(x,s):
        s=2*s
        b=s/2
    while abs(b-s)>1:
        print "h"
        c = (b+s)/2
        if exp2(x,c+L)!=exp2(x,c):
            b=c
        else:
            s=c
    return s
    
def matrix_cycle_length(x):
    N=1
    match=False
    while match is False:
        N=2*N
        q=ceil(sqrt(N))
        L=0
        xx=[]
        y=[]
        for i in range(0,q):
            xx.append(x.__exp__(N+i))
            if i>0 and xx[i].__eq__(xx[0]):
                L=i
                match=True
                return L
        for j in range(0,q):
            y.append(x.__exp__(N+j*q))
            for i in range(1,q):
                if y[j].__eq__(xx[i]):
                    L=j*q-i
                    match=True
                    return L
    return "fail"
    
def matrix_cycle_start(x, L):
    s=1
    b=1
    while not x.__exp__(s+L).__eq__(x.__exp__(s)):
        s=2*s
        b=s/2
    while abs(b-s)>1:
        c = (b+s)/2
        if not x.__exp__(c+L).__eq__(x.__exp__(c)):
            b=c
        else:
            s=c
    return s
