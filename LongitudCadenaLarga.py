def LongitudSubcadenaLarga(cadena):
    n = len(cadena)
    x = 0
    maximalen = 0
    for i in range(n):
        if not cadena[i].isdigit():
            maximalen = max(maximalen, i - x)
            x = i + 1
    maximalen = max(maximalen, n - x)
    return maximalen

print(f'\n{LongitudSubcadenaLarga("hfgit78mri5")}')
print(f'{LongitudSubcadenaLarga("lkoyr6543juyd1")} \n')