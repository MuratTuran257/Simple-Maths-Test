#!/usr/bin/env python
# coding: utf-8

# In[58]:


def number_property(n):
    output=[]
    asalk=0
    if n>=2:
        for i in range(2,n):
            if n%i==0:
                asalk+=1
            else:
                pass
        if asalk==0:
            output.append(True)
        else:
            output.append(False)
    else:
        output.append(False)
    if n%2==0:
        output.append(True)
    else:
        output.append(False)
    if n%10==0:
        output.append(True)
    else:
        output.append(False)
    print(output)


# In[60]:




