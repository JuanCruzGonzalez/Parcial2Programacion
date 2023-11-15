# Proyecto Mutante Detector

Nombre: Juan Cruz Gonzalez
Legajo: 51559
Email: juancgonzalez0901@gmial.com

# De que va el proyecto
Este proyecto implementa un detector de mutantes basado en el análisis de cadenas de ADN. Utiliza una función `esMutante(dna)` que toma una lista de cadenas de ADN y verifica si contiene secuencias repetitivas que indican la presencia de un mutante.

## Cómo funciona

El código implementa varias funciones para analizar la matriz de ADN y buscar secuencias repetitivas en filas, columnas y diagonales. Si se encuentra alguna secuencia de cuatro letras idénticas, el ADN se clasifica como mutante.

La función principal es:

```python
def esMutante(dna):
    # ... (código de la función)
    return comprobar_mutante(dna_matriz)

condicion = False
contador = 0
palabra1 = ""
# ... (se omiten las demás variables)

while not condicion:
    # ... (código del ingreso de filas)

# Construir la lista de palabras
dna = [palabra1, palabra2, palabra3, palabra4, palabra5, palabra6]

# Mostrar la matriz de ADN
for fila in dna:
    for letra in fila:
        print(f"|{letra.upper()}", end="")
    print("|")

# Verificar si la matriz contiene mutantes
resultado = esMutante(dna)

# Mostrar el resultado al usuario
if resultado:
    print("¡Es un mutante!")
else:
    print("No es un mutante.")
```

# Cómo correrlo

Primero clonamos el repositorio con: git clone https://github.com/tu-usuario/tu-repositorio.git

Luego en la consola accedemos a el: cd tu-repositorio

Ejecutamos el archivo python Parcial2.py

Y seguimos las intrucciones que nos da en la consola para ingresar los datos.