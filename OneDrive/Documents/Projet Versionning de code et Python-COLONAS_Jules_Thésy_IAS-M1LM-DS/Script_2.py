#!/usr/bin/env python
# coding: utf-8

# ### Script 2

# #### b) Implémentons la fonction factorielle.

# In[2]:


def factorielle(n):
   if n == 0:
      return 1
   else:
      F = 1
      for k in range(2,n+1):
         F = F * k

      return F


# In[3]:


factorielle(5)


# In[ ]:





# In[ ]:




