#!/usr/bin/env python
# coding: utf-8

# In[888]:


import numpy as np
import pandas as pd
import random
from random import randint
from random import shuffle


# In[911]:


n = 100000


# In[912]:


class Inmate:
    id = None
    isOut = None
    
    def __init__(self,id,isOut=False):   
        self.id = id
        self.isOut = False
        
    def updateIsOut(self,box):
        if(box.id == self.id):
            self.isOut = True
        return self.isOut
    
    def Go(self,gulag):
        nextBox = self.id
        opened_boxes = 0
        while(opened_boxes < n/2 and self.isOut == False):
            self.updateIsOut(gulag.boxes[nextBox])
            nextBox = gulag.boxes[nextBox].id
            opened_boxes = opened_boxes+1
                         
        return self.isOut


# In[913]:


class Box:
    id = None
    def __init__(self,id):   
        self.id = id


# In[914]:


class Gulag:
    boxes = None
    def __init__(self):
        self.boxes = []
        for i in range(n):  
            tmp = Box(i)
            self.boxes.append(tmp)
        shuffle(self.boxes)        


# In[915]:


class Riddle:
    
    inmates = None
    gulag = None
    
    def __init__(self):
        self.inmates = []
        self.gulag = Gulag()
        for i in range(n):  
            tmp = Inmate(i)
            self.inmates.append(tmp)      
    
    def play(self):
        for i in self.inmates:
            if i.Go(self.gulag) == False:
#                 print("Mission Faild ,will get them next time !")
                return False
#         print("---------------------------")
#         print("We Did it !, We are Free")
        return True
        


# In[ ]:


seccess = 0
tries = 100
for x in range(tries):
    g = Riddle()
    res = g.play()
    if res == True:
        seccess=seccess+1
prc = seccess/tries
print("% of Seccess is "+str(prc))


# In[ ]:





# In[ ]:





# In[ ]:





# In[244]:





# In[ ]:





# In[35]:





# In[ ]:




