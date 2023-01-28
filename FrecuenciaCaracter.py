def FrecuenciaCaracter(cadena):
    frecuencia = {}
    for i in cadena:
        if i in frecuencia:
            frecuencia[i] += 1
        else:
            frecuencia[i] = 1
    return frecuencia

print(f'\n {FrecuenciaCaracter("maravila")}\n')