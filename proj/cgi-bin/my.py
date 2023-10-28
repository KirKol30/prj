#!/usr/bin/env python3
from sympy import *
def switch(operator, m1, m2):
    if operator == "Sum":
        return m1+m2
    elif operator == "multiplication":
        return m1*m2
#основное тело
import cgi
out_form = cgi.FieldStorage()
#тельцо
ferst_number = out_form.getfirst("ferstt","не задано")
second_number = out_form.getfirst("secondd","не задано")
operator= out_form.getfirst("tipe_ofoper","не задано")
#операции с symPy

M1=Matrix(ferst_number)
M2=Matrix(second_number)



print("Content-type: text/html")
print()
print(ferst_number)
print(switch(operator, M1, M2))