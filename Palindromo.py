
def Palindromo(cadena):
    return cadena == cadena[::-1]

print(f'\nLa palabra ANA es palindromo?: {Palindromo("ANA")}')
print(f'La palabra ANA es palindromo?: {Palindromo("caballo")}\n')
