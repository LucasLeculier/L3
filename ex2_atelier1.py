# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 13:50:50 2022

@author: lluca
"""

def est_bissextile(année):
    return (année%4==0 and année%100 !=0) or année%400==0

def test():
    année = int(input("entrée l'année à vérifier"))
    return est_bissextile(année)