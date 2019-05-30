"""Documentation du module tabmultiply """
def tabMult(nb,nb2=10):
    """
    Affiche la table de multiplication de nb
    input:
        nb:int             ==> le chiffre a multiplier
        nb2:int default:10 ==> jusqua ou multiplier le chiffre
    output:
        no return 
    """
    i=0
    while i<nb2:
        print("{0}*{1}:".format(i+1,nb),(i+1)*nb)
        i+=1
tabMult(5)
tabMult(nb2=20,nb=5)
help(tabMult)
help('os.system')
print("mod",__name__)

#NOT WORKING
#lmb=lambda x,y: x*y  
#var3=lmb(7,5)
#print(var3)