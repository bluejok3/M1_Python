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


# In[21]:


# exercice 4 questions 1 à 3
Couleurs = ["Pique", "Trefle", "Carreau", "Coeur"]
valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dame", "roi", "as"]
deck = []
for C in Couleurs:
   for v in valeurs:
       card = str(v) + " " + str(C)
       deck.append(card)
#print(deck)

from random import shuffle
shuffle(deck)
print(deck)

joueur1 = []
joueur2 = []
joueur3 = []
joueur4 = []
for index in range(13):
    joueur1.append(deck[index])
    joueur2.append(deck[index + 1])
    joueur3.append(deck[index + 2])
    joueur4.append(deck[index + 3])

print(" J1 = " + str(joueur1))
print(" J2 = " + str(joueur2))
print(" J3 = " + str(joueur3))
print(" J4 = " + str(joueur4))


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


# In[5]:


#exercice 6 question 1
infoEleves = input("Entrer prenom, nom et matricule étudiant séparés par un espace : ")
list = infoEleves.split(" ")
lepie= tuple(list)
print(lepie)
main_list = []


# In[6]:


#exercice 6 question 2 et 3
while True:
    choix = input("Entrer prénom, nom et matricule étudiant séparés par un espace : (FIN pour finir) ")
    if choix == "FIN":
        break
    else:
        list = choix.split(" ")
        matricule = tuple(list)
        main_list.append(matricule)

for etudiant in main_list:
    print(etudiant[0])


# In[7]:


#exercice 7 questions 1 à 3
fr_en = {
    "jardin": "garden",
    "voiture": "car",
    "soleil": "sun",
    "cerveau": "brain"
    }
for cle, valeur in fr_en.items():
    if cle == "cerveau":
        print(valeur)
    else:
        pass


# In[8]:


#exercice 7 question 4
en_fr = {}
for cle, valeur in fr_en.items():
    en_fr[valeur] = cle  # assigne cette cle cette valeur
print(en_fr)


# In[10]:


#exercice 7 question 5
if "brain" in (en_fr): # par défaut dans les clés pour values .values
    print("la traduction est la")


# In[12]:


#exercice 7 question 6
for cle, values in en_fr.items():
    if en_fr[cle] == "cerveau":
        print("clé = " + cle, "valeur = " + values)


# In[13]:


#exercice 7 question 7 à 10
new = {
    "jardin": ["garden", "gardenne"],
    "voiture": ["car", "carre"],
    "soleil": ["sun", "sunne"],
    "cerveau": ["brain", "brainne"],
    "chemin" : ["path", "way"]
    }

for cle, values in new.items():
    if cle == "chemin":
        print ("la deuxième traducion du mot chemin est : " + values[1])

del new["chemin"]
print(new)


# In[17]:


#exercice 8 questions 1 et 2
etudiant = {}

while True:
     choix = input("Entrer le prénom, nom et matricule étudiant séparés par un espace : (FIN pour finir) ")
     if choix == "FIN":
         break
     else:
         list = choix.split(" ")
         lepie = tuple(list)
         count = 0
         for cle in etudiant.keys():
             if lepie[1] in cle:
                 count += 1
         if count > 0:
             new_key = montuple[1] + str(count)
             etudiant[new_key] = lepie
         else:
             etudiant[lepie[1]] = lepie

print(etudiant)


# In[18]:


#exercice 8 question 3
for keys in etudiant.keys():
    print("Nom étudiant : " + keys)


# In[19]:


#exercice 8 question 4
if "Obama" in (etudiant):
    print(etudiant["Obama"])


# In[20]:


#exercice 8 question 5

for cle, values in etudiant.items():
    if values[2] == "12345678":
        print("cle " + str(cle), "valeur " + str(values))


# In[ ]:




