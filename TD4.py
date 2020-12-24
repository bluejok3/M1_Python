#!/usr/bin/env python
# coding: utf-8

# In[10]:





# In[ ]:





# In[21]:


#Exercice 1 question 1

from math import pi; 

def surf_cercle(r):   #variable r pour le rayon
    return pi(r**2)
r = input("saissisez R :")
surf_cercle(r)


# In[12]:


#Exercice 1 question 2

def surf_cercle2(r=1):
    return pi(r2)


# In[14]:


#exercice 1 question 3
def vol_boite(L,l,h): #h=hauteur, L=Longueur et l=largueur
        h=float(input("entrer la hauteur de votre boite :"))
        L=float(input("entrer la Longueur de votre boite :"))
        l=float(input("entrer la largueur de votre boite :"))
    return Llh


# In[15]:


#exercice 1 question 4
def vol_boite2(x=None,y=None,z=None): #définition des arguments x,y,z et qui par défaut n'ont pas de valeur (soit 'None')
    if y==None and z==None: #si y et z n'ont pas de valeur (None)
        return x3
    elif z==None: #si z n'a pas de valeur (None)
        return (x*2)y
    else:
        return xyz


# In[16]:


def remplacement(c1,c2,ch):
    return ch.replace(c1,c2)


# In[17]:


def remplacement2(c1=" ",c2="",ch=""):
    return ch.replace(c1,c2)


# In[18]:


#exercice 2
def nb_car(chaine):
    nb_car=0
    for car in chaine:
        if car == " ":
            pass
        else:
            nb_car+=1
    return nb_car

def nb_mots(chaine):
    nb_mots=len(chaine.split())
    return nb_mots


# In[19]:


#exercice 3 question 1
def TableMult(n,debut=1,fin=10):
    for x in range(debut,fin+1):
        print((nx),end=" ")


# In[ ]:


#exerice 3 question 2
def TableMult2(n,debut=1,fin=10):
    if debut>fin :
        for x in range(debut,fin,-1):
            print((nx),end=" ")
    else:
        for x in range(debut,fin+1):
            print((nx),end=" ")


# In[ ]:


#exercice 3 question 3


# In[ ]:


#exercice 4
def motus():
    from random import randint
    mots = ["arbre", "grave", "piece", "nuage", "crane", "sonne", "table", "herbe", "ecrou", "mulet"]
    number = randint(0, len(mots) - 1)
    random_word = mots[number]
    word = []
    word[:0] = random_word
    user = []
    for x in range(len(word)):
        user.append("-")
    print(" ".join(user))
    compteur = 0

    while True:
        compteur += 1
        if compteur == 11:
            break
        else:
            print("Essai numéro : " + str(compteur))
            ask = input("Entrez une lettre : ")
            for i in range(len(word)):
                if ask == word[i]:
                    user[i] = word[i]
                    if user == word:
                        print(" ".join(user))
                        win = input("Bravo! Envie de rejouer ? y/n ")
                        if win == "y":
                            motus()
                        else:
                            exit()
                else:
                    pass
            print(" ".join(user))

    rejoue = input("Perdu... Voulez-vous rejouer y/n : ")
    if rejoue == "y":
        motus()
motus()


# In[ ]:




