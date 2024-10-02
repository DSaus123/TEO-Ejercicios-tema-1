def lee_numeros(n):
    lista = []
    while n != 0:
        num = int(input("Introduce un número: "))
        lista.append(num)
        n -= 1
    return lista

if __name__ == "__main__":
    res = lee_numeros(7)
    print(res)



