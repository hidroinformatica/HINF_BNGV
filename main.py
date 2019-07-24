import Precipitacion
import Distribucion
import Kolmogorov
import Impresion
import IDF

#-------------Initializar Precipitaciones--------------------------------------
P=Precipitacion.Precipitaciones()
PD=Precipitacion.Depuradas(P)

#-------------Imprimir Precipitaciones-----------------------------------------
Impresion.Precipitaciones(P)
Impresion.Depuradas(PD)
    
#-------------Distribucion Normal-----------------------------------------------
DN=Distribucion.Normal(Precipitacion.Maximos(P))
nombre='Normal'
Impresion.Distribucion(DN,nombre)  

#-------------Distribucion LogNormal--------------------------------------------
DLN=Distribucion.LogNormal(Precipitacion.Maximos(P))
nombre='LogNormal'
Impresion.Distribucion(DLN,nombre)

#-------------Distribucion Gumbel--------------------------------------------
DG=Distribucion.Gumbel(Precipitacion.Maximos(P))
nombre='Gumbel'
Impresion.Distribucion(DG,nombre)
#-------------Seleccion de Distribucion----------------------------------------
nombre=Kolmogorov.Seleccionar(PD)
if nombre=='Normal':
    seleccionado=DN
elif  nombre=='LogNormal':
    seleccionado=DLN
else:
    seleccionado=DG
print()
print('Distribución seleccionada:')   
Impresion.Distribucion(seleccionado,nombre)
#------------------------IDF----------------------------------------
#Años para IDF
print(IDF.Retorno(seleccionado))

