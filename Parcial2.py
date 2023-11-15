def esMutante(dna):
    def comprobar_secuencia(secuencia):
        for i in range(len(secuencia) - 3):
            if secuencia[i] == secuencia[i + 1] == secuencia[i + 2] == secuencia[i + 3]:
                print("Secuencia encontrada:", secuencia[i:i + 4])
                return True
        return False

    def comprobar_mutante(matriz):
        for row in matriz:
            if comprobar_secuencia(row):
                return True

        for col in zip(*matriz):
            if comprobar_secuencia(col):
                return True
        
        for i in range(len(matriz) - 3):
            for j in range(len(matriz[0]) - 3):
                diag = [matriz[i + k][j + k] for k in range(4)]
                if comprobar_secuencia(diag):
                    return True

        for i in range(3, len(matriz)):
            for j in range(len(matriz[0]) - 3):
                diag = [matriz[i - k][j + k] for k in range(4)]
                if comprobar_secuencia(diag):
                    return True

        return False

    # Construir la matriz de 6x6
    dna_matriz = [list(fila.upper()) for fila in dna]

    # Verificar si hay mutantes en la matriz
    return comprobar_mutante(dna_matriz)

# Ejemplo de prueba
condicion = False
contador = 0
palabra1 = ""
palabra2 = ""
palabra3 = ""
palabra4 = ""
palabra5 = ""
palabra6 = ""

while not condicion:
    if contador == 6:
        break

    fila = input("Ingrese una fila de 6 letras para la cadena de ADN: ")

    if len(fila) != 6 or any(letra.upper() not in {'T', 'C', 'G', 'A'} for letra in fila):
        print("Recuerde que la fila debe contener exactamente 6 letras y ser A, T, C o G.")
    else:
        if len(palabra1)<6:
            palabra1 = fila
            contador = contador+1
        elif len(palabra2)<6:
            palabra2 = fila
            contador = contador+1
        elif len(palabra3)<6:
            palabra3 = fila
            contador = contador+1
        elif len(palabra4)<6:
            palabra4 = fila
            contador = contador+1
        elif len(palabra5)<6:
            palabra5 = fila
            contador = contador+1
        elif len(palabra6)<6:
            palabra6 = fila
            contador = contador+1


dna = [palabra1, palabra2, palabra3, palabra4, palabra5, palabra6]

# Verificar si la matriz contiene mutantes
for fila in dna:
    for letra in fila:
        print(f"|{letra.upper()}", end = "")
    print("|")
resultado = esMutante(dna)
# Mostrar el resultado al usuario
if resultado:
    print("¡Es un mutante!")
else:
    print("No es un mutante.")
