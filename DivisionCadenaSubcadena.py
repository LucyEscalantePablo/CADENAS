def CadenaSubcadena(cadena, coma):
    return cadena.split(coma)

a="mundo,de,maravillas,del,universo"
print(f'\n {CadenaSubcadena(a,",")}\n')
