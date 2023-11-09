from  sympy import *

def operat(s):
    (a, b, op) = (s[2:].split('&'))
    a = a.split('=')[1]
    b = b.split('=')[1]
    op = op.split('=')[1]

    j=a.count(']')-1#2
    i=a.count(',')-j+1#2
    m1=[[] * j] * i
    a=a.replace('[','')
    a=','+ a.replace(']','')+','
    #ОСНОВНОЙ ЦИКЛ ПРЕОБРАЗОВАНИЯ
    k=1
    for z in range(0, i):
        for w in range(0, j):
            m1[z].append(int(a.split(',')[k]))
            print(z,w)
            print(m1[z][w])
            k+=1

    print(m1)

    j=b.count(']')-1#2
    i=b.count(',')-j+1#2
    m2=[[] * j] * i
    b=b.replace('[','')
    b=','+ b.replace(']','')+','
    #ОСНОВНОЙ ЦИКЛ ПРЕОБРАЗОВАНИЯ
    k=1
    for z in range(0, i):
        for w in range(0, j):
            m2[z].append(int(b.split(',')[k]))
            print(z,w)
            print(m2[z][w])
            k+=1

    print(m2)
    M1=Matrix(m1)
    M2=Matrix(m2)
    op=op[1:4]
    print(str(op))

    if(op =="Sum"):
        print(M1+M2)

