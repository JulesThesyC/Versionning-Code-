#!/usr/bin/env python
# coding: utf-8

# # Mastère 1 
# ### EXAMEN Versionning de code et Programmation Python:
# ### Implémentation de fonction mathématiques et intégration à Github

# #### Présentation du Projet 

# ##### 1. Création de fonction mathématique simple en Python:

# ###### a) Implémentons la foncton polynomiale ci-dessous:

# ### f(x) = x^3 - 1,5x^2 - 6x + 5

# In[26]:


import numpy as np
import numpy.polynomial.polynomial as nppol


# In[36]:


Polynome=nppol.polyval(x, [5, -6, -1.5, 1])
x = 5
Polynome


# In[ ]:





# In[ ]:





# #### b) Implémentons la fonction factorielle

# In[21]:


def factorielle(n):
   if n == 0:
      return 1
   else:
      F = 1
      for k in range(2,n+1):
         F = F * k

      return F


# In[22]:


factorielle(5)


# In[ ]:





# #### c) Implémentons la suite de Fibonacci.

# In[19]:


nterms = int(input("Entrez un nombre: "))
 
n1 = 0
n2 = 1
 
print("\n la suite fibonacci est :")
print(n1, ",", n2, end=", ")
 
for i in range(2, nterms):
  suivant = n1 + n2
  print(suivant, end=", ")
 
  n1 = n2
  n2 = suivant


# In[ ]:





# #### 2. Création de fonction comportant des modules de gestions des exceptions

# In[ ]:


#### Gestion des exceptions pours les cas suivants:

#### Saisie d'une str dans les arguments de la fonction
#### Sasie un nombre complexe
#### Saisie d'un nombre négatif
#### Saisie d'un très grand nombre
#### Saisie d'un très petit nombre


# In[37]:


def pythagore(a, b):#### Création de la fonction Pytagore
  ##### Retourner hypothénuse d'un triangle rectangle
  c = (a**2 + b**2)**(1/2)
  return c


# In[38]:


# Erreur pour la saisie d'une chaîne de caractères
class StringArgument(Exception):
    def __arg__(self, m):
        self.message = m
    def __str__(self):
        return self.message

# Erreur pour la saisie d'un nombre complexe
class ComplexArgument(Exception):
    def __arg__(self, m):
        self.message = m
    def __str__(self):
        return self.message

# Erreur pour la saisie d'un nombre négatif
class NegativeArgument(Exception):
    def __arg__(self, m):
        self.message = m
    def __str__(self):
        return self.message
    
# Erreur pour la saisie d'un nombre trop grand
class BigArgument(Exception):
    def __arg__(self, m):
        self.message = m
    def __str__(self):
        return self.message

# Erreur pour la saisie d'un nombre trop petit
class SmallArgument(Exception):
    def __arg__(self, m):
        self.message = m
    def __str__(self):
        return self.message


# In[ ]:





# In[ ]:





# In[69]:


### Paramètres:
    ### a : un entier
    ### b : un entier

### Sortie:
    ### c : l'hypoténuse égale à sqrt(a**2 + b**2)


# In[ ]:





# In[82]:


def pythagore(a, b):    
     ### Chaîne de caractères:
 if (type(a)==str) or (type(b)==str):
    print("Impossible d'utiliser une chaîne dans la fonction")
    print("Veuillez saisir un valeur numérique:")
    if(type(a) == str) & (type(b) == int):
      a = int(input()) #### Saisie d'une nouvelle valeur pour a
    elif (type(b) == str) & (type(a) == int):
      b = int(input()) #### Saisie d'une nouvelle valeur pour b
    else:
      a = int(input()) #### Saisie d'une nouvelle valeur pour a
      b = int(input()) #### Saisie d'une nouvelle valeur pour b
    
    ### Nombre complexe
 elif (type(a) == complex) or (type(b) ==complex): #### Si l'une des deux valeurs saisie est ComplexArgument
    ComplexArgument(a,b)
    print(ComplexArgument(a,b)[0])
    print(ComplexArgument(a,b)[1])
    a = ComplexArgument(a,b)[0] #### Partie réelle du premier nombre complexe
    b = ComplexArgument(a,b)[1] #### Partie réelle du second nombre complexe
    
    ### Entier Négatif
 elif (type(a) in [int, float]) and (type(b) in [int, float]):
    #neg(a, b) #### Résultat de l'opération
    a = neg(a,b)[0] #### Varaible a (valeur absolue)
    b = neg(a,b)[1] #### Variable b (valeur absolue)
    # print(a)
    # print(b)
    # print(neg(a, b))
    
    ### Longueur de la variable
 elif (len(str(b)) > 16) or (len(str(a)) > 16): #### Si la longeur de l'une des deux variables est > à 16
    limit_digit(a, b)
    a = limit_digit(a, b)[0] #### J'affiche a
    b = limit_digit(a, b)[1] ### J'affiche b

 return calcul(a, b)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# #### 4. Déploiement des 4 scripts sur la plateforme Github

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




