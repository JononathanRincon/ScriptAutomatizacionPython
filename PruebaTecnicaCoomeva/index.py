arreglo = ['p','l','h','y','a','f','z','v','x','r','q','b','e','w','r','z','q','y','d','a','a','y','v','r','g','r','c','z','j','b','b','n','o','v','n','v','w','a','i','i']

def Ordenamiento(arreglo):
    return sorted(arreglo)

def obtenerVocales(arreglo):
    vocales = ['a','e','i','o','u']
    return [vocal for vocal in arreglo if vocal in vocales]

def eliminarVocales(vocales, nombre):
    
    for vocal in nombre:
        if vocal in vocales:
            vocales.remove(vocal)
    return vocales

OrdenarArreglo = Ordenamiento(arreglo)
print(f"arreglo ordenado {OrdenarArreglo}")

OrdenarVocales =obtenerVocales(OrdenarArreglo)
print(f"vocales del arreglo ordenado {OrdenarVocales}")

nombre= input("Nombre que desea buscar en el arreglo: ")
nombreMinuscula = nombre.lower()

vocalesEliminadas = eliminarVocales(OrdenarVocales, nombreMinuscula) 
print(f"vocales  eliminadas {vocalesEliminadas}")


