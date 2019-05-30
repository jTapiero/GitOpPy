a=input('rentrer qqcose bsvp:\n') 
print(a)

b,c=4,'salut'
print(b)
print(c)

a = b = c ='yo'
print(a,b,c)

print(1+4*5\
    -32+64)

print(str(0))

res=0
while res<120:
    res+=4
    print(res)
res=1996
while res>1900:
    res-=4
    print(res)
i=1
while i <= 10:
    print('%r*7:'%i,i*7)
    i+=1 
def affichTablemult(nb):
    i=0
    while i < 10:
        print('{0}*{1}:'.format(i+1,nb),(i+1)*nb)
        i+=1 
affichTablemult(6)

if [1,2,3] in[[1,2,3],5] :
    print(0,True)
if [2] in[[1,2,3],5] :
    print(True)
if 2 in[[1,2,3],5] :
    print(True)
if 5 in[[1,2,3],5] :
    print(1,True)

texte=input('rentrer qqcose bsvp:\n') 
if 'o' in texte: 
    for var_a in texte:
        if var_a!='o':
            continue
        else:
            texte=list(texte)
            texte[texte.index(var_a)]='0'
            texte="".join(texte)
            "".join(texte)
            print(texte)
            break

yo=input('rentrer qqcose bsvp:\n')
print(texte,type(yo))
print(yo+5)    