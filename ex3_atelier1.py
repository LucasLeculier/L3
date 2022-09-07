# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 13:57:07 2022

@author: lluca
"""
from math import *

def discriminant(a,b,c):
    return b*b - 4*a*c

def racine_unique(a,b):
    return -b/2*a
    
def racine_double(a,b,delta,num):
    if num == 1:
        return (-b + sqrt(delta))/2*a
    elif num== 2:
        return (-b -sqrt(delta))/2*a
    
def str_equation(a,b,c):
    final = ''
    if a == -1 :final += '-x2'
    elif a == 1: final += 'x2'
    else : final += str(a)+'x2'

    
    if b == -1 : final += ' -x'
    elif b<0 : final += str(b)+'x'
    elif b == 1 : ' + x'
    else : final += ' + '+str(b)+'x'
    
    
    if c<0 : final += str(c) 
    else : final += ' + '+str(c)
    return final

def equation(a,b,c):
    delta = discriminant(a,b,c)
    if delta>0:
        racine1 = racine_double(a, b, delta, 1)
        racine2 = racine_double(a, b, delta, 2)
        return "les solutions de l'équation ",str_equation(a, b, c)," sont :",racine1,racine2
    elif delta == 0:
        racine= racine_unique(a, b)
        return "la solution de l'équation ",str_equation(a, b, c)," est :",racine
    else:
        return "l'équation ", str_equation(a, b, c)," n'a pas de solution"
    
    
def test():
    return(equation(2, 0.5, 2))
    # return(equation(2, 4, 2))
    # return(equation(-2, 3, 2))
print(test())
