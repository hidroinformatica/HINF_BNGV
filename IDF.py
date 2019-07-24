import math
from sklearn import linear_model
import numpy as np

#----------------Inicializar datos para el calculo-------------------------------------
#T (años)
T=['5','10','35','50','100','500']

DIDF=[(0.17,10.00),(0.33,20.00),(0.50,30.00),(0.67,40.00),(0.83,50.00),(1.00,60.00),
          (1.50,90.00),(2.00,120.00),(4.00,240.00),(6.00,360.00),(7.00,420.00),
          (8.00,480.00),(10.00,600.00),(11.00,660.00),(12.00,720.00)]
DP=[0.29,0.34,0.38,0.41,0.43,0.45,0.50,0.54,0.64,0.71,0.73,0.76,0.80,0.82,0.84,1.00]

Hr=[0.17,0.33,0.50,0.67,0.83,1.00,1.50,2.00,4.00,6.00,7.00,8.00,10.00,11.00,12.00,24.00]

Mn=[10.00,20.00,30.00,40.00,50.00,60.00,90.00,120.00,240.00,360.00,420.00,480.00,600.00,660.00,720.00,1440.00]

Dmin=[60,120,180,240,300,360,420,480,540,600,660,720,780,840,900,960,1020,1080,1140,1200,1260,1320,1380,1440]

Tr=[140,500]

def Seleccionar(D):
    DT={}
    for x in D.keys():
        if x in T:
            DT[x]=D[x]
    return DT

def Precipitacion(D):
    DT=Seleccionar(D)
    C={}
    for x in DT.keys():
        Tmp=[DT[x]* y for y in DP]
        C[x]=Tmp
    return C

def Intensidad(C):
    CD=Precipitacion(C)
    I={}
    for x in CD.keys():
        tmp=zip(CD[x],Hr)
        Producto=[x[0]/x[1] for x in tmp]
        I[x]=Producto    
    return I

def Analisis(C):
   #A=Intensidades(C)
   x2=[]
   x1=[]
   z1=[]
   xs=[]
   for y in T:
       x1=[math.log10(x) for x in Mn]
       x2=x2+x1
       for z in range(len(Mn)):
           z1.append(math.log10(int(y)))
   ys=[[x2[i],z1[i]] for i in range(0,len(z1))]

   for x in Intensidad(C).values():
       for y in x:
           xs.append(math.log10(y))
           
   x, y = np.array(xs), np.array(ys)
   
   model = linear_model.LinearRegression().fit(y,x)
   
   k=model.intercept_
   n=model.coef_[0]
   m=model.coef_[1]
   return k,n,m

def Retorno(D):
    k,n,m=Analisis(D)
    n=0.75
    Pa=[]
    Pb=[]
    PrI=[]
    Precipitacion=[]
    x1=math.pow(10,k)
    I=[(x1*(math.pow(Tr[0],m)))/(math.pow(x,n)) for x in Dmin]
    PrA=[I[i]*(Dmin[i]/60) for i in range(0,len(I))]
    Pa.append(PrA[0])
    Pb=[PrA[x+1]-PrA[x] for x in range(len(PrA)-1)]
    PrI=Pa+Pb
    Ap=PrI[0]
    PrI=PrI[1:]
    ApOdd=[PrI[x] for x in range(len(PrI)) if x%2!=0]
    ApEven=[PrI[x] for x in range(len(PrI)) if x%2==0]
    Precipitacion=ApEven[::-1]
    Precipitacion=Precipitacion+Pa+ApOdd
    return Precipitacion
    
    
    
    
    