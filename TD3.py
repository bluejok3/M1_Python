#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Exercice 1 | question 1
def exo1_1():
    utilisateur = int(input("Entrer un nombre à multiplier : "))
    for x in range(1,6):
        print(utilisateur*x)

# Exercice 1 | question 2
def exo1_2():
    user = int(input("Entrer un nombre à multiplier : "))
    for x in range(1, 11):
        print(utilisateur*x, end=" ")


# Exercice 1 | question 3
def exo1_3():
    user = int(input("Entrer un nombre à trouver sa table : "))
    for x in range(utilisateur):
        print("Table de", int(x) + 1, ":")
        for i in range(1, 11):
            print((x+1)*i,)

# Exercice 1 | question 4
def exo1_4():
    user = int(input("Entrer un nombre à afficher en asterisk : "))
    for x in range(utilisateur):
        print("*" * (x+1))

# Exercice 1 | question 5
def exo1_5():
    user = int(input("Entrer un nombre à afficher en asterisk : "))
    for x in range(utilisateur):
        print(" " * ((user-1)-x) + ("* " * (x+1)))


# In[2]:


# Exercice 2 | question 1
def exo2_1():
    jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mois = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    mj = []
    longueur = len(jours) - len(mois)
    if longueur == 0:
        for x in range(len(jours)):
            mj.append((mois[x], jours[x]))
    else:
        print("can't do it")
    return mj

mj = exo2_1() # Le laisser sinon l'exo exo2 question 2() n'a pas la variable mj
# print(mj) si on veut display mj

# Exercice 2 | question 2
def exo2_2():
    annee = []
    for month in mj:
        for x in range(month[1]):
            annee.append((str(x+1)) + " " + month[0])
    return annee

annee = exo2_2() # Le laisser sinon exo2_3() n'a pas la variable annee
# print(annee) si on veut display annee

# Exercice 2 | question 3
def exo2_3():
    annee2 = []
    jours_semaine = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for jour in range(365):
        annee2.append(jours_semaine[jour%len(jours_semaine)] + " " + annee[jour])
    return annee2

annee2 = exo2_3()

#print(annee2) # si on veut display annee2

# Exercice 2 | questions 4 et 5
def exo2_4_5():
    dico = {}
    jours_semaine = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for jour in range(365):
        dico[annee[jour]] = jours_semaine[jour%len(jours_semaine)]
    print(dico)
    print(dico["28 October"])
# exo2_4_5()


# In[3]:


#exercice 3 question 1
def exo3_1():
    liste_notes = []
    while len(liste_notes) < 3:
        user = int(input("Entrer une note : "))
        liste_notes.append(user)

    minimum = min(liste_notes)
    maximum = max(liste_notes)
    somme = 0

    for notes in liste_notes:
        somme += int(notes)
    moyenne = float(somme)/len(liste_notes)

    print("moyenne " + str(moyenne), "minimum " + str(minimum), "maximum " + str(maximum))

# Exercice 3 | question 2
def exo3_2():
    utili = int(input("Entrer le nombre de notes que vous voulez entrer ? "))
    liste_notes = []
    while len(liste_notes) < utili:
        user = int(input("Entrer une note : "))
        liste_notes.append(user)
    mini = min(liste_notes)
    maxi = max(liste_notes)
    som = 0

    for notes in liste_notes:
        som += int(notes)
    moy = float(som) / len(liste_notes)

    print("moyenne " + str(moy), "minimum " + str(mini), "maximum " + str(maxi))

#exercice 3 question 3

def exo3_3():
    liste_notes = []
    while True:
        user = input("Entrer une note : (fin pour finir) ")
        if user == "fin":
                break
        else:
            liste_notes.append(float(user))
            mini = min(liste_notes)
            maxi = max(liste_notes)
            som = 0
            for notes in liste_notes:
                som += int(notes)
            moy = float(som) / len(liste_notes)

    print("moyenne " + str(moy), "minimum " + str(mini), "maximum " + str(maxi))


# In[4]:


#Exercice 4
from random import *
def exo4():
    alea21 = randint(1,100)
    correct = False
    while not correct:
        user = int(input("Devine le nombre entre 1 et 100 "))
        if alea21 > user:
            print("Trop Petit !")
        elif alea21 < user:
            print("trop Grand !")
        elif alea21 == user:
            break

    if alea21 == user:
        rejoue = input ("bien joué mek, on rejoue ? (y or n) ")
        if rejoue == 'y':
            exo4()


# In[ ]:





# In[ ]:




