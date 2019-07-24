import math
import Distribucion
import statistics
from scipy.stats import norm
import Precipitacion
#----------------Inicializar datos para el calculo-------------------------------------
def Initializar(M):
    MO=sorted(M,reverse=True)
    LMO=list(map(lambda x: math.log(x),MO))
    LNMO=list(map(lambda x: math.log10(x),MO))
    F0=[1-(x/(len(M)+1)) for x in range(1,(len(M)+1))]
    
    return MO,LMO,LNMO,F0

#-----------------------------Kolmogorov de la distribucion Normal-----------------------------------
def Normal(M):
    MO,LMO,LNMO,F0=Initializar(M)
    #Zn=[(x-Distribucion.Promedio(M))/statistics.stdev(M) for x in MO]
    Fx=[norm.cdf(x, Distribucion.Promedio(M), statistics.stdev(M)) for x in MO]
    K=list(map(lambda x: abs(x[0]-x[1]),zip(Fx,F0)))
    max=0
    for x in K:
        if x > max:
            max=x
    #Maximo Distribucion Normal
    return max

#-------------------------Kolmogorov de la distribucion LogNormal-----------------------------------
def LogNormal(M):
    MO,LMO,LNMO,F0=Initializar(M)
    #Zk
    #Zk=[(x-My)/Dey for x in y]
    Fx=[norm.cdf(x,Distribucion.Promedio(LMO),statistics.stdev(LMO)) for x in LMO]
    K=list(map(lambda x: abs(x[0]-x[1]),zip(Fx,F0)))
    max=0
    for x in K:
        if x > max:
            max=x
    #Maximo Distribucion LogNormal
    return max

#----------------------------Kolmogorov de la distribucion Gumbel-----------------------------------
def Gumbel(M):
    MO,LMO,LNMO,F0=Initializar(M)
    Kg=list(map(lambda x: (x-Distribucion.Promedio(M))/statistics.stdev(M),MO))
    T=[1/(1-math.exp(-math.exp(-(0.5772+(math.pi*x/math.sqrt(6)))))) for x in Kg]
    Fx=[1-(1/x) for x in T]
    K=list(map(lambda x: abs(x[0]-x[1]),zip(Fx,F0)))
    max=0
    for x in K:
        if x > max:
            max=x
    #Maximo Distribucion Gumbel
    return max
#----------------------Buscar el minimo de los tres Kolmogorov---------------------------
def Seleccionar(P):
    min=10000
    KNormal=Normal(Precipitacion.Maximos(P))
    KLogNormal=LogNormal(Precipitacion.Maximos(P))
    KGumbel=Gumbel(Precipitacion.Maximos(P))
    
    for x in (KNormal,KLogNormal,KGumbel):
        if x < min:
            min=x
       
    if min==KNormal:
        return'Normal'
    elif min == KLogNormal:
        return 'LogNormal'
    else:
         return 'Gumbel'
         
