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




