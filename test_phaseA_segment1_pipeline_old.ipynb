#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')
# Kill all ray servers before restarting

#!ray stop


# In[2]:


#!ray start --head --port=6379 --redis-password="cbgt2"
#!ray start --address='10.0.0.33:6379' --redis-password='cbgt2'


# In[3]:


import cbgt as cbgt
from frontendhelpers import *
import init_params as par

# In[32]:


import json


# In[33]:


pl = cbgt.Pipeline()


# In[ ]:





# In[34]:

'''
def helper_paramset(params=dict()):
    # this function is defined in a "normal way" outside the context of the pipeline.
    # this function be basically anything, it's just to demonstrate that outside functions
    # can be used in code block modules
    celldefaults = in_par.init_neuron_params(params)


    return celldefaults
'''

# In[35]:


def codeblock_paramset(self):
    # you can do pretty much anything you want in here
    self.celldefaults = par.helper_paramset(self.params)


# In[36]:


pl.add(codeblock_paramset)


# In[37]:


pl.modulelist


# In[42]:


environment = {
    'params':{}
}
results = cbgt.ExecutionManager(cores=7).run(pl,environment)
print(results)  


# In[29]:


results.keys()


# In[ ]:




