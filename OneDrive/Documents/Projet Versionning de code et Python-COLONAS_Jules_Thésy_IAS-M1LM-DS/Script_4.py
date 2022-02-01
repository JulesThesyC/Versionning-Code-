#!/usr/bin/env python
# coding: utf-8

# ### Script 4

# #### 2. Création de fonction comportant des modules de gestions des exceptions

# In[ ]:


#### Gestion des exceptions pours les cas suivants:

#### Saisie d'une str dans les arguments de la fonction
#### Sasie un nombre complexe
#### Saisie d'un nombre négatif
#### Saisie d'un très grand nombre
#### Saisie d'un très petit nombre


# In[ ]:





# In[1]:


def pythagore(a, b):#### Création de la fonction Pytagore
  ##### Retourner hypothénuse d'un triangle rectangle
  c = (a**2 + b**2)**(1/2)
  return c


# In[ ]:





# In[2]:


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





# In[4]:


### Paramètres:
    ### a : un entier
    ### b : un entier

### Sortie:
    ### c : l'hypoténuse égale à sqrt(a**2 + b**2)


# In[ ]:





# In[5]:


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




