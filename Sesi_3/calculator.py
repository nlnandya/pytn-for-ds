#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(*args):
    res = 0
    for arg in args:
        res += arg
    return res

def multiply(*args):
    res = 1
    for arg in args:
        res = res * arg
    return res

def devide(*args):
    [res, *sisa] = []
    for arg in sisa:
        res = res / arg
    return res


# In[ ]:




