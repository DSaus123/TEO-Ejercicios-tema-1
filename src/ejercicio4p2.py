def lee_numeros(n):
    lista = []
    for _ in range(n):
        num = float(input("Introduce un número: "))
        lista.append(num)
        
    return lista

if __name__ == "__main__":
    n = int(input("Introduce la cantidad de números que quieres leer: "))
    res = lee_numeros(n)
    print(f"\nLa lista final de {n} términos es: {res}")
    print(f"Máximo: {max(res)}")
    if len(res) != 0:
        print(f"Media: {sum(res) / len(res)}")
    else:
        print("No es posible calcular la media")
    contador = 0
    for num in res:
        if num % 2 == 0:
            contador += 1
    print(f"Números pare en la lista: {contador}")
    
    new_num = []
    for num in res:
        if num > 10:
            new_num.append(num)
    print(f"Nueva lista con términos mayores a 10: {new_num}")