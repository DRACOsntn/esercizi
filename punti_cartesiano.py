#dato un insieme di punti  su un piano cartesiano,
#random compresinell'intervallo
# 0,10. calcolare il punto  con ascissa massima e il punti con ordinata minima

import random

x=[]
y=[]
for i in range(0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))
    
#ascissa massima
#scorrere la lista delle x, trovare il massimo e salvare l'indice
#visualizzare poi con un print il numero
massimo=x[0]
indice_max=0
#minimo=y[0]
#inidce_min=0

for i in range (0,20):
    if x[i]>massimo:
        massimo=x[i]
        indice_max=i
print(massimo,y[indice_max])
        
for i in range(0,20):
    if y[i]<minimo:
        minimo=y[i]
        indice_min=i
        #print(minimo,x[indice_min])



punti_cartesiano=[]
for i in range (0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
            
#come accedere alla x del primo punto
#print(punti_cartesiano[0][0])
#come accedere alla y del primo punto
#print(punti_cartesiano[0][1])
