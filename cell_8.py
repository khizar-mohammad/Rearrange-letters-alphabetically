#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def AlphabetSoup(str):
  new_str = list(str)
  for i in range(0,len(new_str),1):
    char = ord(new_str[i])
    new_str[i] = char

  for i in range(0,len(new_str),1):
    for j in range(0,(len(new_str)-1),1):
      if new_str[j] > new_str[j+1]:
        new_str[j], new_str[j+1] = new_str[j+1], new_str[j]

  for i in range(0,len(new_str),1):
    if new_str[i] == 32:
      del new_str[i]

  for i in range(0,len(new_str),1):
    char = chr(new_str[i])
    new_str[i] = char

  str = ''.join(new_str)
  return str

str = input("please enter word: ")
print (AlphabetSoup(str))

