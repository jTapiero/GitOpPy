# exception 
'''
lorsque l interpreteur detecte une code ou un code deffectueux(commande impossible , variable non implementer,...)
il leve ce qu on apelle une exception pour faire remonter l erreur 
une exception est un objet compose dun nom et d'une explication de l erreur

ex: ZeroDivisionError: int division or modulo by zero

'''
# Try-Catch(Except) 
'''
try sert a 'essayer' une un bloc d instruction
il teste si la commande est possible et executable
si elle l est le programme continue normalement
si elle ne l est pas ine exception est levee elle est atrapper par le bloc catch 
le bloc dinstruction de catch s execute et le programme continue sont execution normalement apres
les try sont emboitable 

    declaration:
        1:  try:
                cmd1         
                cmd2
            except: 
                cmd1         
                cmd2
'''
# Except
'''
type of exception:-ValueError
                  -NameError
                  -TypeError
                  -ZeroDivisionError

le bloc except va permettre de capturer un exception est d executer 
un bloc dinstruction concernant la ou les errors attrape                   
le except: permet de capturer toutes types derreur et seffectue pour toutes les exceptions
il sutilise seul ou cas exceptionnel; en fin des listes de except

on peut renommer des exception et grace au renommage l utiliser en tant que variable
    ex: except ValueError as ExcepRet:
            print(ExcepRet)
il est possible de metrre plusieur except apres un try 
 (cela permet de gerer plusieur cas derreur)
    try:
        cmd1         
    except 1: 
        cmd1
    except 2: 
        cmd1

il est possible de creer des exception a detecter 
ex:
    raise [TypeException]('message de lexception')
    if anne >0:
        raise Valueerror('L annee est superieur a zero ')
  
''' 
# else  
'''
Dans le cas du try le else s execute quand le try na pas lever d erreur
ex:
    try:
        cmd
    except:
        cmd2
    else:
        print('cmd effectue')
'''
# finaly
'''
le bloc finaly s executera a la fin edes autres blocs peut importe si une exception est leve ou non  
ex:
    try:
        cmd
    except:
        cmd2
    else:
        print('cmd effectue')
    finaly:
        print('fin try')
'''
#pass
'''
pass se met apres un bloc d instruction 
il permet a passer le bloc sans rien faire 
ex:
    try:
        cmd
    except:
        pass
'''
