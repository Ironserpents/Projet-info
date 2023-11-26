from random import randint
def genereMat(n,m):
    MAT=[[0 for j in range(m)]for i in range(n)]
    for i in range(1,len(MAT)):
        j=randint(0,len(MAT[i])-1)
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
    while x <5:
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

def create_perso(pos):
    (x,y)= pos
    return {"char":"o",'x':x, 'y':y}

def display_map_and_char(l,la,perso):
    letter="s"
    m=genereMat(l,la)
    p=create_perso(perso)
    while letter !="r":
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i == p['x'] and j == p['y']:
                    print(p['char'], end='')
                else:
                    print(dico[m[i][j]],end="")
            print()
        letter = input("Entrez une lettre (z, q, s, d): ")
        update_p(letter, p)
    
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
