import sys

def encriptar(cadena):
    cont = 1
    resultado = ''
    for letra in cadena:
        if cont % 2 == 0:
            num = ord(letra)
            nueva = chr(num + 3)
            resultado = resultado+nueva
        else:
            resultado = resultado + letra
        cont = cont + 1
    resultado = resultado.swapcase()
    resultado = resultado[::-1]
    return  resultado


def desencriptar(cadena):
    cont = 1
    resultado = ''
    cadena = cadena[::-1]
    cadena = cadena.swapcase()
    for letra in cadena:
        if cont % 2 == 0:
            num = ord(letra)
            nueva = chr(num - 3)
            resultado = resultado + nueva
        else:
            resultado = resultado + letra
        cont = cont + 1

    return resultado



if __name__ == '__main__':
    cadena = input("Cadena:")
    cad = encriptar(cadena)
    print(cad)
    cad2 = desencriptar(cad)
    print(cad2)
