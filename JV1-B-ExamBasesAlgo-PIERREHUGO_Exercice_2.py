#PARTIE 2 - TIC TAC TOE

L1display = ["   ","   ","   "]
L2display = ["   ","   ","   "]
L3display = ["   ","   ","   "]

L1valeur = [0,0,0]
L2valeur = [0,0,0]
L3valeur = [0,0,0]

debut=False
findujeu=False

compteTours = 0

croixVal=1
rondVal=2

croix = " X "
rond = " O "

Joueur1 = 0
Joueur2 = 0

while (debut==False):    
    print("Joueur 1 choisi si il est 1/Rond(O) 2/Croix(X)")    #Sélection du symbole par je Joueur 1
    choix = input()

    if choix=="1":
        Joueur1=rond
        Joueur2=croix
        debut=True
    elif choix=="2":
        Joueur1=croix
        Joueur2=rond
        debut=True
    else:
        print("CHOIX INCORRECT")

print (L1display)
print (L2display)
print (L3display)

while (findujeu==False):
    for i in range (0,8):
        compteTours+=1
        print("C'est le ", compteTours, "tour, Joueur 1 choisis une ligne")  #Choix du Joueur 1
        choixLigne = input()
        if choixLigne== "1":                                                 # vérification de ce que le joueur fait
            print("Choisis une colonne:")
            choixColonne = input()
            if choixColonne== "1":                                           #choix de colonne
                if L1valeur[1]==0:                                           #vérifie que la colonne est vide
                    if Joueur1 == rond:
                        L1valeur[0] = rondVal                                #remplace dans les tabelaux par le symbole.
                        L1display[0] = rond
                    else:
                        L1valeur[0] = croixVal
                        L1display[0] = croix
                else:
                    print("Case déja occupée")
        
            if choixColonne== "2":
                if L1valeur[1]==0:
                    if Joueur1 == rond:
                        L1valeur[1] = rondVal
                        L1display[1] = rond
                    else:
                        L1valeur[1] = croixVal
                        L1display[1] = croix
                else:
                    print("Case déja occupée")
        
            if choixColonne== "3":
                if L1valeur[2]==0:
                    if Joueur1 == rond:
                        L1valeur[2] = rondVal
                        L1display[2] = rond
                    else:
                        L1valeur[2] = croixVal
                        L1display[2] = croix
                else:
                    print("Case déja occupée")
        
        if choixLigne== "2":
            print("Choisis une colonne:")
            choixColonne = input()
            if choixColonne== "1":
                if L2valeur[0]==0:
                    if Joueur1 == rond:
                        L2valeur[0] = rondVal
                        L2display[0] = rond
                    else:
                        L2valeur[0] = croixVal
                        L2display[0] = croix
                else:
                    print("Case déja occupée")
        
            if choixColonne== "2":
                if L2valeur[1]==0:
                    if Joueur1 == rond:
                        L2valeur[1] = rondVal
                        L2display[1] = rond
                    else:
                        L2valeur[1] = croixVal
                        L2display[1] = croix
                else:
                    print("Case déja occupée")
        
            if choixColonne== "3":
                if L2valeur[2]==0:
                    if Joueur1 == rond:
                        L2valeur[2] = rondVal
                        L2display[2] = rond
                    else:
                        L2valeur[2] = croixVal
                        L2display[2] = croix
                else:
                    print("Case déja occupée")
        
        if choixLigne== "3":
            print("Choisis une colonne:")
            choixColonne = input()
            if choixColonne== "1":
                if L3valeur[0]==0:
                    if Joueur1 == rond:
                        L3valeur[0] = rondVal
                        L3display[0] = rond
                    else:
                        L3valeur[0] = croixVal
                        L3display[0] = croix
                else:
                    print("Case déja occupée")
        
            if choixColonne== "2":
                if L3valeur[1]==0:
                    if Joueur1 == rond:
                        L3valeur[1] = rondVal
                        L3display[1] = rond
                    else:
                        L3valeur[1] = croixVal
                        L3display[1] = croix
                else:
                    print("Case déja occupée")
        
            if choixColonne== "3":
                if L3valeur[2]==0:
                    if Joueur1 == rond:
                        L3valeur[2] = rondVal
                        L3display[2] = rond
                    else:
                        L3valeur[2] = croixVal
                        L3display[2] = croix
                else:
                    print("Case déja occupée")
        
        if L1valeur[0]==L2valeur[1]==L3valeur[2] or L1valeur[0]==L2valeur[0]==L3valeur[0] or L1valeur[0]==L1valeur[1]==L1valeur[2] or L1valeur[2]==L2valeur[2]==L3valeur[2] or  L1valeur[1]==L2valeur[1]==L3valeur[1] or L2valeur[0]==L2valeur[1]==L2valeur[2] or L3valeur[0]==L3valeur[1]==L3valeur[2] or L3valeur[0]==L2valeur[1]==L1valeur[2]:  #Devrait vérifier les condition de victoire et briser le while, mais ne fonctionne pas
            findujeu=True
            
        input()
        print("Joueur 2 choisis une ligne")      #Vérification des emplacements et affichage pour le Joueur 2
        choixLigne = input()
        if choixLigne== "1":
            print("Choisis une colonne:")
            choixColonne = input()
            if choixColonne== "1":
                if L1valeur[0]==0:
                    if Joueur2 == rond:
                        L1valeur[0] = rondVal
                        L1display[0] = rond
                    else:
                        L1valeur[0] = croixVal
                        L1display[0] = croix
                else:
                    print("Case déja occupée")
            if choixColonne== "2":
                if L1valeur[1]==0:
                    if Joueur2 == rond:
                        L1valeur[1] = rondVal
                        L1display[1] = rond
                    else:
                        L1valeur[1] = croixVal
                        L1display[1] = croix
                else:
                    print("Case déja occupée")
            if choixColonne== "3":
                if L1valeur[2]==0:
                    if Joueur2 == rond:
                        L1valeur[2] = rondVal
                        L1display[2] = rond
                    else:
                        L1valeur[2] = croixVal
                        L1display[2] = croix
                else:
                    print("Case déja occupée")
        if choixLigne== "2":
            print("Choisis une colonne:")
            choixColonne = input()
            if choixColonne== "1":
                if L2valeur[0]==0:
                    if Joueur2 == rond:
                        L2valeur[0] = rondVal
                        L2display[0] = rond
                    else:
                        L2valeur[0] = croixVal
                        L2display[0] = croix
                else:
                    print("Case déja occupée")
        
            if choixColonne== "2":
                if L2valeur[1]==0:
                    if Joueur2 == rond:
                        L2valeur[1] = rondVal
                        L2display[1] = rond
                    else:
                        L2valeur[1] = croixVal
                        L2display[1] = croix
                else:
                    print("Case déja occupée")
            if choixColonne== "3":
                if L2valeur[2]==0:
                    if Joueur2 == rond:
                        L2valeur[2] = rondVal
                        L2display[2] = rond
                    else:
                        L2valeur[2] = croixVal
                        L2display[2] = croix
                else:
                    print("Case déja occupée")
        if choixLigne== "3":
            print("Choisis une colonne:")
            choixColonne = input()
            if choixColonne== "1":
                if L3valeur[0]==0:
                    if Joueur2 == rond:
                        L3valeur[0] = rondVal
                        L3display[0] = rond
                    else:
                        L3valeur[0] = croixVal
                        L3display[0] = croix
                else:
                    print("Case déja occupée")
            if choixColonne== "2":
                if L3valeur[1]==0:
                    if Joueur2 == rond:
                        L3valeur[1] = rondVal
                        L3display[1] = rond
                    else:
                        L3valeur[1] = croixVal
                        L3display[1] = croix
                else:
                    print("Case déja occupée")
            if choixColonne== "3":
                if L3valeur[2]==0:
                    if Joueur2 == rond:
                        L3valeur[2] = rondVal
                        L3display[2] = rond
                    else:
                        L3valeur[2] = croixVal
                        L3display[2] = croix
                else:
                    print("Case déja occupée")
        print(L1display)
        print(L2display)
        print(L3display)
        input()
        if L1valeur[0]==L2valeur[1]==L3valeur[2] or L1valeur[0]==L2valeur[0]==L3valeur[0] or L1valeur[0]==L1valeur[1]==L1valeur[2] or L1valeur[2]==L2valeur[2]==L3valeur[2] or  L1valeur[1]==L2valeur[1]==L3valeur[1] or L2valeur[0]==L2valeur[1]==L2valeur[2] or L3valeur[0]==L3valeur[1]==L3valeur[2] or L3valeur[0]==L2valeur[1]==L1valeur[2]:
            findujeu=True

    print("Match Nul")

print("PARTIE TERMINEE")
print(L1display)
print(L2display)
print(L3display)


#Pour faire un puissance 4 à partir de ce code, il suffirait de rajouter, une L4valeur ainsi qu'une L4display, en augmentant la taille des tableaux de 1, rajouter une vérification de ligne supplémentaire et une vérification de colonne supplémentaire dans chacune d'entre elles.
