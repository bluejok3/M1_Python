#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercice 1 | questions 1 et 2
c = "X44bf38j23jdjgfjh737nei47"
c_num = ""
c_alpha = ""
for caracters in c:
    if str.isdigit(caracters) == True:
        c_num += caracters
    else:
        c_alpha += caracters

print(c_num, c_alpha)


# In[2]:


# Exercice 1 | question 3
str_find = "j23"
c.find(str_find)
if c.find(str_find) != -1:
    new_c = c.replace(str_find, "j24")
    print(new_c)


# In[3]:


# Exercice 1 | question 4
list = ["f","3","7"]
for string in list:
    first = c.find(string)
    print(first)

print("\n")


# In[4]:


# Exercice 2 question 1 (a,b et c)
texte = "We introduce here the Python language"
compteur = 0
for lettre in texte:
    compteur += 1
if compteur == len(texte):
    print("good")
else:
    print("not good")

# Sans compter les espaces
compteur_lettre = 0
for lettre in texte:
    if lettre == " ":
        pass
    else:
        compteur_lettre += 1
print(compteur_lettre)

# Compter les mots dans la variable texte
mots = len(texte.split())
print(mots)


# In[5]:


# Exercice 2 question 2

# Cela est toujours viable puisque le module split est utilisé

texte2 = "We introduce here the Python language. To learn more about the language, consider going through the excellent tutorial https://docs.python.org/ tutorial. Dedicated books are also available, such as http://www.diveintopython.net/."
mots = len(texte2.split())
print(mots)


# In[6]:


# Exercice 3 questions 1 et 2
n = input("Entrer des mots separes par un espace : ")
user_list = n.split()
list_triee = sorted(user_list)
print(list_triee)


# In[17]:


# exercice 4 questions 1 à 3
couleurs=["Pique","Trèfle","Carreau","Coeur"]
valeurs =["2","3","4","5","6","7","8","9","10","valet","dame","roi","as"]
for x in couleurs :
   for y in valeurs:
      print (x+" "+y)

from random import shuffle


# In[29]:


# exercice 5 question 1 et 2
with open("diamonds.csv", "r") as f:
    diamants=f.readlines()
diamants[10].split(",")


# In[31]:


#exercice 5 question 3
with open("diamonds.csv", "r")as f:
    diamants_100=f.readlines()
diamants_100[:20]


# In[47]:


#exercice 5 question 4
with open("diamonds.csv", "r")as f:
    diamants_prix=f.readlines(100000)
    num_columns = len(5) 
    diamonds.csv(5)
diamants_prix[:20]


# In[53]:


#exercice 6 question 1, 2 et 3
prenom= input ('renseignez votre prénom')
nom= input ('renseignez votre nom')
matricule= input ('renseignez votre matricule')
informationEleve = (prenom, nom, matricule)

while matricule != FIN:

#retourne les prénoms, noms et matricules des élèves
def retourne_liste_etudiant():
    return "prenom", "nom", "matricule"


# In[ ]:




