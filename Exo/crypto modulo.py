# -*- coding: cp1252 -*-
def decomposage(txtac):
    i=0
    l=[]
    while(i<len(txtac)):
        l=l+[txtac[i]]
        i=i+1
    return l
def verifpgcd26(A):
    again="true"
    while(again=="true"):
        S=A
        b=26
        l=[]
        if(A>b):
            q=A//b#A=b*q#
            r=A%b#A=b*q+r#
            l=l+[r]
            while(r!=0):
                A=b
                b=r
                q=A//b#A=b*q#
                r=A%b#A=b*q+r#
                l=l+[r]
        else:
            q=b//A#b=A*q#
            r=b%A#b=A*q+r#
            l=l+[r]
            while(r!=0):
                b=A
                A=r
                q=b//A#b=A*q#
                r=b%A#b=A*q+r#
                l=l+[r]
        z=len(l)-2
        if(l[z]!= 1):
            print("attention cles de codage invalide\nveuillez rentrer une nouvelle cle:")
            A=int(input())
        else:
            again="false"
    return S
def transcodage(n):
    f=0
    if(n=="a"):
        f=0
    if(n=="b"):
        f=1 
    if(n=="c"):
        f=2
    if(n=="d"):
        f=3
    if(n=="e"):
        f=4
    if(n=="f"):
        f=5
    if(n=="g"):
        f=6
    if(n=="h"):
        f=7
    if(n=="i"):
        f=8
    if(n=="j"):
        f=9
    if(n=="k"):
        f=10
    if(n=="l"):
        f=11   
    if(n=="m"):
        f=12
    if(n=="n"):
        f=13
    if(n=="o"):
        f=14
    if(n=="p"):
        f=15
    if(n=="q"):
        f=16
    if(n=="r"):
        f=17
    if(n=="s"):
        f=18
    if(n=="t"):
        f=19
    if(n=="u"):
        f=20
    if(n=="x"):
        f=21
    if(n=="w"):
        f=22
    if(n=="x"):
        f=23
    if(n=="y"):
        f=24
    if(n=="z"):
        f=25
    if(n==" "):
        f=85   
    return f
def invtranscodage(n):
    f=0
    if(n==0):
        f="a"
    if(n==1):
        f="b" 
    if(n==2):
        f="c"
    if(n==3):
        f="d"
    if(n==4):
        f="e"
    if(n==5):
        f="f"
    if(n==6):
        f="g"
    if(n==7):
        f="h"
    if(n==8):
        f="i"
    if(n==9):
        f="j"
    if(n==10):
        f="k"
    if(n==11):
        f="l"   
    if(n==12):
        f="m"
    if(n==13):
        f="n"
    if(n==14):
        f="o"
    if(n==15):
        f="p"
    if(n==16):
        f="q"
    if(n==17):
        f="r"
    if(n==18):
        f="s"
    if(n==19):
        f="t"
    if(n==20):
        f="u"
    if(n==21):
        f="v"
    if(n==22):
        f="w"
    if(n==23):
        f="x"
    if(n==24):
        f="y"
    if(n==25):
        f="z"
    if(n==85):
        f=" "   
    return f
    

def codage(a,B,l):
    i=0
    t=""
    v=[]
    while(i<len(l)):
        
        u=transcodage(l[i])
        if(u==85):
            Z=" "
        else:    
            z=(u*a)+B
            Z=z%26
        t=invtranscodage(Z)    
        v=v+[t]
        i=i+1
        
    return v
def clesdecode(A):
    i=0
    while((A*i)%26!=1):
        i=i+1
    return i    

def decodage(r,B,l,a):
    i=0
    t=""
    v=[]
    while(i<len(l)):
    
        u=transcodage(l[i])
        if(u==" "):
            Z=85
        else:    
            z=(u-B)*r
            Z=z%26
        t=invtranscodage(Z)    
        v=v+[t]
        i=i+1
        
    return v
        
        
            
#programme principale #
mdp="mot de passe"
j=0
k=0
while(j<3):
    print("veuiller rentrer un mot de passe:")
    mdpr=input()
    if(mdp==mdpr):
        j=4
        again="true"
        while (again=="true"):
            print("voulez vous:\n 1)coder \n 2)decoder \n 3)quitter")
            rep=input()
            while(rep!="1" and rep!="2" and rep!="3"):
                print("voulez vous:\n 1)coder \n 2)decoder \n 3)quitter")
                rep=input()
            if(rep=="1"):#coder#                
                print ("veuiller rentrer le texte a coder \n(attention ne peut encoder que du alpha-beta)")
                txtac=str(input())
                l=[]
                v=[]
                l=decomposage(txtac)
                print("la cles de codage\n a pour A:")
                print("attention A doit etre premier avec 26")
                A=int(input())
                a=verifpgcd26(A)
                print("et pour B:")
                B=int(input())
                v=codage(a,B,l)
                i=0
                k=""
                while(i<len(v)):
                    d=str(v[i])      
                    k=k+d
                    i=i+1
                print("voici votre code:\n",k)           

                
                              
            elif(rep=="2"):#decoder#
                print ("veuiller rentrer le texte a decoder \n(attention ne peut encoder que du alpha-beta)")
                txtac=str(input())
                l=[]
                l=decomposage(txtac)
                print("la cles de codage\n a pour A:")
                print("attention A doit etre premier avec 26")
                A=int(input())
                a=verifpgcd26(A)
                print("et pour B:")
                B=int(input())
                r=clesdecode(A)
                v=decodage(r,B,l,a)
                i=0
                k=""
                while(i<len(v)):
                    d=str(v[i])      
                    k=k+d
                    i=i+1
                print("voici votre code:\n",k)

            else:#quitter#
                print("etes vous sur?(o/n)")
                ret=str(input())
                if (ret=="o"):
                    again="false"
                    j=4
                else:
                    print("acces refuse")
                    j=j+1
                
if (j==4):
    print("au revoir")
else:
    print("acces refuse vous etes expulsé du programme")
        
 

          
    
