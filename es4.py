#scrivere un programma che dati due punti in un piano cartesiano
#scriva l'equazione della retta associata e mandi in output il messaggio
#con la positività, negatività del coefficiente angolare.

import random
def calcolo_m ( xuno , xdue , yuno , ydue ) :
    m = ( ydue - yuno ) / ( xdue - xuno )
    return ( m )


def equazione ( m , x , y ) :
    eq = " y - " + str ( y ) + " = " + str ( m ) + " ( x - " + str ( x ) + " ) "
    print ( eq )
    
def controllo_m ( m ):
    if m > 0 :
        print ( " m ha segno positivo " )
    elif m == 0 :
        print ( " m è nullo " )
    else:
        print ( " m ha segno negativo " )
if __name__=="__main__":
    xuno = random.randint ( - 20 , 20 )
    xdue = random.randint ( - 20 , 20 )
    yuno = random.randint ( - 20 , 20 )
    ydue = random.randint ( - 20 , 20 )
    
    coefficiente_angolare = calcolo_m ( xuno , xdue , yuno , ydue )
    print ( coefficiente_angolare )
    equazione ( coefficiente_angolare , xdue , ydue )
    controllo_m ( coefficiente_angolare )