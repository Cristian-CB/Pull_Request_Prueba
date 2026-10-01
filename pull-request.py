#Vamos a crear una función de rotación circular. Consiste en una rotación de n números en una dirección (izquierda o derecha) de una determinada lista.
#Por ejemplo, la siguiente lista:

lista = [2, 4, 1, 3, 7, 9]

#Se le aplicaría f(lista, 2, right) y tendría la siguiente salida:
#return [7, 9, 2, 4 , 1, 3]


def f(vector, n, dir):

    """x = slice(len(vector)-n, len(vector))
    lista1 = vector[x]
    #print(lista1)

    y = slice(len(vector)-n)
    lista2 = vector[y]
    #print(lista2)

    lista1.extend(lista2)
    print(lista1)"""

    if dir == "rigth":
        print(vector[-n:] + vector[:-n])

    elif dir == "left":
        print(vector [n:] + vector[:n])

    else:
        print("¬_¬")


f(lista, 2 , "rigth")