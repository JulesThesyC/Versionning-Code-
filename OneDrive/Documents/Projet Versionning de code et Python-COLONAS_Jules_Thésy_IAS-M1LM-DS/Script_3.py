#!/usr/bin/env python
# coding: utf-8

# ### Script 3

# #### c) Implémentons la suite de Fibonacci.

# In[1]:


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





# In[ ]:




