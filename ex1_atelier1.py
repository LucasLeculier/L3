# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 13:37:31 2022

@author: lluca
"""

def message_imc(indice):
    if indice < 16.5:
        return "dénutrition ou famine"
    elif indice <= 18.5:
        return "maigreur"
    elif indice <= 25:
        return "corpulence normale"
    elif indice <= 30:
        return "surpoid"
    elif indice <= 35:
        return "obsésité modérée"
    elif indice <= 40:
        return "obésité sévère"
    else : return "obésité morbide"
        
def test():
    indice = int(input("entrer votre IMC : "))
    return "pour un imc de", indice,message_imc(indice)
print(test())