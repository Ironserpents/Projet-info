# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def display_map(m, d):
  for ligne in m:
    print("".join([d[x] for x in ligne]))

# m = [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
# d = {0: " ", 1: "#"}
# display_map(m, d)

def create_perso(départ):
    l=["x","y"]
    d={}
    d["char"]="o"
    for x in range(len(départ)):
        d[l[x]]=départ[x]
    return d
#create_perso((0,0))
