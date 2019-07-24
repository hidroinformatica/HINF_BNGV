import os
import math
import statistics
import copy

#------------------------Extraer datos de precipitacion de la base de datos--------------
fPath=os.getcwd()+"\\db.csv"
f=open(fPath,"r").read()
f=f[:-1]
f=f.split('\n')

#------------------------Diccionario con datos para contrastar---------------------------
Datos={'10':2.213,'11':2.247,'12':2.279,'13':2.309,'14':2.335,'15':2.247,'16':2.279,
       '17':2.309,'18':2.335,'19':2.361,'20':2.385,'21':2.408,'22':2.429,
       '23':2.448,'24':2.467,'25':2.486,'26':2.502,'27':2.519,'28':2.534,
       '29':2.549,'30':2.563,'31':2.577,'32':2.591,'33':2.604,'34':2.616,'35':2.628,
       '36':2.639,'37':2.65,'38':2.661,'39':2.671,'40':2.682,'41':2.692,
       '42':2.7,'43':2.71,'44':2.719,'45':2.727,'46':2.736,'47':2.744,'48':2.753,
       '49':2.76,'50':2.768,'55':2.804,'60':2.837,'65':2.866,'70':2.893,
       '75':2.917,'80':2.94,'85':2.961,'90':2.981,'95':3,'100':3.017,'110':3.049,
       '120':3.078,'130':3.104,'140':3.129}



#------------------------Convertir entero a Real--------------------------------------
def convToInt(n):
    return float(n)

#-------------Funcion para ordenar las precipitaciones de la base de datos--------------
def Precipitaciones(): 
    count=1
    max=0
    Precipitaciones={}
    for x in f:
        Lp=[convToInt(n) for n in x.split(',')]
        year=str(int(Lp[0]))
        Precipitaciones[year]=Lp[1:]   
    for x in Precipitaciones.keys():
        for i in Precipitaciones[x]:
            if i > max:
                max=i
            count=count+1
        Precipitaciones[x].append(max)
        max=0     
    return Precipitaciones

#--------------Funcion que descarta los datos fuera del limite establecido------
def Dudosos(P):
    L=copy.deepcopy(P)
    #LOG precipitaciones
    for k,v in L.items():
        L[k].append(math.log10(v[-1]))  
    #Numero de años de la muestra
    nL=len(L)
    #K = coeficiente al nivel de significación de 10%
    K=Datos[str(nL)]
    #SL= desviación standard de logaritmos de registros
    TL=[]
    count=0
    TLcount=0
    for v in L.values():
        TL.append(v[-1])
        TLcount=TLcount+v[-1]
        count=count+1
    SL=statistics.stdev(TL)
    
    #PLm = media de logaritmo de registros
    PLM=TLcount/count
    
    #(P/Pm - 1)^3
    for k,v in L.items():
        L[k].append(math.pow(v[-2]*SL,3))
    #PL1 = logaritmo de límite superior
    PL1=PLM+SL*K
    
    #PL2 = logaritmo de límite inferior
    PL2=PLM-SL*K
 
    #P1 = límite superior
    P1=math.pow(10,PL1)
  
    #P2 = límite inferior
    P2=math.pow(10,PL2)
    #Buscando datos dudosos entre las precipitaciones
    for k,v in L.items():
        if v[-3]<P2 or v[-3]>P1:
            """
            print()
            print("Dato Dudoso en el año ",k," cuyo valor es ",v[-3],
                  ", siendo los limites inferior y superior en este caso : "
                  ,round(P2,1)," y ",round(P1,1)," respectivamente.")
            """
            P={n:m for n,m in P.items() if n!=k}
            #Llamando a la funcion de nuevo con una nueva lista de precipitaciones menos el año
            #de dato dudoso
            return Dudosos(P)
    """  
    print()
    print("Nuevos valores de Limites: ")
    print("-"*25)
    print()
    print("Limite inferior =",round(P2,1))
    print("Limite superior =",round(P1,1))
    """
    #Devuelve las precipitaciones que no tienen datos dudosos
    return(L)
    
#---------Funcion que devuelve las preciptaciones sin años con máximas fuera de limite---------------    
def Depuradas(P):
    Pr=Dudosos(P)
    count=0
    for k,v in Pr.items():
        for i in v[:-3]:
            if i==v[-3]:
                count=count+1
                Pr[k].append(count)
            count=count+1
        count=0
    return Pr

#----------Funcion para obtener las precipitaciones maximas de los años depurados------------------    
def MaximosDepurados(P):
    maximos=[]
    years=[]
    #Pr=Dudosos(P)
    for v in P.values():
        maximos.append(v[-4])
    for x in P.keys():
        years.append(int(x))
    return maximos

#----------Funcion para obtener las precipitaciones maximas de los años -----------------------
def Maximos(P):
    maximos=[]
    years=[]
    for v in P.values():
        maximos.append(v[-1])
    for x in P.keys():
        years.append(int(x))
    return maximos