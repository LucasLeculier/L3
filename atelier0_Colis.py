# -*- coding: utf-8 -*-

#Liste des possibilités en fonction du type de lettre
VERTE = {20 : 1.16,
         100 : 2.32,
         250 : 4,
         500 : 6,
         1000 : 7.5,
         3000 : 10.5,
         0 : 0.5}

PRIORITAIRE = {20 : 1.43,
               100 : 2.86,
               250 : 5.26,
               500 : 7.89,
               3000 : 11.44,
               0 : 0.5}

ECOPLI = {20 : 1.14,
          100 : 2.28,
          250 : 3.92,
          0 : 0.5}

OUTRE_MER = {500 : 8.35,
             1000 : 11.2,
             2000 : 14.1,
             5000 : 23.65,
             10000 : 37.5,
             15000 : 75.85,
             30000 : 87.4}
# Poid max pour chaque type de lettre
POID_MAX = {"verte" : 3000,
            "prioritaire" : 3000,
            "ecopli" : 250,
            "outre-mer" : 30000}

TYPES_LETTRES = ["verte","prioritaire","ecopli","colissimo outre-mer","cécogramme"]

OM1 = ['guyanne','guadeloupe','martinique,la reunion; st pierre et miquelon', 'st barthelemy', 'st-martin,mayotte']


OM2 = ['nouvelle-caledonie','polynesie francasie', 'wallis-et-futuna']


# Liste des types de lettres









def saisie_type_lettre()-> str:
    # #Choix du type de lettre et vérification
        type_lettre = input("verte, prioritaire, ecopli, outre-mer ou cécogramme ? " )
        return type_lettre

        #Si cécogramme, le prix est toujours de 0
            # if type_lettre == 'cécogramme':
            #     print("les envoies par cécogramme sont gratuits")
            #     exit()
    # Choix du poid et vérification


def prix_complement(poid : int, zone : int)-> float:
    # On renvoie le prix du complément aérien en fonction de la zone 1 ou 2
    DIVISEUR = 10
    TARIF_OM1 = 0.05
    TARIF_OM2 = 0,11
    
    multiplicateur = 0
    if poid%DIVISEUR==0:
        multiplicateur = poid/DIVISEUR
    else:
        multiplicateur = poid//DIVISEUR + 1
    if zone==1:
        prix = TARIF_OM1 * multiplicateur
    else:
        prix = TARIF_OM2 * multiplicateur
    return prix



def saisie_poid() ->int:   
        #Récupération poid du colis/lettre
        poid = int(input("Entrez le poid du colis (0 pour un sticker suivi)"))
        return poid
       
def Calcul_prix_sans_complement(type_lettre : str, poid : int)-> float:
    #Récupération du prix en fonction du type de lettre et du poid correspondant ( sans complément aérien)
    while True :  
       if poid >= 0 and POID_MAX[type_lettre] >= poid :
            break
    if poid == 0 and (type_lettre == 'ecopli' or type_lettre == 'verte' or type_lettre == 'prioritaire'):
        print("les envoies par sticker sont au prix de 0,50€")
        exit()   
    #Récuperation du poid correspondant
    if type_lettre == 'ecopli':
        for i in ECOPLI.keys():
            resultat = i
            if poid<i : 
                prix = ECOPLI[resultat]
                break
    elif type_lettre == 'verte':
        for i in VERTE.keys():
            resultat = i
            if poid<i :
                prix = VERTE[resultat]
                break
    elif type_lettre == 'prioritaire':
        for i in PRIORITAIRE.keys():
            resultat = i
            if poid<i : 
                prix = PRIORITAIRE[resultat]
                break
    else:
        for i in OUTRE_MER.keys():
            resultat = i
            if poid<i : 
                prix = OUTRE_MER[resultat]
                break
    return prix


def prix_affranchissment()-> int:
    #Programme d'execution qui renvoie le prix final recherché
    type_lettre = ''
    boolean_complement = ''
    choix_region = 0
    prix_final = 0.0
    #verification du type de lettre
    while type_lettre not in TYPES_LETTRES :
        type_lettre = saisie_type_lettre()
    # fin du programme si le type est cécogramme
    if type_lettre == 'cécogramme': 
         print("les envoies par cécogrammes sont toujours gratuits")
         quit()
    poid = saisie_poid()
    #vérification demande zone outre-mer
    while boolean_complement != 'O' and boolean_complement !='N':
        boolean_complement = input("Votre envoie est-il destiné a un territoire hors france métropolitaine ? O/N")
    if boolean_complement =='O':
        #récupération de la zone
        while choix_region != 1 and choix_region != 2:
            print("Région numéro 1 : ",OM1)
            print("Région numéro 2 : ",OM2)
            choix_region = int(input("Quel est votre région :"))
        prix_final += prix_complement(poid,choix_region)
    prix_final += Calcul_prix_sans_complement(type_lettre, poid)    
    return prix_final
    

print(prix_affranchissment())
