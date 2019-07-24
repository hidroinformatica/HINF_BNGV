T=['0-60','60-120','120-180','180-240','240-300','300-360','360-420','420-480','480-540','540-600','600-660',
   '660-720','720-780','780-840','840-900','900-960','960-1020','1020-1080','1080-1140','1140-1200','1200-1260',
   '1260-1320','1320-1380','1380-1440']


def Distribucion(P,distribucion):
    print()   
    print("Distribución",distribucion)
    print("-"*23)
    print('%6s %15s '%("T(Años)","Distribución"))
    for k,v in P.items():
        print('%6s %10.2f'%(k,v))

def Precipitaciones(P):
    print("\nPrecipitaciones máximas por año:")
    print("-"*33)
    print("Número de años: ", len(P))
    print()
    #print('%6s %10s %10s'%("Año","Maximo","Mes"))
    print('%6s %10s'%("Año","Maximo"))
    for k,v in P.items():
        #print('%6s %10s %10s'%(k,v[-4],meses[v[-1]-1]))
        print('%6s %10s'%(k,v[-1]))
    
def Depuradas(P):  
    #Imprimir las precitaciones maximas mensuales por año depuradas
    #meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"]
    print("\nPrecipitaciones máximas por año depuradas:")
    print("-"*43)
    print("Número de años: ", len(P))
    print()
    #print('%6s %10s %10s'%("Año","Maximo","Mes"))
    print('%6s %10s'%("Año","Maximo"))
    for k,v in P.items():
        #print('%6s %10s %10s'%(k,v[-4],meses[v[-1]-1]))
        print('%6s %10s'%(k,v[-4]))
