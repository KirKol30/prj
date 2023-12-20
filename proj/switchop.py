from  sympy import *
def switch(M1, M2, op):
    M1.applyfunc( Symbol('{:.3f}'.format(x)))
    M2.applyfunc( Symbol('{:.3f}'.format(x)))
    if(op =="Sum"):

        print(M1+ M2)
    elif(op=="Mul"):
        print(M1*M2)
    elif(op=="Min"):
        print(M1-M2)
def clinner(s):
   s=s.replace('%20',' ')
   s=s.replace('%22', '"')


