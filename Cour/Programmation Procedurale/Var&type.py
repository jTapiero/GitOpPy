#Les Variables
    '''
    une variables est un espace de stockage creer dynamyquement
    une variable est definie par la taille de l espace de stockage et par son type 
    il n'y a pas de de definition des variables
    on les ecris directement et python fais un typage dynamique(affecte automatiquement le type)
    sensible a la casse a =! A 

    Syntaxe Nomvar:
        -Alphanumerique + _
        -ne peut commencer par un chiffre 
        -camelCase  ou my_space (tt minuscule avec _ pour les espaces)


    '''
    NomVar=Val
#Les types 
    '''
    Un type ou type de donnee 
    est la categorie de la valeur qui est stockes dans la variable
    de par cette categorie sont aussi attribuer le taille de la variable 
    
    int    : Nombre entier positifs et negatif
    float  : Nombre Decimal positifs et negatif
    string : suite de Charactere alphanumerique 
        defini par: 'val' "val" """ val"""
        les "" peuvent contenir les ''
        \ permet de rendre string les charactere problematique
        \n saut de ligne
        \t Tabulation
    Bool   : peut contenir la valeur False ou True 

    fct:
        type(var) ==> permet d obtenir le type de la variable

    String Fct:
        str.lower()        ==> change tous les characteres en minuscule  
        str.upper()        ==> change tous les characteres en minuscules
        str.capitalize()   ==> Change le premier charactere en majuscule
        str.strip()        ==> Retire les especes en debut et fin de chaine 
        str.fct().center(x)==> met la chaine de taille x et centre les charactere au milieu de la chaine 
        
    '''
#Variable Scope
'''
referencement des variable en python
    en python une variable est compose de deux partie
    une partie 'label' et une partie objet
    la partie label possedent le nom de la variable et la reference vers un objet 
    la partie objet possedent une valeur un type et un id 

    la reference est une adresse dans l espace memoire de stockage de l ordinateur contenant l objet 
    
    en python lorsque une ou plusieur variable ont la meme valeur elle n ont pas plusieur objet contenneur qui leur sont associeer
    mais une objet/conteneur vers lequelle tous ces labels pointes

les variables mutables et immutables 
    il existe deux types de variables en python:

    les immutables:
        ce sont des variables qui ne 'changent' pas
        c est a dire que lorsque on affecte une nouvelle valeur sur cette variable
        l objet referenceer n est pas modifier c est a dire qu un autre objet contenant la nouvelle valeur se deer 
        et la variable reference vers ce nouvelles objet 

        ce sont les variables tel que int string float tuple

    les mutables:
        ce sont des variables qui changent 
        generalement ce sont des listes ou des dictionnaires(elements contenant des variables immutables)
        lorsque on essayent de les changer par affectation ils ont le meme comportement que les variables immutables
        lorsqu on essaye de les modifier par une de leur propres methode de modification
        l objet lui meme est modifieer
            ex:list.append()
        on peut aussi creer deux variables immutable qui pointent vers le meme objet referend
        ex: liste1=list2
        le changement dans l un se repcutera dans l autre 
        pour creer une copie de la liste sans avoir le meme objet referend ont doit passer par le constructeur
        ex: list1=list(list2)

    id(x) sert a avoir la refference de l objet de la variable x
    is sert a comparer les id(remplacent ==)  

les espaces de nom

    un espace de nom est un espace memoire sous forme de dictionnaire
    contenant les differents elements du programme  permettant a l interpreteur de pouvoir manipuler les variables/fonction/objet
    les namespace peuvent simbriquer les un les autres
    
    lorsque python est lancer il possedent deja un namespace BUILT-in contenant les fonction de bases inclus dans python
    dans ce namespace built in va etre creer un namespace globale dans lequelle va etre executer notre code courant
    a chaque fois q une fonction, un objet,un package ou module sera appeler un sous namespace sera rajouter 
    de maniere ordonner au namespace global
    en fonction de l on nous trouvons nous trouvons different types de namespace
        namespace:-build-in : tous les entite contenu sont accesible dans tous les namespace
                  -global   : le namespace dans lequelle se trouve le namespece local 
                  -local    : le namespace dans lequel l interpreteur execute le programme 
                  -nested   : les ou le namespace contenue dans le namespace local

    les namespace creer pour des fonction se creer lors de leur appel et se detruisent lors de la fin de l execution de la fonction
    return permet de passer une valeur dun namespece a un autre 

    les namespaces sont architechturer de maniere pyramidale et comme un systeme de fichier
    ces a dire que un namespace local n a pas acces au varaibles du namespace nested mais elle a acces a en lecture seulement au varible du namespace globale
    pour modifier une variable globale dans un namespace local il faut utiliser l instruction global
    ex:
        vari=11 #namespace global
        def fct ():#namespace local
            global vari
            vari=30
    les variables locale de sclarent en dessous la docstring
    lorsque on import un module par la fonction 'import' on rajoute a notre namespace actuelle un objet liste contenant tous les elements ddu fichier importer
    pour acceder a ces elements il faut preciser leur adresse (c est aussi leur namespace) :module.element.elemet.fc()
    lorsquon modifie ces elements on les modifie dans leur namespace ce qui fait que leur acess est donne par namespace globale mais leur modification ce fait comme l orsq il sont en local

    
    lorsqu on utilise from '' import ==> on insere dans le namespece global 
    pour l import de module et/ou de package va sajouter au namespace locale(ou global) tous le namespace
    du module
    un namespace va permettre a ne pas se retrouver a avoir plusieur fois la meme variables dans un seul et meme namespace

les scopes des variables
    ce qu on apelle scope ou portee des variables sont l espace dans laquelle est peuvent etre appeler
    si les variables contenu dans le namespace local sont des variables local
    les variables contenu dans le namespace global sont des variables globales


'''


