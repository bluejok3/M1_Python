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


# In[ ]:




