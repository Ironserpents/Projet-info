from random import randint
import time
def genereMat(n,m):
    MAT=[[0 for j in range(m)]for i in range(n)]
    for a in range(0,2):
        for i in range(1,len(MAT)):
            j=randint(0,len(MAT[i-2]))
            MAT[i][j-1]=1
    x=0
    #Apparition d'instincteur
    i=randint(0,n-1)
    j=randint(0,m-1)
    if MAT[i][j]==0:
        MAT[i][randint(0,len(MAT[i])-1)]=2
    if MAT[i][j]==1:
        MAT[i][j]=2
    #placement de flammes sur la map
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
    MAT[3][3]=4
    return MAT
#tout les déplacements possible du perso
def voisinage(point) :
    x,y = point
    return {(x+1,y),(x-1,y),(x,y+1),(x,y-1)}
#vérification que la map peut se faire
def test(m,e,s) :
    if m[s[0]][s[1]]== 1:
        return False
    cc = {e}
    voisins = {p for p in voisinage(e) if valide2(m,p)}
    while len(voisins)>0 :
        cc = cc | voisins
        voisins = {p  for c in cc for p in voisinage(c) if valide2(m,p) and p not in cc} 
    return s in cc
#verifie que le perso sort pas de la map ou va sur un mur ou trou
def valide2(m,coord):
    x,y = coord
    if x<0  or y<0 or x>=len(m) or y>=len(m[0]) :
        return False
    if m[x][y] == 1 :
        return False
    if m[x][y]== 3:
        return False
    return True

def create_perso(pos,o):
    (x,y)= pos
    return {"char":"o",'x':x, 'y':y, "objet":o}


def display_map_char_and_objects(l,la,perso):
    r=input("Quel est votre nom ? :")
    print( r," :Qu'est ce qui se passe? de la fumée...")
    time.sleep(3)
    print(r,":Le batiment prend feu, il faut sortir vite")
    a=4
    n=time.time()
    while a!=-1:     
        letter,f,="s",False
        while f==False:
            m=genereMat(l,la)
            p=create_perso(perso,0)
            f=test(m,perso,(3,3))
        while letter !="r":
            if time.time()-n > 30:
                print(r,": On non il y a du feu de partout.")
                if p["objet"] >0:
                    print(r,":Même avec l'extinteur je ne peux rien faire")
                print(r,":Aieee, ca brûle !")
                time.sleep(5)
                print("Le batiment a totalement pris feu")
                return
            for i in range(len(m)):
                for j in range(len(m[0])):
                    if i == p['x'] and j == p['y']:
                        print(p['char'], end='')
                    else:
                        print(dico[m[i][j]],end="")
                print()
            letter = input("Entrez une lettre (z, q, s, d): ")
            update_p(letter, p,m)
            if m[p['x']][p['y']] ==2:
                p["objet"]=p["objet"]+1
                print(r,":Oh un extincteur, ca pourra me permmettre d'enlever un peu de feu")
                m[p['x']][p['y']]=0
            if m[p['x']][p['y']] ==3:
                if p["objet"]>0:
                    p["objet"]=p["objet"]-1
                    print(r,": Autant utilisais un extincteur")
                    m[p['x']][p['y']]=0                    
                else:
                    print(r,":Aieee, ca brûle")
                    time.sleep(3)
                    print("Vous avez pris feu")
                    return
            if p['x']== 3 and p['y'] ==3:
                if a==0:
                   print(r,":J'ai survécu !!!")
                   time.sleep(2)
                   print(r,": C'était juste")
                   a=a-1
                   break
                else:
                    if p["objet"]>0:
                        print("Les escaliers que vous avez pris été trop fragile, vous avez enlevé vos extincteurs.")
                    print (r,":Aller, je suis à l'étage",a,"\n Je peux le faire")
                    a=a-1
                    break
            
dico={0:' ',1:'#', 2:'B',3:'X',4:'E'}

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
            p["x"] = p["x"]- 1
    elif letter == "d":
        p["y"] = p["y"]+ 1
        if not valide(m,p):
            p["y"] = p["y"]- 1
    else:
        print("La lettre {} n'est pas valide.".format(letter))
display_map_char_and_objects(6,6,(1,1))
