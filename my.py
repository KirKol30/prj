from  sympy import *
import numpy as np
from switchop import *
s='/?A=[[123, 65], [77, 90]]&B=[[123, 144], [22, 91]]&op="Min"'


def operat(s):
    try:
        s = s.replace('%20', ' ')
        s = s.replace('%22', '"')
        print(s)
        (a, b, op) = (s[2:].split('&'))
        a = a.split('=')[1]#первая матрица
        b = b.split('=')[1]#вторая матрица
        op = op.split('=')[1]#операция
    #привожу матрицы к виду без скобок, для удобства чтения, но сперва считываю размерности матрицы
        i = a.count(']') - 1
        j = int((a.count(',') - i + 1) / i) + 1
        m1 = np.empty((i, j))
        a = a.replace('[', '')
        a = ',' + a.replace(']', '') + ','
        #ОСНОВНОЙ ЦИКЛ ПРЕОБРАЗОВАНИЯ
        k=1
        try:
            for z in range(0, i):
                for w in range(0, j):
                    m1[z][w]=int(a.split(',')[k])
                    m1[z][w]=int(m1[z][w])
                    k+=1
        except:
            print(k +"in first")
        i = b.count(']') - 1
        j = int((b.count(',') - i + 1) / i) + 1
        m2 = np.empty((i, j))
        b=b.replace('[','')
        b=','+ b.replace(']','')+','
        #ОСНОВНОЙ ЦИКЛ ПРЕОБРАЗОВАНИЯ
        k=1
        for z in range(0, i):
            for w in range(0, j):
                print()
                m2[z][w]=int(b.split(',')[k])
                k+=1
        M1=Matrix(m1)
        M2=Matrix(m2)
        op=op[1:4]
        print(str(op))
        try:
            switch(M1, M2, op)
        except:
            print("Error")

    except:
        print("Stop")
operat(s)


