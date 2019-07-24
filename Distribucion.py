import math
import statistics

#----------------Inicializar datos para el calculo-------------------------------------
#T,Años
T=[2,5,10,30,35,50,71,100,140,175,500]
#Pr,Probabilidad
Pr=[1/x for x in T]
#W,Logaritmo niperiano
W=[math.sqrt(math.log(1/(math.pow(x,2)))) for x in Pr]
#Variable Z
z=[(x - ((2.515517+0.802853*x+0.010325*x**2)/(1+1.432788*x+0.189269*x**2+0.001308*x**3))) for x in W]
#Coeficiente K
Kt=[-1*(math.sqrt(6)/math.pi)*(0.5772+(math.log10(math.log10(x/(x-1))))) for x in T]

#---------------------------Calculo de Promedio-------------------------------------------
def Promedio(M):
    count=0
    suma=0.0
    for x in M:
        suma=suma + x
        count=count+1
    promedio=suma/count
    return promedio

#-------------------------------Distribucion normal------------------------------------------
def Normal(M):
    DNormal={}
    count=0
    #Distribucion 
    D=[Promedio(M)+(statistics.stdev(M)*x) for x in z]
    #Creando diccionario de distribucion 
    for x in T:
        DNormal[str(x)]=D[count]
        count=count+1
    return(DNormal)
    
#--------------------------------Distribucion LogNormal-----------------------------------
def LogNormal(M):
    DLNormal={}
    count=0
    #Distribucion 
    LM=list(map(lambda x: math.log10(x),M))
    D=[Promedio(LM)+(statistics.stdev(LM)*x) for x in z]
    #Creando diccionario de distribucion 
    for x in T:
        DLNormal[str(x)]=math.pow(10,D[count])
        count=count+1
    return(DLNormal)
    
#-----------------------------Distribucion Gumbel----------------------------------------
def Gumbel(M):
    DGumbel={}
    count=0
    #Distribucion 
    D=[Promedio(M)+(statistics.stdev(M)*x) for x in Kt]
    #Creando diccionario de distribucion 
    for x in T:
        DGumbel[str(x)]=D[count]
        count=count+1
    return(DGumbel)
