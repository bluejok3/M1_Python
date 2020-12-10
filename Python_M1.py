#TD1
#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 5
y = 10
z = 7
print ( x + y - z )


# In[3]:


a = "je suis"
b = "un beau"
c = "gosse"
print (a, b, c)


# In[5]:


print ( 10000 > 1)
print ( 1==1)
print (1 < 0)


# In[3]:


prenom = "Louis "
nom = "Tadej"
nom_complet = prenom + nom
print (nom_complet)
i= 0
while i <= 100:
    print('L T')
    i = i+1


# In[4]:


a = input ("salut bg c'est quoi ton prénom ? ")
b = int (input("tu m'as l'air jeune et dynamique, t'as quel age ? "))


# In[9]:


Celsius = int (input("Entrez la température Celsius: "))
Farhenheit= 9/5 * Celsius + 32
print ("Température: ", Celsius, "Farhenheit = ", Farhenheit, " F")
Farhenheit = int(input("Rentre la température en farhenheit: "))
Celsius = (Farhenheit-32)*5/9
print ("Temperature: ", Farhenheit, "Celsius =", Celsius, " C")


# In[10]:


A=input('Entrer une valeur de verite pour A: (entrer False ou True)')
B=input('Entrer une valeur de verite pour B: (entrer False ou True)')
C=input('Entrer une valeur de verite pour C: (entrer False ou True)')

expression_bol=input('Entrer une expression Bolenne avec des "non", "ou", "et", et des parentheses:')
expression_bol.replace('non', 'not')
expression_bol.replace('et', 'and')
expression_bol.replace('ou', 'or')
print (bool(expression_bol))


# In[ ]:





#TD2
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


# Exo 3 | 1-2
n = input("Entrer des mots separes par un espace : ")
user_list = n.split()
list_triee = sorted(user_list)
print(list_triee)


# In[17]:


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
    en_fr[valeur] = cle  # assigne cette cle avec cette valeur
print(en_fr)


# In[10]:


#exercice 7 question 5
if "brain" in (en_fr): # par défaut dans les clés pour values .values
    print("la traduction est ici")


# In[12]:


#exercice 7 question 6
for cle, values in en_fr.items():
    if en_fr[cle] == "cerveau":
        print("clé = " + cle, "valeur = " + values)


# In[13]:


#exercice 7 question 7 à 10
new = {
    "jardin": ["garden", "Garten"],
    "voiture": ["car", "Wagen"],
    "soleil": ["sun", "Sonne"],
    "cerveau": ["brain", "Gehirn"],
    "chemin" : ["path", "Pfad"]
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


#TD3
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

