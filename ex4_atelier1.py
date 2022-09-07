# -*- coding: utf-8 -*-
from datetime import date
"""
Created on Tue Sep  6 14:34:40 2022

@author: lluca
"""
jours_par_mois_31 = ['1','3','5','7','8','octobre','12']
jours_par_mois_30 = ['4','6','9','11']


def est_bissextile(année):
    return (année%4==0 and année%100 !=0) or année%400==0


def date_est_valide(jour,mois,annee):
    if annee>0 and mois>0 and jour >0 and mois<13 and jour <32 :
        if mois == 2:
            #cas fevrier bissextile
            if est_bissextile(annee):
                if jour < 30 : return True
                else : return False
            #cas fevrier non bissextile
            elif jour<29 : return True
            else:return False
            #Cas mois qui compte 30 jours
        if mois in jours_par_mois_30:
            if jour<31: return True
            else : return False
        return True
    return False

def saisie_date_naissance():
    jour = int(input('entrez le jour : '))
    mois = int(input('entrez le mois : '))
    année = int(input('entrez l"année : '))
    return date(année,mois,jour)

def age(anniversaire):
    #décomposition des jours,mois,année
    adj = date.today()
    a1 = adj.year
    m1 = adj.month
    j1 = adj.day
    a2 = anniversaire.year
    m2 = anniversaire.month
    j2 = anniversaire.day
    
    #calcul de l'age
    if m1<m2: return a1-a2
    elif m1==m2 : 
        if j1<j2 : return a1-a2
    return a1-a2-1

def est_majeur(date_naissance):
    return age(date_naissance)>=18

def test():
    while True:
        #Saisie date valide
        anniversaire = saisie_date_naissance()
        if date_est_valide(anniversaire.day, anniversaire.month, anniversaire.year):
            break
    if est_majeur(anniversaire):
        return "Accès autorisé"
    else: return "Vous avez "+ str(age(anniversaire))+" ans Accès refuser"
    
print(test())