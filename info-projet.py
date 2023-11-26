from random import randint
def genereMat(n,m):
    MAT=[[0 for j in range(m)]for i in range(n)]
    for a in range(2):
        for i in range(1,len(MAT)):
            j=randint(0,len(MAT[i-1]))
            MAT[i][j-1]=1
    x=0
    #Apparition d objet
    i=randint(0,n-1)
    j=randint(0,m-1)
    if MAT[i][j]==0:
        MAT[i][randint(0,len(MAT[i])-1)]=2
    if MAT[i][j]==1:
        MAT[i][j]=2
    #placement de trou sur la map
    while x <3:
        k=randint(0,n-1)
        l=randint(0,m-1)
        if MAT[k][l]==0:
            MAT[k][randint(0,len(MAT[k])-1)]=3
            x+=1
        if MAT[k][l]==1:
            x+=1
        if MAT[k][l]==2:
            x+=1
    return MAT

def voisinage(point) :
    x,y = point
    return {(x+1,y),(x-1,y),(x,y+1),(x,y-1)}

def test(m,e,s) :
    cc = {e}
    voisins = {p for p in voisinage(e) if valide2(m,p)}
    while len(voisins)>0 :
        cc = cc | voisins
        voisins = {p  for c in cc for p in voisinage(c) if valide2(m,p) and p not in cc} 
    return s in cc
def valide2(m,coord):
    x,y = coord
    if x<0  or y<0 or x>=len(m) or y>=len(m[0]) :
        return False
    if m[x][y] == 1 :
        return False
    return True

def create_perso(pos):
    (x,y)= pos
    return {"char":"o",'x':x, 'y':y}

def display_map_and_char(l,la,perso):
    letter,f="s",False
    while f==False:
        m=genereMat(l,la)
        print(m)
        p=create_perso(perso)
        f=test(m,perso,(3,3))
    while letter !="r":
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i == p['x'] and j == p['y']:
                    print(p['char'], end='')
                else:
                    print(dico[m[i][j]],end="")
            print()
        letter = input("Entrez une lettre (z, q, s, d): ")
        update_p(letter, p,m)
    
dico={0:' ',1:'#', 2:'B',3:'X'}

def valide(m,coord):
    x,y = coord['x'], coord['y']
    if x<0  or y<0 or x>=len(m) or y>=len(m[0]) :
        return False
    if m[x][y] == 1 :
        return False
    return True

def update_p(letter, p,m):
    if letter == "z":
        p["x"] = p["x"] - 1
        if not valide(m,p):
            p["x"]= p["x"] +1
    elif letter == "q":
        p["y"] = p["y"]- 1
        if not valide(m,p):
            p["y"] = p["y"]+ 1
    elif letter == "s":
        p["x"] = p["x"] + 1
        if not valide(m,p):
            p["y"] = p["y"]- 1
    elif letter == "d":
        p["y"] = p["y"]+ 1
        if not valide(m,p):
            p["y"] = p["y"]- 1
    elif letter =="r":
        print("Vous avez arrêté le jeu.")
    else:
        print("La lettre {} n'est pas valide.".format(letter))

display_map_and_char(6,6,(1,1))
